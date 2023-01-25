import time


class Cnpj:

    def __init__(self, cnpj) -> None:
        self.__cnpj = cnpj.replace('.', '').replace('-', '').replace('/', '')
        if len(self.__cnpj) != 14:
            msg = f'NÚMERO DE DÍGITOS INVÁLIDO. {len(self.__cnpj)} (NECESSÁRIO 14)'
            Arquivo.registra_erro(self.__cnpj, msg)
            raise CnpjException(f'\033[31m{msg}\033[m')
        if not self.__cnpj.isnumeric():
            msg = 'CARACTERES INVÁLIDOS. ENTRE APENAS NÚMEROS'
            Arquivo.registra_erro(self.__cnpj, msg)
            raise CnpjException(f'\033[31m{msg}\033[m')

    def valida_cnpj(self):
        '''Testa cnpj (todos nr iguais, e dígito verificador'''

        if len(set(list(self.__cnpj))) == 1:  # verificação se todos os dígitos são iguais
            msg = 'CNPJ INVALIDO (DÍGITOS IGUAIS)'
            Arquivo.registra_erro(self.__cnpj, msg)
            raise CnpjException(f'\033[31m{msg}\033[m')

        cnpj_str = list(self.__cnpj)

        soma = 0   # verificação do primeiro algarismo do dígito
        mult1 = 5
        mult2 = 9
        for i in range(12):
            if i < 4:
                soma += int(cnpj_str[i]) * mult1
                mult1 -= 1
            else:
                soma += int(cnpj_str[i]) * mult2
                mult2 -= 1
        digito_1 = 0 if (soma % 11) < 2 else 11 - (soma % 11)
        if digito_1 != int(cnpj_str[12]):
            msg = 'PRIMEIRO DIGITO VERIFICADOR INVÁLIDO'
            Arquivo.registra_erro(self.__cnpj, msg)
            raise CnpjException(f'\033[31m{msg}\033[m')

        soma = 0   # verificação do segundo algarismo do dígito
        mult1 = 6
        mult2 = 9
        for i in range(13):
            if i < 5:
                soma += int(cnpj_str[i]) * mult1
                mult1 -= 1
            else:
                soma += int(cnpj_str[i]) * mult2
                mult2 -= 1
        digito_1 = 0 if (soma % 11) < 2 else 11 - (soma % 11)
        if digito_1 != int(cnpj_str[13]):
            msg = 'SEGUNDO DIGITO VERIFICADOR INVÁLIDO'
            Arquivo.registra_erro(self.__cnpj, msg)
            raise CnpjException(f'\033[31m{msg}\033[m')

        Arquivo.registra_sucesso(self.__cnpj)

        return '\033[32mCNPJ VÁLIDO\033[m'  # retorno caso cpf válido


class Arquivo(Cnpj):

    HORA = time.gmtime(time.time() - 10800)

    def __init__(self) -> None:
        pass

    def registra_sucesso(self):
        '''registro das entradas válidas'''
        with open("./cnpj_valido.txt", 'a', encoding='utf-8') as valido:
            valido.write(
                f'CNPJ {self} OK - {time.strftime("%d/%m/%Y %H:%M:%S", Arquivo.HORA)}\n')

    def registra_erro(self, msg):
        '''log de de erros'''
        with open("./cnpj_invalido.log", 'a', encoding='utf-8') as log:
            log.write(
                f'{self} {msg} - {time.strftime("%d/%m/%Y %H:%M:%S", Arquivo.HORA)}\n')


class CnpjException(Exception):
    pass
