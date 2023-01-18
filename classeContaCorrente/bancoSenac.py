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
if id.login(input('DIGITE O CPF/CNPJ: ')) == 'clientePF':
    pass
