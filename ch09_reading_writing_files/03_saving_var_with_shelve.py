import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(f'type: {type(shelfFile)}')
print(f"shelfFile['cats']: {shelfFile['cats']}")
shelfFile.close()

shelfFile = shelve.open('mydata')
print(f'list(shelfFile.keys()): {list(shelfFile.keys())}')
print(f'list(shelfFile.values()): {list(shelfFile.values())}')
shelfFile.close()
