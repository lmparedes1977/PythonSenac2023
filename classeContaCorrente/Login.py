from DB import *
from Util import *
from ClientePf import *
from ClientePj import *


class Login(Util, DB):

    __tipo_cliente = ''
    __cliente_novo = False
    __id = ''

    def __init__(self):
        pass

    def login(self, id):

        self.__id = id.replace('.', '').replace('-', '')

        if len(self.__id) <= 11:
            if self.valida_cpf(self.__id):
                Login.__tipo_cliente = 'clientePF'
                Login.__id = self.__id
                Login.get_tipo_cliente()

                # lista_clientes = self.consultar_lista_clientes_pf()
                # if self.__id in lista_clientes:
                #     print("Bem vindo Fulano")
                #     Login.__cliente_novo = False
                # else:
                #     Login.__cliente_novo = True

        if len(self.__id) == 14:
            if self.valida_cnpj(self.__id):
                Login.__tipo_cliente = 'clientePJ'
                Login.__id = self.__id
                Login.get_tipo_cliente()
                # lista_clientes = self.consultar_lista_clientes_pj()
                # if self.__id in lista_clientes:
                #     print("Bem vindo Fulano")
                #     Login.__cliente_novo = False
                # else:
                #     Login.__cliente_novo = True

        if len(self.__id) != 14 and len(self.__id) != 11:
            raise Exception('ENTRADA INVÁLIDA')

    def get_id(self):
        return Login.__id

    @staticmethod
    def get_tipo_cliente():
        return Login.__tipo_cliente
