from cpf import *
from cnpj import *


continuar = True
print()
while continuar:
    try:
        resp = input(
            'Para validar CPF digite 1, para CNPJ digite 2: ').strip()[0]
        while resp not in '12':
            resp = input(
                'INVALIDO. Para validar CPF digite 1, para CNPJ digite 2: ').strip()[0]
        if resp == '1':
            meu_cpf = Cpf(input("Digite o CPF: "))
            validaCPF = meu_cpf.valida_cpf()
        if resp == '2':
            meu_cnpj = Cnpj(input("Digite o CNPJ: "))
            validaCNPJ = meu_cnpj.valida_cnpj()
    except CpfException as e:
        print(e)
    except CnpjException as e:
        print(e)
    else:
        print(validaCPF) if resp == '1' else print(validaCNPJ)
    finally:
        continua = input('DESEJA CONTUNAR: [S/N]').upper().strip()[0]
        while continua not in 'SN':
            continua = input(
                'INVALIDO. DESEJA CONTUNAR: [S/N]').upper().strip()[0]
        if continua == 'N':
            continuar = False


print('FIM DO PROGRAMA')
