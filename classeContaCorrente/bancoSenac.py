# @classmethod
# def cria_goblin(cls):
#   return Classe(arg, arg, arg)

# @staticmethod
# def faz_algo(): <- não envolve um objeto instanciado (self)
#   código


from ClientePj import *
from ClientePf import *
from Login import *

BANCO = 'BANCO SENAC'
LOGIN = 'LOGIN'
print('='*35)
print(F'{BANCO:^35}')
print('='*35)
print(F'{LOGIN:^35}\n')

id = Login()
cliente = ''
tipo_cliente = input('DIGITE O CPF/CNPJ: ')
if id.login(tipo_cliente) == 'clientePF':
    print("SEJA BEM VINDO!".center(35))
    cliente = ClientePf(id.get_id(), input(
        "Nome completo:"), input("Endereço"))
