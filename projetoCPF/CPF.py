from datetime import datetime
from CPFException import *


class CPF:
    def __init__(self, cpf) -> None:
        self.__cpf = cpf.replace('.', '').replace('-', '')
        if len(self.__cpf) < 11 or not self.__cpf.isnumeric():
            with open("./cpf_invalido.log", 'a', encoding='utf-8') as log:
                log.write(
                    f'ENTRADA DO USUARIO {self.__cpf} INVALIDA - {datetime.now()}\n')
            raise CPFException(
                'CPF INVÁLIDO. NECESSÁRIO 11 NÚMEROS, SEM LETRAS\n')

    def valida_cpf(self):
        cpf_str = list(self.__cpf)
        soma = 0
        mult = 10

        for i in range(9):
            soma += int(cpf_str[i]) * mult
            mult -= 1

        digito_1 = soma % 11 if (soma % 11) < 2 else 11 - (soma % 11)

        if digito_1 != int(cpf_str[9]):
            with open("./cpf_invalido.log", 'a', encoding='utf-8') as log:
                log.write(
                    f'PRIMEIRO DÍGITO DO CPF {self.__cpf} INVALIDO - {datetime.now()}\n')
            raise CPFException('\033[31mDIGITO VERIFICADOR INVÁLIDO\033[m')

        soma = 0
        mult = 11
        for i in range(10):
            soma += int(cpf_str[i]) * mult
            mult -= 1

        digito_2 = soma % 11 if (soma % 11) < 2 else 11 - (soma % 11)

        if digito_2 != int(cpf_str[10]):
            with open("./cpf_invalido.log", 'a', encoding='utf-8') as log:
                log.write(
                    f'SEGUNDO DÍGITO DO CPF {self.__cpf} INVALIDO - {datetime.now()}\n')
            raise CPFException('\033[31mDIGITO VERIFICADOR INVÁLIDO\033[m')

        with open("./cpf_valido.txt", 'a', encoding='utf-8') as valido:
            valido.write(f'CPF {self.__cpf} OK - {datetime.now()}\n')
        return '\033[32mCPF VÁLIDO\033[m'
