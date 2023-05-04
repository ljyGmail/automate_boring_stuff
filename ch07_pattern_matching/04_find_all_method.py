import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(f'mo.group(): {mo.group()}')


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
print(
    f"phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'): {phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')}")

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
print(
    f"phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'): {phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')}")

# To summarize what the findall() method returns:
# When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d, findall() returns a list of string metches
# When called on a regex with groups, such as (\d\d\d)-(\d\d\d)-(\d\d\d\d), findall() returns a list of tuples of strings (one string for each group)
