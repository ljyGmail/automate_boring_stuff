import re

namesRegex = re.compile(r'Agent \w+')

print(
    f"namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'): {namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')}")

# use the matched text itself as part of the substitution
agentNamesRegex = re.compile(r'Agent (\w)\w*')

print(f"agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'): ",
      agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
