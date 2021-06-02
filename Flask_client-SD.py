import requests
import json
import urllib.parse

api = 'http://127.0.0.1:8080'
url = f'{api}/clientes'

dados = requests.get(url).json()
#print(json.dumps(dados, indent = 4))

'''for d in dados:
    print(f'{d["CustomerId"]} - {d["FirstName"]} {d["LastName"]}')'''

id = input('Digite o id desejado: ')

url_id = f'{api}/cliente/{id}'

dados = requests.get(url_id).json()
#print(json.dumps(dados, indent = 4))

print(f'{dados[0]["CustomerId"]} - {dados[0]["FirstName"]} {dados[0]["LastName"]}')
