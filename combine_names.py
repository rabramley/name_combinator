#!/usr/bin/env python3
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("language", help="language of the names")
parser.add_argument("--sex", "-s", choices=['female', 'male'], help="sex of names")
parser.add_argument("--count", "-c", type=int, default=100, help="number of names to create")

args = parser.parse_args()

print(f'Creating {args.count} {args.sex} names for {args.language}')

with open(f'data/{args.language}_{args.sex}_last.csv') as f:
    first_parts = f.read().splitlines()

with open(f'data/{args.language}_{args.sex}_last.csv') as f:
    last_parts = f.read().splitlines()

names = set()

for _ in range(args.count):
    firstpart = random.choice(first_parts)
    lastpart = random.choice(last_parts)
    names.add(f'{firstpart}{lastpart}'.capitalize())

print(', '.join(names))