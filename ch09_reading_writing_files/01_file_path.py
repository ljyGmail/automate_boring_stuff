# Backslash on Windows and Forward Slash on macOS and Linux
import os
from pathlib import Path
import sys

CURRENT_OS = sys.platform

print(f'Path("spam", "bacon", "eggs"): {Path("spam", "bacon", "eggs")}')
print(
    f'str(Path("spam", "bacon", "eggs")): {str(Path("spam", "bacon", "eggs"))}')

myFiles = ['accounts.txt', 'details.csv', 'invie.docx']
for filename in myFiles:
    print(Path(r'c:\Users\Al', filename))

# Using the / Operator to Join Paths
print(f"Path('spam') / 'bacon' / 'eggs': {Path('spam') / 'bacon' / 'eggs'}")
print(f"Path('spam') / Path('bacon/eggs): {Path('spam') / Path('bacon/eggs')}")
print(
    f"Path('spam') / Path('bacon', 'eggs'): {Path('spam') / Path('bacon', 'eggs')}")

# Using the / operator with Path objects makes joining paths just as easy as string concatenation
homeFolder = r'c:\Users\Al'
subFolder = 'spam'
print('homeFolder + "\\\\" + subFolder: ' + (homeFolder + '\\' + subFolder))

print('"\\\\".join([homeFolder, subFolder]): ' +
      '\\'.join([homeFolder, subFolder]))

homeFolder = Path('C:/Users/Al')
subFolder = Path('spam')
print(f'homeFolder / subFolder: {homeFolder / subFolder}')
print(f'str(homeFolder / subFolder): {str(homeFolder / subFolder)}')

# 'spam' / 'bacon' / eggs # error, when using / operator for joining paths, one of the first two values must be a Path object

# The current Working Directory
print(f'Path.cwd(): {Path.cwd()}')
os.chdir('..')
print(f'Path.cwd() after going one level up: {Path.cwd()}')

os.chdir('automate_boring_stuff')

# os.chdir('ThisFolderDoesNotExist')
print(f'os.getcwd(): {os.getcwd()}')

# The Home Directory
print(f'Path.home(): {Path.home()}')

# Absolute vs. Relative Paths

# Creating New Folders Using the os.makedirs() Function
os.makedirs('delicious/walnut/waffles', exist_ok=True)

# mkdir() can only make one directory at a time
Path('spams').mkdir(exist_ok=True)

# Handling Absolute and Relative Paths
print(f'Path.cwd(): {Path.cwd()}')
print(f'Path.cwd().is_absolute(): {Path.cwd().is_absolute()}')
print(
    f"Path('spam/bacon/eggs').is_absolute(): {Path('spam/bacon/eggs').is_absolute()}")

print(f"Path('my/relative/path): {Path('my/relative/path')}")

# relative to the current working directory
print(
    f"Path.cwd() / Path('my/relative/path'): {Path.cwd() / Path('my/relative/path')}")

# relative to another path besides the current working directory
print(
    f"Path.home() / Path('my/relative/path'): {Path.home() / Path('my/relative/path')}")

# The os.path also has some useful functions related to absolute and relative paths
print(f"os.path.abspath('.'): {os.path.abspath('.')}")
print(f"os.path.abspath('./Scripts'): {os.path.abspath('./Scripts')}")
print(f"os.path.isabs('.'): {os.path.isabs('.')}")
print(
    f"os.path.isabs(os.path.abspath('.')): {os.path.isabs(os.path.abspath('.'))}")

print(f"os.path.relpath('a/b', 'a'): {os.path.relpath('a/b', 'a')}")
print(f"os.path.relpath('a', 'c/d'): {os.path.relpath('a', 'c/d')}")

# Getting the Parts of a File Path
if CURRENT_OS == 'win32':
    p = Path('C:/Users/Al/spam.txt')
    print(f'p.anchor: {p.anchor}')
    print(f'p.parent: {p.parent}')  # This is a Path object, not a string.
    print(f'p.name: {p.name}')
    print(f'p.stem: {p.stem}')
    print(f'p.suffix: {p.suffix}')
    print(f'p.drive: {p.drive}')
else:
    p = Path('/aaa/bbb/ccc/spam.txt')
    print(f'p.anchor: {p.anchor}')
    print(f'p.parent: {p.parent}')  # This is a Path object, not a string.
    print(f'p.name: {p.name}')
    print(f'p.stem: {p.stem}')
    print(f'p.suffix: {p.suffix}')

print(f'Path.cwd(): {Path.cwd()}')
print(f'Path.cwd().parents[0]: {Path.cwd().parents[0]}')
print(f'Path.cwd().parents[1]: {Path.cwd().parents[1]}')
print(f'Path.cwd().parents[2]: {Path.cwd().parents[2]}')
print(f'Path.cwd().parents[3]: {Path.cwd().parents[3]}')
print(f'Path.cwd().parents[4]: {Path.cwd().parents[4]}')

# The older os.path module also has similar functions for getting the different parts of a path written in a string value.
if CURRENT_OS == 'win32':
    calcFilePath = 'C:\\Windows\\System32\\calc.exe'
else:
    calcFilePath = '/aaa/bbb/ccc/calc.exe'
print(f'os.path.basename(calcFilePath): {os.path.basename(calcFilePath)}')
print(f'os.path.dirname(calcFilePath): {os.path.dirname(calcFilePath)}')

# get dir name and base name together
print(f'os.path.split(calcFilePath): {os.path.split(calcFilePath)}')

# create the same tuple as above
print(
    f'(os.path.dirname(calcFilePath), os.path.basename(calcFilePath)): {(os.path.dirname(calcFilePath), os.path.basename(calcFilePath))}')

print(f'calcFilePath.split(os.sep): {calcFilePath.split(os.sep)}')

# Finding File Sizes and Folder Contents
print(
    f"os.path.getsize('data/checkbox.png'): {os.path.getsize('data/checkbox.png')}")
