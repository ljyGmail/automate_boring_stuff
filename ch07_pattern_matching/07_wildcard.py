import re

atRegex = re.compile(r'.at')
print(
    f"atRegex.findall('The cat in the hat sat on the flat mat.'): {atRegex.findall('The cat in the hat sat on the flat mat.')}")

# Matching Everything with Dot-Star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(f'mo.group(1): {mo.group(1)}')
print(f'mo.group(2): {mo.group(2)}')

# non-greedy dot-star
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(f'mo.group(): {mo.group()}')

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(f'mo.group(): {mo.group()}')

# Matching Newlines with the Dot Character
noNewlineRegex = re.compile('.*')

print("noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group():",
      noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

newlineRegex = re.compile('.*', re.DOTALL)

print("newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group():",
      newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
