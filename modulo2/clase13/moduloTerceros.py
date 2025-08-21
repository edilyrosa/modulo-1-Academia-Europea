import requests
url = 'https://whenisthenextmcufilm.com/api'
res = requests.get(url)
if res.status_code == 200:
    datos = res.json()
    print('TDD de la data', type(datos))
    print('La data', datos)
    print('---'*40)
    print('La url del post es', datos["following_production"]["poster_url"])
else: print('Error', res.status_code)


