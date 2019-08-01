import csv
with open('1.csv', 'rb') as csvfile:
    students_reader = csv.reader(csvfile, delimiter='\t')
    for row in students_reader:
        print ', '.join(row)
