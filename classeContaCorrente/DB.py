from datetime import datetime


class DB:

    @staticmethod
    def set_clients_pf_list(id, name, adress, acount_nr):
        '''Doc'''
        with open('pf.txt', 'a') as arq:
            arq.write(f'{id:<20} {name:<20} {adress:<40} {acount_nr:<20}\n')

    @staticmethod
    def set_clients_pj_list(id, name, adress, acount_nr):
        '''Doc'''
        with open('pj.txt', 'a') as arq:
            arq.write(f'{id:<20} {name:<20} {adress:<40} {acount_nr:<20}\n')

    @staticmethod
    def get_clients_pf_list():
        '''Doc'''
        lista = []
        with open('pf.txt', 'r') as arq:
            arq.readlines()
            lista = [linha.rstrip().split() for linha in arq]
        return lista

    @staticmethod
    def get_clients_pj_list():
        '''Doc'''
        with open('pj.txt', 'r') as arq:
            arq.readlines()
            arq = [linha.rstrip().split() for linha in arq]
            return arq

    @staticmethod
    def set_client_pf(self, id):
        '''Doc'''
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
