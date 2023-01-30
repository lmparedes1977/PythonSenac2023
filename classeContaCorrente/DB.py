from datetime import datetime
import json


class DB:

    __PF = 'pf.json'
    __PJ = 'pj.json'

    def fetch_data(type_client):

        # @staticmethod
        # def set_clients_pf_list(id, name, adress, account_nr):
        #     '''Doc'''
        #     clientes_pf = {}
        #     with open(DB.__TODOS_PF, encoding='utf-8') as file:
        #         json.dump(file, clientes_pf)
        #     clientes_pf['pf'].append({'id': id, 'name': name,
        #                               'adress': adress, 'account_nr': account_nr,
        #                               'balance': 0, 'bank_st': []})
        #     with open(DB.__TODOS_PF, 'w', encoding='utf-8') as file:
        #         file.write(json.load(clientes_pf, ensure_ascii=False))

        # @staticmethod
        # def set_clients_pj_list(id, name, adress, account_nr):
        #     '''Doc'''
        #     clientes_pj = {}
        #     with open(DB.__TODOS_PJ, encoding='utf-8') as file:
        #         json.dump(file, clientes_pj)
        #     clientes_pj['pf'].append({'id': id, 'name': name,
        #                               'adress': adress, 'account_nr': account_nr,
        #                               'balance': 0, 'bank_st': []})
        #     with open(DB.__TODOS_PJ, 'w', encoding='utf-8') as file:
        #         file.write(json.load(clientes_pj, ensure_ascii=False))

        # @staticmethod
        # def get_clients_pf_list():
        #     '''Doc'''
        #     clientes_pf = {}
        #     with open(DB.__TODOS_PJ, encoding='utf-8') as file:
        #         json.dump(file, clientes_pf)
        #     return clientes_pf

        # @staticmethod
        # def get_clients_pj_list():
        #     '''Doc'''
        #     clientes_pj = {}
        #     with open(DB.__TODOS_PJ, encoding='utf-8') as file:
        #         json.dump(file, clientes_pj)
        #     return clientes_pj

        # @staticmethod
        # def deposit_pf(self, amount):
        #     '''Doc'''
        #     clientes_pf = {}
        #     with open(DB.__TODOS_PF, encoding='utf-8') as file:
        #         json.dump(file, clientes_pf)
        #     clientes_pf['pf'].append({'id': id, 'name': name,
        #                               'adress': adress, 'account_nr': account_nr,
        #                               'balance': 0, 'bank_st': []})
        #     with open(DB.__TODOS_PF, 'w', encoding='utf-8') as file:
        #         file.write(json.load(clientes_pf, ensure_ascii=False))
        #     pass

        # @staticmethod
        # def set_client_pj(self, id):
        #     '''Doc'''
        #     pass

        # @staticmethod
        # def get_cliente_pf(self, id):
        #     '''Doc'''
        #     pass

        # @staticmethod
        # def get_cliente_pj(self, id):
        #     '''Doc'''
        #     pass

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
