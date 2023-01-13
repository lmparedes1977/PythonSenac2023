from CPF import *


continuar = True
while continuar:
    try:
        meu_cpf = CPF(input("Digite o CPF: "))
        valida = meu_cpf.valida_cpf()
    except CPFException as e:
        print(e)
    else:
        print(valida)
    finally:
        continua = input('DESEJA CONTUNAR: [S/N]').upper().strip()[0]
        while continua not in 'SN':
            continua = input(
                'INVALIDO. DESEJA CONTUNAR: [S/N]').upper().strip()[0]
        if continua == 'N':
            continuar = False
else:
    print('FIM DO PROGRAMA')
