import csv

# Tries to open a new file for printing and puts the column header in
def ready_printing(curr):
    with open('output' + str(curr or '') + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, dialect='excel-tab')
        writer.writerow(gen_header())

# Outputs the data into the output file.
def print_row(curr, data):
    with open('output' + str(curr or '') + '.csv', 'a', newline='') as file:
        writer = csv.writer(file, dialect='excel-tab')
        writer.writerow(data.values())

# Header generator.
def gen_header():
    header = []
    header.append('Name of Issuer')
    header.append('Title of Class')
    header.append('CUSIP')
    header.append('Value(x$1000)')
    header.append('SH/PRN Amount')
    header.append('SH/PRN')
    header.append('PUT/CALL')
    header.append('Investment Discretion')
    header.append('Other Manager')
    header.append('Sole Voting Authority')
    header.append('Shared Voting Authority')
    header.append('None Voting Authority')
    return header
