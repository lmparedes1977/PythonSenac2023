
from DB import *

CAMINHO = './arquivos/'


class Util(DB):

    __nr_cadastro = 0
    __next_PF = 0
    __next_PJ = 0

    @staticmethod
    def __calcular_dv(account_nr):
        mult = 10
        soma = 0
        for n in account_nr:
            soma += int(n) * mult
            mult -= 1
        resto = soma % 11
        return resto if resto < 2 else 11 - resto

    @staticmethod
    def get_acount():

        Util.__next_PF += 1
        return Util.__next_PF

    def valida_cpf(self, id):
        '''testar todos os números iguais,
           e dígito verificador é válido'''

        self.__cpf = id

        if len(set(list(self.__cpf))) == 1:    # verificação se todos os dígitos são iguais
            DB.registra_erro_cpf(self.__cpf, 'DIGITOS IGUAIS')
            raise CpfException(
                '\033[31mCPF COM TODOS OS DIGITOS IGUAIS (INVÁLIDO)\033[m')

        cpf_str = list(self.__cpf)

        soma = 0    # verificação do primeiro algarismo do dígito
        mult = 10
        for i in range(9):
            soma += int(cpf_str[i]) * mult
            mult -= 1
        digito_1 = 0 if (soma % 11) < 2 else 11 - (soma % 11)
        if digito_1 != int(cpf_str[9]):
            DB.registra_erro_cpf(self.__cpf, 'PRIMEIRO')
            return False

        soma = 0   # verificação do segundo algarismo do dígito
        mult = 11
        for i in range(10):
            soma += int(cpf_str[i]) * mult
            mult -= 1
        digito_2 = 0 if (soma % 11) < 2 else 11 - (soma % 11)
        if digito_2 != int(cpf_str[10]):
            DB.registra_erro_cpf(self.__cpf, 'SEGUNDO')
            return False

        DB.registra_sucesso_cpf(self.__cpf)
        return True    # retorno caso cpf válido

    def valida_cnpj(self, id):
        '''Testa cnpj (todos nr iguais, e dígito verificador'''

        self.__cnpj = id

        if len(set(list(self.__cnpj))) == 1:  # verificação se todos os dígitos são iguais
            DB.registra_erro_cnpj(self.__cnpj, "DIGITOS IGUAIS")
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
            DB.registra_erro_cnpj(self.__cnpj, "PRIMEIRO")
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
            DB.registra_erro_cnpj(self.__cnpj, "SEGUNDO")
            raise CnpjException('\033[31mDIGITO VERIFICADOR INVÁLIDO\033[m')

        DB.registra_sucesso_cnpj(self.__cnpj)

        return '\033[32mcnpj VÁLIDO\033[m'  # retorno caso cpf válido


class CpfException(Exception):
    pass


class CnpjException(Exception):
    pass
