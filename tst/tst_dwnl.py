#!/usr/bin/env python
from argparse import ArgumentParser
from os.path import basename
from shutil import copyfileobj
from urllib.request import urlopen

# Parse arguments

parser = ArgumentParser(prog='download',
                        description='Download file from the given URL to current working directory')
parser.add_argument('url', help='Download URL')
parser.add_argument('output', nargs='?', default='', help='Output file name')
args = parser.parse_args()

if args.output == '':
    args.output = basename(args.url)

with urlopen(args.url) as response, open(args.output, 'wb') as output:
    copyfileobj(response, output)
