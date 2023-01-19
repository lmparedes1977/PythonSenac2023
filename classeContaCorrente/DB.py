

class DB:

    def registrar_lista_clientes_pf(self, id, name, adress, acount_nr):
        with open('pf.txt', 'a') as arq:
            arq.write(f'{id:<20} {name:<20} {adress:<40} {acount_nr:<20}\n')

    def registrar_lista_clientes_pj(self, nome, conta):
        with open('pj.txt', 'a') as arq:
            arq.write(f'{nome:<20} {conta}\n')

    @staticmethod
    def consultar_lista_clientes_pf(self):
        lista = []
        with open('pf.txt', 'r') as arq:
            arq.readlines()
            lista = [linha.rstrip().split() for linha in arq]
        return lista

    @staticmethod
    def consultar_lista_clientes_pj():
        with open('pj.txt', 'r') as arq:
            arq.readlines()
            arq = [linha.rstrip().split() for linha in arq]
            return arq

    def consultar_cliente_pf(self, id):
        pass

    def consultar_cliente_pf(self, id):
        pass
