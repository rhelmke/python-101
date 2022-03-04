# generally just google python 3 <what i want to do>, works mostly
# specifically look at https://docs.python.org/3/library/functions.html

import os
import sys

fd = open(sys.argv[1], 'r')  # TODO use pathlib here, TODO use argparse for sys.argv
data = fd.read()
fd.close()

csv_data = dict()

counter = 0  # TODO find built-in to not have to count
for line in data.splitlines(keepends=False):
    values = line.split(',')
    for value in values:  # TODO I can do this in one line, don't I (list comprehension)
        values[values.index(value)] = value.strip()
    csv_data[counter] = values
    counter += 1

if not csv_data:  # TODO Earlier point might need exit too ...
    print('Empty file')
    sys.exit(1)


header = csv_data.pop(0)
format_string = '{}\t'  # TODO Again, maybe one liner?? (str.join, list comprehension)
for header_name in header:
    format_string += '{}: {{}}\t\t'.format(header_name)

for line_number, values in csv_data.items():
    print(format_string.format(line_number, *values))

