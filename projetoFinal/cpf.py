
import time


class Cpf:

    def __init__(self, cpf) -> None:
        self.__cpf = cpf
        

    @classmethod
    def recebe_cpf(cls, cpf):
        recebido = cpf.replace('.', '').replace('-', '')
        if not recebido.isnumeric():
            msg = 'CARACTERES INVÁLIDOS. ENTRE APENAS NÚMEROS'
            Arquivo.registra_erro(recebido, msg)
            raise CpfException(msg)
        if len(recebido) != 11:
            msg = f'NÚMERO DE DÍGITOS INVÁLIDO. {len(recebido)} (NECESSÁRIO 11)'
            Arquivo.registra_erro(recebido, msg)
            raise CpfException(msg)        
        if len(set(list(recebido))) == 1:  # verificação se todos os dígitos são iguais
            msg = 'ENTRADA INVALIDA (DÍGITOS IGUAIS)'
            Arquivo.registra_erro(recebido, msg)
            raise CpfException(msg)    

        return cls(recebido)

    def valida_cpf(self):
        '''Testa cpf (todos nr iguais, e dígito verificador'''

        cpf_str = list(self.__cpf)

        soma = 0   # verificação do primeiro algarismo do dígito
        mult = 10
        for i in range(9):
            soma += int(cpf_str[i]) * mult
            mult -= 1
        digito_1 = 0 if (soma % 11) < 2 else 11 - (soma % 11)
        if digito_1 != int(cpf_str[9]):
            msg = 'PRIMEIRO DIGITO VERIFICADOR INVÁLIDO'
            Arquivo.registra_erro(self.__cpf, msg)
            raise CpfException(msg)

        soma = 0   # verificação do segundo algarismo do dígito
        mult = 11
        for i in range(10):
            soma += int(cpf_str[i]) * mult
            mult -= 1

        digito_2 = soma % 11 if (soma % 11) < 2 else 11 - (soma % 11)

        if digito_2 != int(cpf_str[10]):
            msg = 'SEGUNDO DIGITO VERIFICADOR INVÁLIDO'
            Arquivo.registra_erro(self.__cpf, msg)
            raise CpfException(msg)

        Arquivo.registra_sucesso(self.__cpf)

        return 'OK => CPF VÁLIDO'  # retorno caso cpf válido


class Arquivo(Cpf):

    HORA = time.gmtime(time.time() - 10800)

    def registra_sucesso(self):
        '''registro das entradas válidas'''
        with open('./cpf_valido.txt', 'a', encoding='utf-8') as valido:
            valido.write(
                f'CPF {self} OK - {time.strftime("%d/%m/%Y %H:%M:%S", Arquivo.HORA)}\n')

    def registra_erro(self, msg):
        '''log de de erros'''
        with open('./cpf_invalido.log', 'a', encoding='utf-8') as log:
            log.write(
                f'{self} - {msg} - {time.strftime("%d/%m/%Y %H:%M:%S", Arquivo.HORA)}\n')


class CpfException(Exception):
    pass
