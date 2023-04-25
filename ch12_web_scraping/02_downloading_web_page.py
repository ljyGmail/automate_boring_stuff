import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(f'type(res): {type(res)}')

print(
    f'res.status_code == requests.codes.ok: {res.status_code == requests.codes.ok}')

print(f'len(res.text): {len(res.text)}')

print(f'res.text[:250]: {res.text[:250]}')
