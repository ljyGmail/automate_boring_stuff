# Creating Regex Objects
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Matching Regex Objects
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(f'Phone number found: {mo.group()}')

# More Pattern Matching with Regular Expressions

# Grouping with Parentheses
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(f'mo.group(1): {mo.group(1)}')
print(f'mo.group(2): {mo.group(2)}')
print(f'mo.group(0): {mo.group(0)}')
print(f'mo.group(): {mo.group()}')

print(f'mo.groups(): {mo.groups()}')
areaCode, mainNumber = mo.groups()
print(f'areaCode: {areaCode}')
print(f'mainNumber: {mainNumber}')

# escape parenthesis
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(f'mo.group(1): {mo.group(1)}')
print(f'mo.group(2): {mo.group(2)}')

# Matching Multiple Groups with the Pipe
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(f'mo1.group(): {mo1.group()}')

mo2 = heroRegex.search('Tina Fey and Batman')
print(f'mo2.group(): {mo2.group()}')

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(f'mo.group(): {mo.group()}')
print(f'mo.group(1): {mo.group(1)}')

# Optional Matching with the Question Mark
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(f'mo1.group(): {mo1.group()}')

mo2 = batRegex.search('The Adventures of Batwoman')
print(f'mo2.group(): {mo2.group()}')

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242.')
print(f'mo1.group(): {mo1.group()}')

mo2 = phoneRegex.search('My number is 555-4242.')
print(f'mo2.group(): {mo2.group()}')

# Matching Zero or More with the Star
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(f'mo1.group(): {mo1.group()}')

mo2 = batRegex.search('The Adventures of Batwoman')
print(f'mo2.group(): {mo2.group()}')

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(f'mo3.group(): {mo3.group()}')

# Matching One or More with the Plus
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(f'mo1.group(): {mo1.group()}')

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(f'mo2.group(): {mo2.group()}')

mo3 = batRegex.search('The Adventures of Batman')
print(f'mo3 == None: {mo3 == None}')

# Matching Specific Repetitions with Braces
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(f'mo1.group(): {mo1.group()}')

mo2 = haRegex.search('Ha')
print(f'mo2 == None: {mo2 == None}')
