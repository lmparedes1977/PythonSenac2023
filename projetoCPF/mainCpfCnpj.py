from cpf import *
from cnpj import *


continuar = True
print()
while continuar:
    try:
        resp = input(
            '\nPara validar CPF digite 1, para CNPJ digite 2: ').strip()[0]
        while resp not in '12':
            resp = input(
                '\nINVALIDO. Para validar CPF digite 1, para CNPJ digite 2: ').strip()[0]
        if resp == '1':
            meu_cpf = Cpf(input("\nDigite o CPF: "))
            validaCPF = meu_cpf.valida_cpf()
        if resp == '2':
            meu_cnpj = Cnpj(input("\nDigite o CNPJ: "))
            validaCNPJ = meu_cnpj.valida_cnpj()
    except CpfException as e:
        print(e)
    except CnpjException as e:
        print(e)
    else:
        print(validaCPF) if resp == '1' else print(validaCNPJ)
    


print('\n\033[36mFIM DO PROGRAMA\033[m\n')
