from classes import *

BANCO = 'BANCO SENAC'
LOGIN = 'LOGIN'
print('='*35)
print(F'{BANCO:^35}')
print('='*35)
print(F'{LOGIN:^35}\n')


pf = ClientePf.cadastra_cliente_pf(input('Digite o cpf: '), input(
    "digite o nome: "), input("Digite um endereço: "), input('Digite a senha: '))
