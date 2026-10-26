#!/usr/bin/env python3
"""Render the ethics glossary with its extra source term retained as a note.

The original ChatGPT glossary has 31 items despite a 30-item prompt. Keep the
first 30 numbered definitions and the final source node in its original order,
but present Stewardship as an explicitly labeled supplementary paragraph.
All other source rendering and verification use the established renderer.
"""
import argparse
import json
from bs4 import BeautifulSoup
import revise_source_conversations as common

_original_column = common.edited_column


def ethics_column(original, n, c, config):
    col = _original_column(original, n, c, config)
    if (n, c) == (1, 1):
        assert config['wordpressId'] == 3285
        assert config['supplementarySourceTerm'] == '1.1.30'
        node = col.select_one('[data-source-node="1.1.30"]')
        assert node.name == 'li' and node.parent.name == 'ol'
        numbered = node.parent
        assert len(numbered.find_all('li', recursive=False)) == 31
        assert numbered.find_all('li', recursive=False)[-1] is node
        node.extract()
        node.name = 'p'
        node['class'] = ['supplementary-source-term']
        numbered.insert_after(node)
        # Coalesce adjacent whitespace after extraction, as HTML parsing does.
        col = BeautifulSoup(str(col), 'html.parser').div
    return col


def verify(config, rendered):
    result = common.verify(config, rendered)
    soup = BeautifulSoup(rendered, 'html.parser')
    col = soup.select_one('#prompt-1 .original-response[data-source-column="1"]')
    assert len(col.ol.find_all('li', recursive=False)) == 30
    note = col.select_one('.supplementary-source-term')
    assert note is col.ol.find_next_sibling()
    assert note['data-source-node'] == '1.1.30'
    assert [n['data-source-node'] for n in col.select('[data-source-node]')] == [f'1.1.{k}' for k in range(31)]
    result['glossaryRequestedCounts'] = [30, 30]
    result['supplementarySourceTerm'] = {'sourceNode': '1.1.30', 'position': 'Immediately after the first glossary', 'reason': 'Retain original extra term without presenting 31 numbered items as 30.'}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    config = json.loads((common.DATA / 'ethics-core-concepts-edits.json').read_text())
    common.edited_column = ethics_column
    rendered = common.render(config)
    result = verify(config, rendered)
    if args.write:
        tracker = json.loads((common.ROOT / 'quality/editorial-audit-tracker.json').read_text())
        assert result['pagePath'] in [p['pagePath'] for p in tracker['currentBatch']['pages']]
        (common.ROOT / config['pageFile']).write_text(rendered)
    else:
        assert (common.ROOT / config['pageFile']).read_text() == rendered
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
