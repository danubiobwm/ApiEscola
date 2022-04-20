import requests
import jsonpath

headers = {'Authorization': 'Token 424602972ef3470edb27941c198ad106e91e29d7'}

url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())

assert resultado.status_code == 200