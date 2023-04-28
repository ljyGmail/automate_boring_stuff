import csv

# reader Objects
exampleFile = open('data/ch16/example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

print(f'exampleData: {exampleData}')

print(f'exampleData[0][0]: {exampleData[0][0]}')
print(f'exampleData[0][1]: {exampleData[0][1]}')
print(f'exampleData[0][2]: {exampleData[0][2]}')
print(f'exampleData[1][1]: {exampleData[1][1]}')
print(f'exampleData[6][1]: {exampleData[6][1]}')

# Reading Data from reader Objects in a for Loop
exampleFile = open('data/ch16/example.csv')
exampleReader = csv.reader(exampleFile)

print('-=' * 20)
for row in exampleReader:
    print(f'Row #{exampleReader.line_num} {row}')

# DictReader CSV Objects
exampleFile = open('data/ch16/exampleWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile)

print('-=' * 20)
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])


exampleFile = open('data/ch16/example.csv')

# supply the DictReader() with a second argument containing made-up header names
exampleDictReader = csv.DictReader(exampleFile, ['time', 'name', 'amount'])

print('-=' * 20)
for row in exampleDictReader:
    print(row['time'], row['name'], row['amount'])
