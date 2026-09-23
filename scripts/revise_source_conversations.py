#!/usr/bin/env python3
"""Render individually reviewed conversations from immutable WordPress snapshots.

The fixed Git revision supplies site chrome only. Each configuration contains
explicit, source-addressed edits and page-specific review decisions.
"""
import argparse
import copy
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

from bs4 import BeautifulSoup, Comment

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'quality/original-source-revisions'
TAGS = ['p', 'li', 'h3', 'h4']


def text(node):
    return node.get_text(' ', strip=True)


def own_text(node):
    """Exclude nested tracked blocks when counting unchanged source blocks."""
    clone = copy.deepcopy(node)
    for child in clone.find_all(TAGS):
        child.decompose()
    return text(clone)


def sections(source, config=None):
    result = []
    prose = (config or {}).get('proseSectionHeadingIndexes', [])
    pairs = (config or {}).get('pairedResponseHeadingIndexes', {})
    headings = source.select('h2')
    for index, h in enumerate(source.select('h2')):
        if index in pairs.values():
            continue
        cols = h.find_next_sibling().select(':scope > .wp-block-column')
        if index in (config or {}).get('siblingColumnHeadingIndexes', []):
            cols = []
            for sibling in h.find_next_siblings():
                if sibling.name == 'h2':
                    break
                cols.extend(sibling.select(':scope > .wp-block-column'))
        if str(index) in pairs:
            response_index = pairs[str(index)]
            assert response_index == index + 1
            response_heading = headings[response_index]
            assert response_heading.get_text().strip() == 'ChatGPT Response:'
            col = source.new_tag('div')
            for sibling in response_heading.find_next_siblings():
                if sibling.name == 'h2':
                    break
                col.append(copy.deepcopy(sibling))
            cols = [col]
        if index in (config or {}).get('preambleHeadingIndexes', []) and str(index) not in pairs:
            for sibling in h.find_next_siblings():
                if sibling.name == 'h2':
                    break
                cols = sibling.select(':scope > .wp-block-column')
                if cols:
                    break
        if index in prose:
            assert not cols
            col = source.new_tag('div')
            skip = (config or {}).get('prosePreambleCounts', {}).get(str(index + 1), 0)
            for position, sibling in enumerate(h.find_next_siblings()):
                if sibling.name == 'h2':
                    break
                if position < skip:
                    continue
                col.append(copy.deepcopy(sibling))
            cols = [col]
        if cols:
            result.append((h, cols))
    return result


def preamble_nodes(heading, config, n):
    if str(n) in config.get('prosePreambleCounts', {}):
        nodes = list(heading.find_next_siblings())[:config['prosePreambleCounts'][str(n)]]
        assert all(node.name != 'h2' for node in nodes)
        return nodes
    if n - 1 not in config.get('preambleHeadingIndexes', []):
        return []
    result = []
    for sibling in heading.find_next_siblings():
        if sibling.name == 'h2' or sibling.select(':scope > .wp-block-column'):
            break
        result.append(sibling)
    return result


def original_prompt(heading, config, n):
    if str(n) in config.get('promptContinuationPreambleIndexes', {}):
        continuation = preamble_nodes(heading, config, n)[config['promptContinuationPreambleIndexes'][str(n)]]
        assert continuation.name == 'p'
        return heading.get_text() + '\n' + continuation.get_text()
    if str(n) in config.get('promptPreambleIndexes', {}):
        p = preamble_nodes(heading, config, n)[config['promptPreambleIndexes'][str(n)]]
        value = p.get_text()
        assert value.startswith('Prompt: ')
        return value[len('Prompt: '):]
    return heading.get_text()


def labels_for(config, n):
    return config.get('sectionModelLabels', {}).get(str(n), config['modelLabels'])


def tag(soup, name, value=None, **attrs):
    node = soup.new_tag(name, attrs=attrs)
    if value is not None:
        node.string = value
    return node


def readable_math(original, config):
    """Explicitly transcribe legacy equation images without changing block order."""
    col = copy.deepcopy(original)
    mapping = config.get('mathImageText', {})
    if mapping:
        for image in col.select('img.latex'):
            alt = image.get('alt', '')
            assert alt in mapping, ('Unreviewed formula', alt)
            span = BeautifulSoup('<span class="source-math"></span>', 'html.parser').span
            span.string = mapping[alt]
            image.replace_with(span)
    return col


def edited_column(original, n, c, config):
    col = readable_math(original, config)
    if config.get('removeDecorativeImages'):
        for figure in col.select('figure:has(img)'):
            assert not figure.get_text(strip=True)
            figure.decompose()
        for blank in col.find_all(string=lambda value: not value.strip()):
            blank.extract()
    for el in [col, *col.find_all(True)]:
        el.attrs = {k: v for k, v in el.attrs.items()
                    if k in ('href', 'colspan', 'rowspan', 'start')}
    col['class'] = ['original-response']
    col['data-source-column'] = str(c)
    for i, (old_image, new_image) in enumerate(zip(original.find_all('img'), col.find_all('img'))):
        key = f'{n}.{c}.img{i}'
        if key in config.get('sourceImageDescriptions', {}):
            new_image['src'] = old_image['src']
            new_image['alt'] = config['sourceImageDescriptions'][key]
            new_image['style'] = 'max-width:100%;height:auto'
    nodes = col.find_all(TAGS)
    for k, node in enumerate(nodes):
        node['data-source-node'] = f'{n}.{c}.{k}'
    for k, node in enumerate(nodes):
        key = f'{n}.{c}.{k}'
        if key in config.get('leadingTextReplacements', {}):
            # A question can contain a nested list of options. Edit only its
            # leading text, preserving every original option and its address.
            children = list(node.contents)
            boundary = next(i for i, child in enumerate(children)
                            if getattr(child, 'name', None) in ('ul', 'ol'))
            assert all(not getattr(child, 'find_all', lambda *a: [])(TAGS)
                       for child in children[:boundary])
            for child in children[:boundary]:
                child.extract()
            node.insert(0, config['leadingTextReplacements'][key] + '\n')
        if key in config['replacements']:
            assert not node.find_all(TAGS), ('Replacement would remove source descendants', key)
            node.clear()
            for child in list(BeautifulSoup(config['replacements'][key], 'html.parser').contents):
                node.append(child)
    for i, answer in enumerate(col.find_all('details')):
        key = f'{n}.{c}.answer{i}'
        if key in config.get('bareAnswerReplacements', {}):
            assert not answer.find_all(TAGS)
            assert not any(parent.name in TAGS for parent in answer.parents)
            summary = answer.summary.extract()
            answer.clear()
            answer.append(summary)
            answer.append(config['bareAnswerReplacements'][key])
    cell_edits = config.get('tableCellReplacements', {})
    for t, table in enumerate(col.find_all('table')):
        for r, row in enumerate(table.find_all('tr')):
            for cell_index, cell in enumerate(row.find_all(['th', 'td'], recursive=False)):
                key = f'{n}.{c}.table{t}.{r}.{cell_index}'
                if key in cell_edits:
                    assert not cell.find_all(TAGS)
                    cell.clear()
                    for child in list(BeautifulSoup(cell_edits[key], 'html.parser').contents):
                        cell.append(child)
    for key, value in config.get('listItemContinuations', {}).items():
        if key.startswith(f'{n}.{c}.'):
            node = col.select_one(f'[data-source-node="{key}"]')
            assert node is not None and node.name == 'li'
            addition = BeautifulSoup('<li></li>', 'html.parser').li
            addition['data-source-addition'] = key
            for child in list(BeautifulSoup(value, 'html.parser').contents):
                addition.append(child)
            node.insert_after(addition)
    for value in config.get('responseAppendices', {}).get(f'{n}.{c}', []):
        for child in list(BeautifulSoup(value, 'html.parser').contents):
            col.append(child)
    if config.get('disclosureParagraphsAsDiv'):
        for p in col.select('p:has(> details)'):
            p.name = 'div'
    for h in col.find_all('h4'):
        h.name = 'h5'
    for h in col.find_all('h3'):
        h.name = 'h4'
    starts = config.get('orderedListStarts', {}).get(f'{n}.{c}')
    if starts is not None:
        lists = col.find_all('ol')
        assert len(lists) == len(starts)
        for ol, start in zip(lists, starts):
            ol['start'] = str(start)
    for index in config.get('manuallyNumberedLists', {}).get(f'{n}.{c}', []):
        ol = col.find_all('ol')[index]
        for number, li in enumerate(ol.find_all('li', recursive=False), 1):
            assert text(li).startswith(f'{number}. ')
        ol['style'] = 'list-style:none;padding-left:0'
    for group in config.get('joinedParagraphs', {}).get(f'{n}.{c}', []):
        # Keep each source address while honoring a prompt for one paragraph.
        paragraphs = [col.select_one(f'[data-source-node="{n}.{c}.{k}"]') for k in group]
        assert len(paragraphs) > 1 and all(p is not None and p.name == 'p' for p in paragraphs)
        assert all(p.parent is col and not p.find_all(TAGS) for p in paragraphs)
        assert list(paragraphs[0].find_next_siblings('p', limit=len(group)-1)) == paragraphs[1:]
        for paragraph in paragraphs[1:]:
            gap = paragraph.previous_sibling
            if isinstance(gap, str) and not gap.strip():
                gap.extract()
            paragraph.name = 'span'
            paragraphs[0].append(' ')
            paragraphs[0].append(paragraph.extract())
    return col


def render(config):
    source = BeautifulSoup((DATA / config['snapshot']).read_text(), 'html.parser')
    original = sections(source, config)
    assert len(original) == len(config['headings'])
    assert all(len(cols) == len(labels_for(config, n))
               for n, (_, cols) in enumerate(original, 1))
    appendices = config.get('sourceAppendices', [])
    all_headings = source.select('h2')
    assert len(original) + len(appendices) + len(config.get('pairedResponseHeadingIndexes', {})) == len(all_headings)
    for appendix in appendices:
        assert all_headings[appendix['headingIndex']].get_text() == appendix['heading']
    shell = subprocess.check_output(['git', 'show', f"{config['shellRevision']}:{config['pageFile']}"], cwd=ROOT, text=True)
    soup = BeautifulSoup(shell, 'html.parser')
    for node in soup.find_all(string=lambda n: isinstance(n, Comment)):
        if 'AUTO-GENERATED BY scripts/build_archive.py' in node:
            node.replace_with(Comment(f" EDITORIALLY MAINTAINED: original-preserving cycle 8; WordPress post {config['wordpressId']} "))
    body = soup.select_one('.article-body')
    # Navigation is site chrome, never a source for responses.
    route = body.select_one('#reader-route').extract()
    future = body.select_one('#future-branches').extract()
    body.clear()
    intro = tag(soup, 'section', **{'class': 'article-section', 'id': 'source-texture'})
    intro.append(tag(soup, 'h2', config['introHeading']))
    intro.append(tag(soup, 'p', config['intro']))
    p = tag(soup, 'p')
    p.append(tag(soup, 'a', config['sourceLabel'], href=config['sourceUrl']))
    intro.append(p)
    if config.get('highlights'):
        intro.append(tag(soup, 'h3', 'Highlights · edited summary'))
        highlights = tag(soup, 'ul', **{'class': 'source-highlights'})
        for value in config['highlights']:
            highlights.append(tag(soup, 'li', value))
        intro.append(highlights)
    body.append(intro)
    body.append(route)
    ledger = soup.select_one('.prompt-ledger ol')
    ledger.clear()
    for n, (heading, cols) in enumerate(original, 1):
        prompt = original_prompt(heading, config, n)
        li = tag(soup, 'li')
        a = tag(soup, 'a', **{'class': 'prompt-ledger__link', 'href': f'#prompt-{n}'})
        a.append(tag(soup, 'span', str(n), **{'class': 'prompt-number', 'aria-hidden': 'true'}))
        a.append(tag(soup, 'span', prompt, **{'class': 'prompt-ledger__text'}))
        li.append(a)
        ledger.append(li)
        section = tag(soup, 'section', **{'class': 'article-section article-section--prompt', 'id': f'prompt-{n}'})
        meta = tag(soup, 'div', **{'class': 'article-section__meta'})
        meta.append(tag(soup, 'span', str(n), **{'class': 'prompt-number article-section__number', 'aria-hidden': 'true'}))
        is_heading = n in config.get('nonPromptSections', [])
        meta.append(tag(soup, 'span', 'Original response heading' if is_heading else 'Original prompt · edited responses'))
        section.append(meta)
        p = tag(soup, 'p', **{'class': 'article-section__prompt'})
        p.append(tag(soup, 'span', 'Response heading:' if is_heading else f'Prompt {n}:'))
        p.append(' ')
        p.append(tag(soup, 'span', prompt, **{'class': 'original-prompt-text'}))
        section.append(p)
        section.append(tag(soup, 'h2', config['headings'][n-1]))
        for k, original_preamble in enumerate(preamble_nodes(heading, config, n)):
            if k == config.get('promptContinuationPreambleIndexes', {}).get(str(n)):
                continue
            preamble = copy.deepcopy(original_preamble)
            image_origin = config.get('preambleImageOrigins', {}).get(f'{n}.{k}')
            kept_attributes = ('href', 'src', 'alt', 'width', 'height') if image_origin else ('href',)
            for el in [preamble, *preamble.find_all(True)]:
                el.attrs = {key: value for key, value in el.attrs.items() if key in kept_attributes}
            if image_origin:
                assert original_preamble.img[image_origin['sourceAttribute']] == image_origin['url']
                preamble.img['src'] = image_origin['url']
                preamble.img['alt'] = image_origin['alt']
                preamble.img['style'] = 'max-width:189px;height:auto'
            preamble['data-source-preamble'] = f'{n}.{k}'
            section.append(preamble)
        for c, col in enumerate(cols, 1):
            edited = edited_column(col, n, c, config)
            dialogue = config.get('dialogues', {}).get(f'{n}.{c}')
            if dialogue:
                turns = [edited.select_one(f'[data-source-node="{n}.{c}.{k}"]')
                         for k in dialogue['sourceTurnNodes']]
                lines = tag(soup, 'ol', **{'class': 'source-dialogue'})
                for turn in turns:
                    li = tag(soup, 'li')
                    li.append(turn.extract())
                    lines.append(li)
                for value in dialogue.get('continuation', []):
                    li = tag(soup, 'li')
                    li.append(tag(soup, 'p', value))
                    lines.append(li)
                edited.append(lines)
            label = labels_for(config, n)[c-1]
            display = config.get('sectionResponseLabels', {}).get(f'{n}.{c}', label + ' response · editorial edition')
            edited.insert(0, tag(soup, 'h3', display))
            section.append(edited)
        body.append(section)
    bonus = config.get('sourceBonusExchange')
    if bonus:
        heading = source.find(id=bonus['sourceHeadingId'])
        assert heading is not None and heading.name == 'h4'
        assert heading.get_text() == bonus['prompt']
        figure = heading.find_next_sibling()
        comment = figure.find_next_sibling()
        assert figure.name == 'figure' and comment.name == 'p'
        assert comment.get_text() == bonus['curatorComment']
        n = len(original) + 1
        li = tag(soup, 'li')
        a = tag(soup, 'a', **{'class': 'prompt-ledger__link', 'href': f'#prompt-{n}'})
        a.append(tag(soup, 'span', str(n), **{'class': 'prompt-number', 'aria-hidden': 'true'}))
        a.append(tag(soup, 'span', heading.get_text(), **{'class': 'prompt-ledger__text'}))
        li.append(a)
        ledger.append(li)
        section = tag(soup, 'section', **{'class': 'article-section article-section--prompt', 'id': f'prompt-{n}'})
        p = tag(soup, 'p', **{'class': 'article-section__prompt'})
        p.append(tag(soup, 'span', f'Prompt {n}:'))
        p.append(' ')
        p.append(tag(soup, 'span', heading.get_text(), **{'class': 'original-prompt-text'}))
        section.append(p)
        section.append(tag(soup, 'h2', 'Original image response and curator comment'))
        image = copy.deepcopy(figure)
        for el in [image, *image.find_all(True)]:
            el.attrs = {k: v for k, v in el.attrs.items() if k in ('src', 'srcset', 'sizes', 'width', 'height', 'alt', 'loading')}
        image.img['alt'] = bonus['alt']
        if bonus.get('useSourceImageOrigin'):
            # WordPress records its working media origin beside the expired custom-domain URL.
            image.img['src'] = figure.img['data-large-file']
            image.img.attrs.pop('srcset', None)
        image.img['style'] = 'max-width:100%;height:auto'
        image.append(tag(soup, 'figcaption', 'Original 2024 image response; retained as part of the conversation.'))
        section.append(image)
        section.append(tag(soup, 'p', comment.get_text(), **{'class': 'curator-comment'}))
        body.append(section)
    for appendix in appendices:
        section = tag(soup, 'section', **{'class': 'article-section', 'id': appendix['id']})
        section.append(tag(soup, 'h2', appendix['heading']))
        figure = copy.deepcopy(all_headings[appendix['headingIndex']].find_next_sibling())
        assert figure.name == 'figure'
        for el in [figure, *figure.find_all(True)]:
            el.attrs = {k: v for k, v in el.attrs.items()
                        if k in ('src', 'srcset', 'sizes', 'width', 'height', 'alt', 'loading')}
        figure.img['alt'] = appendix['alt']
        figure.img['style'] = 'max-width:100%;height:auto'
        figure.append(tag(soup, 'figcaption', appendix['caption']))
        section.append(figure)
        body.append(section)
    body.append(future)
    for label, value in config.get('pageSignals', {}).items():
        matches = [item for item in soup.select('.page-signals__item')
                   if text(item.select_one('.page-signals__label')) == label]
        assert len(matches) == 1, label
        matches[0].select_one('.page-signals__value').string = value
    description = config['description']
    soup.select_one('.article-standfirst').string = description
    for name in ['description', 'og:description', 'twitter:description']:
        node = soup.find('meta', attrs={'name': name}) or soup.find('meta', attrs={'property': name})
        if node:
            node['content'] = description
    for node in soup.select('meta[property="article:modified_time"]'):
        node['content'] = config['date']
    for node in soup.select('script[type="application/ld+json"]'):
        data = json.loads(node.string or '{}')
        if data.get('@type') == 'Article':
            data.update(dateModified=config['date'], description=description)
            node.string = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    return '\n'.join(line.rstrip() for line in str(soup).splitlines()) + '\n'


def verify(config, rendered):
    raw = (DATA / config['snapshot']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == config['sourceSha256']
    original = sections(BeautifulSoup(raw, 'html.parser'), config)
    soup = BeautifulSoup(rendered, 'html.parser')
    if config.get('highlights'):
        assert [x.get_text() for x in soup.select('.source-highlights > li')] == config['highlights']
    prompts = [original_prompt(h, config, n) for n, (h, _) in enumerate(original, 1)]
    bonus = config.get('sourceBonusExchange')
    if bonus:
        source = BeautifulSoup(raw, 'html.parser')
        heading = source.find(id=bonus['sourceHeadingId'])
        assert heading.get_text() == bonus['prompt']
        prompts.append(heading.get_text())
        actual = soup.select_one(f'#prompt-{len(prompts)}')
        figure = heading.find_next_sibling()
        expected_src = figure.img['data-large-file'] if bonus.get('useSourceImageOrigin') else figure.img['src']
        assert actual.img['src'] == expected_src
        if bonus.get('useSourceImageOrigin'):
            assert not actual.img.has_attr('srcset')
        assert actual.select_one('.curator-comment').get_text() == figure.find_next_sibling().get_text() == bonus['curatorComment']
        assert [s['id'] for s in soup.select('.article-section--prompt')] == [f'prompt-{n}' for n in range(1, len(prompts) + 1)]
    for n, (h, _) in enumerate(original, 1):
        old_preambles = [p for k, p in enumerate(preamble_nodes(h, config, n))
                         if k != config.get('promptContinuationPreambleIndexes', {}).get(str(n))]
        new_preambles = soup.select(f'#prompt-{n} [data-source-preamble]')
        assert [x.get_text() for x in old_preambles] == [x.get_text() for x in new_preambles]
        assert [a.get('href') for p in old_preambles for a in p.find_all('a')] == [a.get('href') for p in new_preambles for a in p.find_all('a')]
        for p in new_preambles:
            image_origin = config.get('preambleImageOrigins', {}).get(p['data-source-preamble'])
            if image_origin:
                assert p.img is not None, 'Original preamble illustration missing'
                assert p.img['src'] == image_origin['url'] and p.img['alt'] == image_origin['alt']
    assert prompts == [n.get_text() for n in soup.select('.original-prompt-text')]
    assert prompts == [n.get_text() for n in soup.select('.prompt-ledger__text')]
    used = set()
    retained = changed = 0
    for n, (_, cols) in enumerate(original, 1):
        for c, col in enumerate(cols, 1):
            expected = edited_column(col, n, c, config)
            actual = soup.select_one(f'#prompt-{n} .original-response[data-source-column="{c}"]')
            actual_nodes = actual.select('[data-source-node]')
            expected_nodes = expected.select('[data-source-node]')
            assert [x['data-source-node'] for x in actual_nodes] == [x['data-source-node'] for x in expected_nodes]
            for old, want, got in zip(readable_math(col, config).find_all(TAGS), expected_nodes, actual_nodes):
                key = got['data-source-node']
                assert str(got) == str(want), key
                if key in config['replacements'] or key in config.get('leadingTextReplacements', {}):
                    used.add(key)
                    changed += 1
                else:
                    assert own_text(old) == own_text(got), key
                    retained += 1
            assert [(x.name, len(x.find_all('li', recursive=False))) for x in expected.find_all(['ol', 'ul'])] == [(x.name, len(x.find_all('li', recursive=False))) for x in actual.find_all(['ol', 'ul']) if 'source-dialogue' not in x.get('class', [])]
            assert len(col.find_all('table')) == len(actual.find_all('table'))
            for t, (old_table, new_table) in enumerate(zip(col.find_all('table'), actual.find_all('table'))):
                assert len(old_table.find_all('tr')) == len(new_table.find_all('tr'))
                for r, (old_row, new_row) in enumerate(zip(old_table.find_all('tr'), new_table.find_all('tr'))):
                    old_cells = old_row.find_all(['th', 'td'], recursive=False)
                    new_cells = new_row.find_all(['th', 'td'], recursive=False)
                    assert len(old_cells) == len(new_cells)
                    for i, (old_cell, new_cell) in enumerate(zip(old_cells, new_cells)):
                        key = f'{n}.{c}.table{t}.{r}.{i}'
                        if key in config.get('tableCellReplacements', {}):
                            used.add(key)
                        else:
                            assert text(old_cell) == text(new_cell), key
            assert [ol.get('start', '1') for ol in expected.find_all('ol')] == [
                ol.get('start', '1') for ol in actual.find_all('ol')
                if 'source-dialogue' not in ol.get('class', [])]
            for i, (old_answer, new_answer) in enumerate(zip(col.find_all('details'), actual.find_all('details'))):
                key = f'{n}.{c}.answer{i}'
                if key in config.get('bareAnswerReplacements', {}):
                    assert new_answer.summary.get_text() == old_answer.summary.get_text()
                    assert new_answer.get_text() == old_answer.summary.get_text() + config['bareAnswerReplacements'][key]
                    used.add(key)
            dialogue = config.get('dialogues', {}).get(f'{n}.{c}')
            if dialogue:
                lines = actual.select_one('.source-dialogue').find_all('li', recursive=False)
                source_count = len(dialogue['sourceTurnNodes'])
                assert [line.select_one('[data-source-node]')['data-source-node']
                        for line in lines[:source_count]] == [
                            f'{n}.{c}.{k}' for k in dialogue['sourceTurnNodes']]
                assert [text(line) for line in lines[source_count:]] == dialogue.get('continuation', [])
            else:
                # Also check explicitly added material, such as a missing key
                # or a split list item; source-node checks alone cannot do so.
                clone = copy.deepcopy(actual)
                clone.find('h3', recursive=False).decompose()
                assert str(clone) == str(expected), (n, c, 'complete response mismatch')
    edits = set(config['replacements']) | set(config.get('leadingTextReplacements', {})) | set(config.get('tableCellReplacements', {})) | set(config.get('bareAnswerReplacements', {}))
    assert used == edits, ('Unused edits', edits - used)
    if config.get('mathImageText'):
        assert {im.get('alt', '') for _, cols in original for col in cols for im in col.select('img.latex')} == set(config['mathImageText'])
    image_keys = set()
    for n, (_, cols) in enumerate(original, 1):
        for c, col in enumerate(cols, 1):
            actual = soup.select_one(f'#prompt-{n} .original-response[data-source-column="{c}"]')
            for i, old_image in enumerate(col.find_all('img')):
                key = f'{n}.{c}.img{i}'
                if key in config.get('sourceImageDescriptions', {}):
                    new_image = actual.find_all('img')[i]
                    assert new_image['src'] == old_image['src']
                    assert new_image['alt'] == config['sourceImageDescriptions'][key]
                    image_keys.add(key)
    assert image_keys == set(config.get('sourceImageDescriptions', {}))
    for appendix in config.get('sourceAppendices', []):
        old = BeautifulSoup(raw, 'html.parser').select('h2')[appendix['headingIndex']].find_next_sibling()
        new = soup.select_one('#' + appendix['id'])
        assert new.h2.get_text() == appendix['heading']
        assert new.img['src'] == old.img['src']
    checks = {}
    for check in config['countChecks']:
        observed = [len(node.find_all(check['child'], recursive=check.get('recursive', False))) for node in soup.select(check['selector'])]
        assert observed == check['expected'], (check, observed)
        checks[check['name']] = observed
    ids = [x['id'] for x in soup.select('[id]')]
    assert all(count == 1 for count in Counter(ids).values())
    for a in soup.select('a[href^="#"]'):
        assert soup.find(id=a['href'][1:]), a['href']
    assert 'EDITORIALLY MAINTAINED:' in rendered
    assert 'AUTO-GENERATED BY scripts/build_archive.py' not in rendered
    for label, value in config.get('pageSignals', {}).items():
        items = [item for item in soup.select('.page-signals__item')
                 if text(item.select_one('.page-signals__label')) == label]
        assert len(items) == 1 and text(items[0].select_one('.page-signals__value')) == value
    return {'pagePath': '/' + config['pageFile'].removesuffix('index.html'),
            'sourceSha256': config['sourceSha256'], 'originalPrompts': len(prompts) - len(config.get('nonPromptSections', [])),
            'originalHeadings': len(prompts),
            'sourceColumns': sum(len(cols) for _, cols in original),
            'modelResponses': sum(len(cols) for _, cols in original) - len(config.get('nonResponseColumns', [])), 'blocksRetainedVerbatim': retained,
            'tableCellsExplicitlyRevised': len(config.get('tableCellReplacements', {})),
            'blocksExplicitlyRevised': changed, 'bareAnswersExplicitlyRevised': len(config.get('bareAnswerReplacements', {})), 'promptOrderExact': True,
            'sourceBlockOrderExact': True,
            'listAndTableStructuresPreserved': not bool(config.get('listItemContinuations') or config.get('responseAppendices')),
            'explicitListItemSplits': list(config.get('listItemContinuations', {})),
            'explicitResponseAppendices': list(config.get('responseAppendices', {})),
            'formatChecks': checks, 'sha256': hashlib.sha256(rendered.encode()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('slug')
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    config = json.loads((DATA / f'{args.slug}-edits.json').read_text())
    rendered = render(config)
    result = verify(config, rendered)
    if args.write:
        tracker = json.loads((ROOT / 'quality/editorial-audit-tracker.json').read_text())
        assert result['pagePath'] in [p['pagePath'] for p in tracker['currentBatch']['pages']]
        (ROOT / config['pageFile']).write_text(rendered)
    else:
        assert (ROOT / config['pageFile']).read_text() == rendered
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
