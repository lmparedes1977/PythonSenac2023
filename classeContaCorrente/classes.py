from datetime import datetime
import json


class Login():
    """Classe para identificação do usuário"""

    @staticmethod
    def login(conta, senha):
        pass

    def get_id(self):
        pass

    @staticmethod
    def get_tipo_cliente():
        pass


class ClientePf():

    def __init__(self, id: str) -> None:
        self.__id = id

    @staticmethod
    def cadastra_cliente_pf(cpf, nome, endereco, senha):
        cliente = {'id': Util.next_id(), 'cpf': cpf, 'nome': nome, 'endereco': endereco,
                   'nr_conta': Util.next_account_pf(), 'senha': senha, 'saldo': 0, 'extrato': []}
        cadastro = DB.le_json(DB.CLIENTES_PF)
        cadastro['clientes']: list.append(cliente)
        DB.escreve_json(DB.CLIENTES_PF, cadastro)
        return ClientePf.login_pf(cliente['id'])

    @classmethod
    def login_pf(cls, id):
        return cls(id)


class ClientePj():

    def __init__(self, id: str) -> None:
        self.__id = id

    @staticmethod
    def cadastra_cliente_pj(cnpj, nome, endereco, senha):
        cliente = {'id': Util.next_id(), 'cnpj': cnpj, 'nome': nome, 'endereco': endereco,
                   'nr_conta': Util.next_account_pj(), 'senha': senha, 'saldo': 0, 'extrato': []}
        cadastro = DB.le_json(DB.CLIENTES_PJ)
        cadastro['clientes']: list.append(cliente)
        DB.escreve_json(DB.CLIENTES_PJ, cadastro)
        return ClientePj.login_pj(cliente['id'])

    @classmethod
    def login_pj(cls, id):
        return cls(id)


class DB:

    CLIENTES_PF = 'pf.json'
    CLIENTES_PJ = 'pj.json'
    NEXT = 'next.json'

    @staticmethod
    def le_json(arquivo):
        with open(arquivo, encoding='utf-8') as arq:
            return json.load(arq)

    @staticmethod
    def escreve_json(arquivo, dado):
        with open(arquivo, 'w', encoding='utf-8') as arq:
            arq.write(json.dumps(dado, ensure_ascii=False))

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
    def calcula_dv(account_nr):
        account = list(str(account_nr))
        mult = len(account)
        soma = 0
        for n in account_nr:
            soma += int(n) * mult
            mult -= 1
        resto = soma % 11
        return resto if resto < 2 else 11 - resto

    @staticmethod
    def next_id():
        arquivo = DB.le_json(DB.NEXT)
        id = arquivo['next_id']
        arquivo['next_id'] += 1
        DB.escreve_json(DB.NEXT, arquivo)
        return id

    @staticmethod
    def next_account_pf():
        arquivo = DB.le_json(DB.NEXT)
        account = arquivo['next_account_pf']
        arquivo['next_account_pf'] += 1
        DB.escreve_json(DB.NEXT, arquivo)
        return account

    @staticmethod
    def next_account_pj():
        arquivo = DB.le_json(DB.NEXT)
        account = arquivo['next_account_pj']
        arquivo['next_account_pj'] += 1
        DB.escreve_json(DB.NEXT, arquivo)
        return account

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
