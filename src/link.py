#!/usr/bin/python3

import argparse
import json
from utils import clipboard

parser = argparse.ArgumentParser()
parser.add_argument('--prefix', help='Set prefix')
parser.add_argument('--text', help='Set text')
args = parser.parse_args()

text = args.text
prefix = args.prefix if args.prefix else ''


def item(clip):
    content = f"{prefix}[{text}]({clip})".replace('\n', '')
    return {
        'title': content,
        'subtitle': f"Paste {content}",
        'arg': content
    }


items = list(map(item, clipboard))

print(json.dumps({'items': items}))
