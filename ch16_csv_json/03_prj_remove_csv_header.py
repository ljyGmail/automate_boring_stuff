import csv
import os

src_folder = 'data/ch16/headerToBeRemoved'
result_folder = 'data/ch16/headerRemoved'
os.makedirs(result_folder, exist_ok=True)

# Loop through every file in the source directory.
for csvFilename in os.listdir('data/ch16/headerToBeRemoved'):
    if not csvFilename.endswith('.csv'):
        continue  # skip non-csv files

    print(f'Removing header from {csvFilename}...')

    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open(os.path.join(src_folder, csvFilename))
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue  # skip first row
        csvRows.append(row)
    csvFileObj.close()

    # Write out the CSV file.
    csvFileObj = open(os.path.join(
        result_folder, csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
