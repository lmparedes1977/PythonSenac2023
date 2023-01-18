

class DB:

    def registrar_cliente(self):
        with open('lista_de_clientes.txt', 'a') as arq:
            arq.write(f'{self.__nome:<20} {self.__nr_conta}\n')

    def consultar_registro(self):
        pass
