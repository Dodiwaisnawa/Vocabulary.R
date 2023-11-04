import requests

api_key = '9716e5f1-ecfb-4367-80a2-a8ac0e2e12f7'
word = 'Banana'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions :
    print(definitions)