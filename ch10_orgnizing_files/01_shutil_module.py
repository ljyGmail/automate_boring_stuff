import send2trash
import shutil
import os
from pathlib import Path

# copy single file
p = Path('data/ch10')
print(
    f"shutil.copy(p / 'source/spam.txt', p / 'dest'): {shutil.copy(p / 'source/spam.txt', p / 'dest')}")
print(
    f"shutil.copy(p / 'source/spam.txt', p / 'dest/spam2.txt'): {shutil.copy(p / 'source/spam.txt', p / 'dest/spam2.txt')}")

# copy entire folder
# shutil.copytree(p / 'source/folder_tree', p / 'dest/folder_tree_backup')

# Moving and Renaming Files and Folders
# print(
#     f"shutil.move(p / 'source/spam.txt', p / 'dest/spam3.txt'): {shutil.move(p / 'source/spam.txt', p / 'dest/spam3.txt')}")
# shutil.move(p / 'source/spam.txt', p / 'does_not_exist/eggs/ham')

# Permanently Deleting Files and Folders
for filename in Path('data/ch10/source/delete_test').glob('*.txt'):
    print(filename)
    # os.unlink(filename)

baconFile = open('data/ch10/source/bacon.txt', 'a')  # create the file
baconFile.write('Bacon is not a vegetable')
baconFile.close()
send2trash.send2trash('data/ch10/source/bacon.txt')
