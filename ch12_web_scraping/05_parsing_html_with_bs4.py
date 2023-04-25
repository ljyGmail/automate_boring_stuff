import requests
import bs4

res = requests.get('https://nostarch.com')
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

print(f'type(noStarchSoup): {type(noStarchSoup)}')

exampleFile = open('data/ch12/example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
print(f'type(exampleFile): {type(exampleSoup)}')

# Finding an Element with the select() Method
elems = exampleSoup.select('#author')
print(f'type(elems): {type(elems)}')
print(f'len(elems): {len(elems)}')
print(f'type(elems[0]): {type(elems[0])}')
print(f'str(elems[0]): {str(elems[0])}')
print(f'elems[0].getText(): {elems[0].getText()}')
print(f'elems[0].attrs: {elems[0].attrs}')

pElems = exampleSoup.select('p')
print(f'str(pElems[0]): {str(pElems[0])}')
print(f'pElems[0].getText(): {pElems[0].getText()}')
print(f'str(pElems[1]): {str(pElems[1])}')
print(f'pElems[1].getText(): {pElems[1].getText()}')
print(f'str(pElems[2]): {str(pElems[2])}')
print(f'pElems[2].getText(): {pElems[2].getText()}')

# Getting Data from an Element's Attributes
spanElem = exampleSoup.select('span')[0]
print(f'str(spanElem): {str(spanElem)}')
print(f"spanElem.get('id'): {spanElem.get('id')}")
print(
    f"spanElem.get('some_nonexistent_addr') == None: {spanElem.get('some_nonexistent_addr') == None}")
print(f'spanElem.attrs: {spanElem.attrs}')
