#!/usr/bin/env python3

import argparse
from csv import reader
import random

# ########## #
# ARG PARSER #
# ########## #
parser = argparse.ArgumentParser(description='Randomize which exercises to do')
parser.add_argument('-s', '--sets', help='Determine how many sets you want to do",dest="sets', dest='sets',metavar='', default='1')
parser.add_argument('-c', '--count', help='Determine how many exercises per set you want to do',dest='count', metavar='', default='5')
parser.add_argument('-p', '--path', help='Path to csv file, defaults to the template',dest='path', metavar='', default='template.csv')

args = parser.parse_args()

sets = int(args.sets)
count = int(args.count)

# read csv file as a list of lists
exercises = []
with open(args.path, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    exercises = list(csv_reader)

# remove header
exercises.pop(0)

text_set = 'sets' if sets > 1 else 'set'

print()
print('-----------------------------------------------------------')
print('You are doing {} {} of these exercises:'.format(sets, text_set))
print()
random.shuffle(exercises)
for c in range(count):
    exercise = exercises.pop()
    text_rep = 'reps' if int(exercise[2]) > 1 else 'rep'
    print('  {}: {} @ {} x {} {}'.format(c + 1, exercise[0], exercise[1], exercise[2], text_rep))

print('-----------------------------------------------------------')
print()