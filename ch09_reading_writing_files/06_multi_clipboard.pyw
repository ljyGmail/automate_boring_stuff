import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

print(sys.argv)

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    else:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
