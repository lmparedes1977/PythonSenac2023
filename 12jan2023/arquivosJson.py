import json


pessoa = {
    'nome': 'Leozão',
    'idade': 45
}

pessoa_json = json.dumps(pessoa)

print(pessoa_json)

with open('pessoa.json', 'w', encoding='utf-8') as arq:
    arq.write((json.dumps(pessoa)))
