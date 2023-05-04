import re

xmasRegex = re.compile(r'\d+\s\w+')

print(
    f"xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'): \
        {xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')}")

# Making Your Own Character Classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(
    f"vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'): {vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')}")

# negative character class
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(
    f"consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'): {consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')}")
