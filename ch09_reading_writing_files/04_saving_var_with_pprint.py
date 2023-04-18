import myCats
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'},
        {'name': 'Pooka', 'desc': 'fluffy'}]
print(f'pprint.pformat(cats): {pprint.pformat(cats)}')

fileObj = open('ch09_reading_writing_files/myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

print(f'myCats.cats: {myCats.cats}')
print(f'myCats.cats[0]: {myCats.cats[0]}')
print(f"myCats.cats[0]['name']: {myCats.cats[0]['name']}")
