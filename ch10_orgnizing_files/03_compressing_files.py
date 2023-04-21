# Reading ZIP Files
import zipfile
import os
from pathlib import Path

p = Path('data/ch10/')

exampleZip = zipfile.ZipFile(p / 'example.zip')
print(f'exampleZip.namelist(): {exampleZip.namelist()}')

spamInfo = exampleZip.getinfo('spam.txt')
print(f'spamInfo.file_size: {spamInfo.file_size}')
print(f'spamInfo.compress_size: {spamInfo.compress_size}')
print(
    f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')

exampleZip.close()

# Extracting from ZIP Files
exampleZip = zipfile.ZipFile(p / 'example.zip')
# exampleZip.extractall('../demo')
# exampleZip.extract('spam.txt')
# print(
#     f"exampleZip.extract('spam.txt', '../demo'): {exampleZip.extract('spam.txt', '../demo')}")
exampleZip.close()

# Creating and Adding to ZIP Files
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('data/ch10/source/spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
