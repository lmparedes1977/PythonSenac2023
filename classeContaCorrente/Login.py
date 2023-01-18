
from Util import *


class Login(Util):
    id_cliente = 1
    tipo_cliente = ''

    def __init__(self):
        pass

    def login(self, id):
        self.__id = id.replace('.', '').replace('-', '')
        if len(self.__id) <= 11:
            if self.valida_cpf(self.__id):
                Login.tipo_cliente = 'clientePF'
                with open('cadastro_geral.txt', 'r') as arq:
                    arq.readlines()
                    arq = [linha.rstrip().split() for linha in arq]
                    if self.__if in arq:

        if len(self.__id) == 14:
            Login.tipo_cliente = 'clientePJ'
        else:
            raise Exception('ENTRADA INVÁLIDA')
