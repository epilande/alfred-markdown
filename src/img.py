#!/usr/bin/python3

import json
from utils import query, clipboard


def item(clip):
    content = f"![{query}]({clip})".replace('\n', '')
    return {
        'title': content,
        'subtitle': f"Paste {content}",
        'arg': content
    }


items = list(map(item, clipboard))

print(json.dumps({'items': items}))
