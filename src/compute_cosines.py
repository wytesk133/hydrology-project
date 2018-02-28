#!/usr/bin/env python
from argparse import ArgumentParser
from math import pi, cos

# Parse arguments

parser = ArgumentParser(prog='compute_cosines',
                        description='Reads input csv file, computes cosine values, and writes output csv file')
parser.add_argument('input', help='Path to input CSV file')
parser.add_argument('output', help='Path to output CSV file')
args = parser.parse_args()

# Reads input csv file, computes cosine values, and writes output csv file
# Assuming the format of the CSV file is:
#   station_id, angle_degrees

with open(args.input) as infile, open(args.output, mode='w') as outfile:
    # Assuming the first line is the header
    header = infile.readline().strip()
    outfile.write(header)
    outfile.write(',angle_cosine\n')

    # Read, compute, and write without storing the entire file in memory
    for line in infile:
        id, angle_deg = line.strip().split(',')
        angle_rad = float(angle_deg) * pi / 180
        outfile.write('{},{},{:.3f}\n'.format(id, angle_deg, cos(angle_rad)))
