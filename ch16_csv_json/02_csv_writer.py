import csv

# writer Objects
outputFile = open('data/ch16/output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

print(
    f"outputWriter.writerow(['spam','eggs','bacon','ham']): {outputWriter.writerow(['spam','eggs','bacon','ham'])}")
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])

outputFile.close()

# The delimiter and lineterminator Keyword Arguments
csvFile = open('data/ch16/example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')

csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])

csvFile.close()

# DictWriter CSV Objects
outputFile = open('data/ch16/dictwriter_output.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
outputDictWriter.writeheader()
print(
    f"outputDictWriter.writerow(['Name':'Alice','Pet':'cat','Phone':'555-1234']): {outputDictWriter.writerow({'Name':'Alice','Pet':'cat','Phone':'555-1234'})}")
outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})

outputFile.close()
