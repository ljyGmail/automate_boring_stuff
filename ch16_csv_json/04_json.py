import json

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

jsonDataAsPythonValue = json.loads(stringOfJsonData)

print(f'jsonDataAsPythonValue: {jsonDataAsPythonValue}')


pythonValue = {'isCat': True, 'miceCaught': 0,
               'name': 'Zophie', 'felineIQ': None}

stringOfJsonData = json.dumps(pythonValue)

print(f'stringOfJsonData: {stringOfJsonData}')
