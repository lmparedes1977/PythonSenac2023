from datetime import datetime


class Cnpj:
    def __init__(self, cnpj) -> None:
        self.__cnpj = cnpj.replace('.', '').replace('-', '')
        if len(self.__cnpj) < 14 or not self.__cnpj.isnumeric():
            with open("./cnpj_invalido.log", 'a', encoding='utf-8') as log:
                log.write(
                    f'ENTRADA DO USUARIO {self.__cnpj} INVALIDA - {datetime.now()}\n')
            raise CnpjException(
                'cnpj INVÁLIDO. NECESSÁRIO 14 NÚMEROS (NÃO TODOS IGUAIS), SEM LETRAS\n')

    def valida_cnpj(self):
        '''Testa cnpj (todos nr iguais, e dígito verificador'''

        if len(set(list(self.__cnpj))) == 1:  # verificação se todos os dígitos são iguais
            with open("./cnpj_invalido.log", 'a', encoding='utf-8') as log:
                log.write(
                    f'cnpj {self.__cnpj} INVALIDO (DÍGITOS IGUAIS) - {datetime.now()}\n')
            raise CnpjException(
                '\033[31mcnpj COM TODOS OS DIGITOS IGUAIS (INVÁLIDO)\033[m')

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
            Arquivo.registra_erro(self.__cnpj)
            raise CnpjException('\033[31mDIGITO VERIFICADOR INVÁLIDO\033[m')

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
            Arquivo.registra_erro(self.__cnpj)
            raise CnpjException('\033[31mDIGITO VERIFICADOR INVÁLIDO\033[m')

        Arquivo.registra_sucesso(self.__cnpj)

        return '\033[32mcnpj VÁLIDO\033[m'  # retorno caso cpf válido


class Arquivo(Cnpj):
    def __init__(self) -> None:
        pass

    def registra_sucesso(self):
        '''registro das entradas válidas'''
        with open("./cnpj_valido.txt", 'a', encoding='utf-8') as valido:
            valido.write(f'cnpj {self} OK - {datetime.now()}\n')

    def registra_erro(self):
        '''log de de erros'''
        with open("./cnpj_invalido.log", 'a', encoding='utf-8') as log:
            log.write(
                f'SEGUNDO DÍGITO DO cnpj {self} INVALIDO - {datetime.now()}\n')


class CnpjException(Exception):
    pass
