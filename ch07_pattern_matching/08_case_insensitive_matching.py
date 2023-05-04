import re

# the following regexes match completely different strings
regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

# case-insensitive matching
robocop = re.compile(r'robocop', re.IGNORECASE)
print(
    f"robocop.search('RoboCop is part man, part machine, all cop.').group(): {robocop.search('RoboCop is part man, part machine, all cop.').group()}")

print(
    f"robocop.search('ROBOCOP protects the innocent.').group(): {robocop.search('ROBOCOP protects the innocent.').group()}")

print(
    f"robocop.search('Al, why does your programming book talk about robocop so much?').group(): {robocop.search('Al, why does your programming book talk about robocop so much?').group()}")
