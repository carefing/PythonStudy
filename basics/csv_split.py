"""
The source file is a csv file with one line of header and 2000 lines of codes.
Will use this csv_split.py to split source file to 10 destination files.
A destination file is a csv file with one line of header and 200 lines of codes.
"""

import csv

filename = 'test_file/code_2000.csv'

license_hundreds = []
with open(filename) as f:
    reader = csv.reader(f)
    num = 0
    licenses = []
    for row in reader:
        num += 1
        if (num == 1):
            continue
        licenses.append(row)
        if ((num - 1) % 200 == 0):
            license_hundreds.append(licenses[:])
            licenses.clear()

for hundred in range(10):
    file = 'test_file/code_' + str(hundred) + '.csv'
    with open(file, 'w', newline='') as fo:
        writer = csv.writer(fo)
        writer.writerow(['code'])
        for license in license_hundreds[hundred]:
            writer.writerow(license)
