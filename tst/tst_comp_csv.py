#!/usr/bin/env python
from argparse import ArgumentParser
import sys

# Parse arguments

parser = ArgumentParser(prog='compare_csv',
                        description='Compares two CSV files and returns the result as exit code')
parser.add_argument('expected', help='Path to expected output')
parser.add_argument('actual', help='Path to actual output')
args = parser.parse_args()

def csv_row_matches(x:str, y:str)->bool:
    return x.strip().split(',') == y.strip().split(',')

with open(args.expected) as expected, open(args.actual) as actual:
    for expected_line in expected:
        if not csv_row_matches(expected_line, actual.readline()):
            sys.exit(1)
    # Fails if actual output is longer than expecteed output
    if actual.readline() != '':
        sys.exit(1)

sys.exit(0)
