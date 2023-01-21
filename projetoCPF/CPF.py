from datetime import datetime


class Cpf:
    def __init__(self, cpf) -> None:
        self.__cpf = cpf.replace('.', '').replace('-', '')
        if len(self.__cpf) < 11 or not self.__cpf.isnumeric():
            with open("./cpf_invalido.log", 'a', encoding='utf-8') as log:
                log.write(
                    f'ENTRADA DO USUARIO {self.__cpf} INVALIDA - {datetime.now()}\n')
            raise CpfException(
                'CPF INVÁLIDO. NECESSÁRIO 11 NÚMEROS (NÃO TODOS IGUAIS), SEM LETRAS\n')

    def valida_cpf(self):
        '''Testa cpf (todos nr iguais, e dígito verificador'''

        if len(set(list(self.__cpf))) == 1:  # verificação se todos os dígitos são iguais
            with open("./cpf_invalido.log", 'a', encoding='utf-8') as log:
                log.write(
                    f'CPF {self.__cpf} INVALIDO (DÍGITOS IGUAIS) - {datetime.now()}\n')
            raise CpfException(
                '\033[31mCPF COM TODOS OS DIGITOS IGUAIS (INVÁLIDO)\033[m')

        cpf_str = list(self.__cpf)

        soma = 0   # verificação do primeiro algarismo do dígito
        mult = 10
        for i in range(9):
            soma += int(cpf_str[i]) * mult
            mult -= 1
        digito_1 = 0 if (soma % 11) < 2 else 11 - (soma % 11)
        if digito_1 != int(cpf_str[9]):
            Arquivo.registra_erro(self.__cpf)
            raise CpfException('\033[31mDIGITO VERIFICADOR INVÁLIDO\033[m')

        soma = 0   # verificação do segundo algarismo do dígito
        mult = 11
        for i in range(10):
            soma += int(cpf_str[i]) * mult
            mult -= 1

        digito_2 = soma % 11 if (soma % 11) < 2 else 11 - (soma % 11)

        if digito_2 != int(cpf_str[10]):
            Arquivo.registra_erro(self.__cpf)
            raise CpfException('\033[31mDIGITO VERIFICADOR INVÁLIDO\033[m')

        Arquivo.registra_sucesso(self.__cpf)

        return '\033[32mCPF VÁLIDO\033[m'  # retorno caso cpf válido


class Arquivo(Cpf):
    def __init__(self) -> None:
        pass

    def registra_sucesso(self):
        '''registro das entradas válidas'''
        with open("./cpf_valido.txt", 'a', encoding='utf-8') as valido:
            valido.write(f'CPF {self} OK - {datetime.now()}\n')

    def registra_erro(self):
        '''log de de erros'''
        with open("./cpf_invalido.log", 'a', encoding='utf-8') as log:
            log.write(
                f'SEGUNDO DÍGITO DO CPF {self} INVALIDO - {datetime.now()}\n')


class CpfException(Exception):
    pass
