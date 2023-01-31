from datetime import datetime
import json


class Login():
    """Classe para identificação do usuário"""

    @staticmethod
    def login(conta, senha):

    def get_id(self):
        return Login.__id

    @staticmethod
    def get_tipo_cliente():
        return Login.__tipo_cliente


class ClientePf():

    def __init__(self, cpf: str, nome: str, endereco: str, nr_conta: str, senha: str) -> None:
        self.__cpf = cpf
        self.__nome = nome
        self.endreco = endereco
        self.__nr_conta = nr_conta
        self.__senha = senha

    @classmethod
    def cliente_logado(cls, cpf, nome, endereco, nr_conta, )


class ClientePj():

    def __init__(self, cnpj: str, nome: str, endereco: str, nr_conta: str, senha: str) -> None:
        self.__cnpj = cnpj
        self.__nome = nome
        self.__endreco = endereco
        self.__nr_conta = nr_conta
        self.__senha = senha


class DB:

    __CLIENTES_PF = 'pf.json'
    __CLIENTES_PJ = 'pj.json'

    @staticmethod
    def cria_cliente_pf(cpf, nome, endereco, senha):
        '''Inclui novo Cliente no DB (arquivo JSON __CLIENTES_PF)'''
        clientes = {}
        with open(DB.__CLIENTES_PF, encoding='utf-8') as arq:
            json.dump(arq, clientes)
        clientes['clientes'].append({'id': clientes['nextId'], 'cpf': cpf, 'nome': nome,
                                     'endereco': endereco, 'nr_conta': clientes['nextAccount'],
                                     'senha': senha})
        clientes['nextId'], clientes['nextAccount'] += 1, 1
        with open(DB.__CLIENTES_PF, 'w', encoding='utf-8') as file:
            file.write(json.load(clientes, ensure_ascii=False))

    @staticmethod
    def set_clients_pj_list(cnpj, nome, endereco, senha):
        '''Inclui novo Cliente no DB (arquivo JSON __CLIENTES_PJ)'''
        clientes = {}
        with open(DB.__CLIENTES_PJ, encoding='utf-8') as arq:
            json.dump(arq, clientes)
        clientes['clientes'].append({'id': clientes['nextId'], 'cnpf': cnpj, 'nome': nome,
                                     'endereco': endereco, 'nr_conta': clientes['nextAccount'],
                                     'senha': senha})
        clientes['nextId'], clientes['nextAccount'] += 1, 1
        with open(DB.__CLIENTES_PJ, 'w', encoding='utf-8') as file:
            file.write(json.load(clientes, ensure_ascii=False))

    @staticmethod
    def get_clients_pf_list():
        '''Doc'''
        clientes_pf = {}
        with open(DB.__CLIENTES_PJ, encoding='utf-8') as file:
            json.dump(file, clientes_pf)
        return clientes_pf

    @staticmethod
    def get_clients_pj_list():
        '''Doc'''
        clientes_pj = {}
        with open(DB.__CLIENTES_PJ, encoding='utf-8') as file:
            json.dump(file, clientes_pj)
        return clientes_pj

    @staticmethod
    def deposit_pf(self, amount):
        '''Doc'''
        clientes_pf = {}
        with open(DB.__CLIENTES_PF, encoding='utf-8') as file:
            json.dump(file, clientes_pf)
        clientes_pf['pf'].append({'id': id, 'name': name,
                                  'adress': adress, 'account_nr': account_nr,
                                  'balance': 0, 'bank_st': []})
        with open(DB.__CLIENTES_PF, 'w', encoding='utf-8') as file:
            file.write(json.load(clientes_pf, ensure_ascii=False))
        pass

    @staticmethod
    def set_client_pj(self, id):
        '''Doc'''
        pass

    @staticmethod
    def get_cliente_pf(self, id):
        '''Doc'''
        pass

    @staticmethod
    def get_cliente_pj(self, id):
        '''Doc'''
        pass

    def registra_sucesso_cpf(self):
        '''registro das entradas válidas'''
        with open("./cpf_valido.txt", 'a', encoding='utf-8') as valido:
            valido.write(f'CPF {self} OK - {datetime.now()}\n')

    def registra_erro_cpf(self, digito):
        '''log de de erros'''
        with open("./cpf_invalido.log", 'a', encoding='utf-8') as log:
            log.write(
                f'{digito} DÍGITO DO CPF {self} INVALIDO - {datetime.now()}\n')

    def registra_sucesso_cnpj(self):
        '''registro das entradas válidas'''
        with open("./cnpj_valido.txt", 'a', encoding='utf-8') as valido:
            valido.write(f'CNPJ {self} OK - {datetime.now()}\n')

    def registra_erro_cnpj(self, digito):
        '''log de de erros'''
        with open("./cnpj_invalido.log", 'a', encoding='utf-8') as log:
            log.write(
                f'{digito} DÍGITO DO CNPJ {self} INVALIDO - {datetime.now()}\n')


class Servicos:

    def depositar(self, deposito):
        pass

    def sacar(self, saque):
        pass

    def consulta_saldo(self):
        pass


class Util():

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
