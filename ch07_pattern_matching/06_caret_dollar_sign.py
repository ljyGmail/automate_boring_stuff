import re

beginsWithHello = re.compile(r'^Hello')
print(
    f"beginsWithHello.search('Hello, world!'): {beginsWithHello.search('Hello, world!')}")

print(
    f"beginsWithHello.search('He said Hello.') == None: {beginsWithHello.search('He said Hello.') == None}")

endsWithNumber = re.compile(r'\d$')
print(
    f"endsWithNumber.search('Your number is 42'): {endsWithNumber.search('Your number is 42')}")

print(
    f"endsWithNumber.search('Your number is forty two.') == None: {endsWithNumber.search('Your number is forty two.') == None}")

wholeStringIsNum = re.compile(r'^\d+$')
print(
    f"wholeStringIsNum.search('1234567890'): {wholeStringIsNum.search('1234567890')}")

print(
    f"wholeStringIsNum.search('12345xyz67890') == None: {wholeStringIsNum.search('12345xyz67890') == None}")

print(
    f"wholeStringIsNum.search('12  34567890') == None: {wholeStringIsNum.search('12  34567890') == None}")
