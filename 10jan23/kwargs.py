pessoa = {
    'nome': 'Leozão',
    'sobrenome': 'Paredes',
}

dados_pessoa = {
    'nr_pe': 43,
    'idade': 46,
}

dados_completos = {**pessoa, **dados_pessoa}

print(dados_completos)

for dado in dados_completos.values():
    print(f'{dado=}')
