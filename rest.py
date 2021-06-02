import requests
import json
import urllib.parse

connStr = 'https://geocode.search.hereapi.com/v1/geocode?'
connKey = 'dM-cWRsThiY0t2ZyQRy6il7o6paj2MZJCj9zxdktUzc'
lang = 'pt-BR'

endereco = 'Sao Goncalo'

valores = urllib.parse.urlencode({'apiKey':connKey, 'lang':lang, 'q':endereco})

#print(valores)
url = f'{connStr}{valores}'
print(url)

request = requests.get(url).json()
print(json.dumps(request, indent = 4))

teste = f'Latitude: {request["items"][0]["position"]["lat"]} Longitude: {request["items"][0]["osition"]["lng"]}'

print()