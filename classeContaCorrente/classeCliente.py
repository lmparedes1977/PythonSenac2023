

class Cliente:
    __next_acount = '10000'

    def __init__(self, nome, nr_conta=__next_acount) -> None:
        self.__nome = nome
        self.__conta_base = nr_conta
        self.__nr_conta = self.__conta_base + \
            "-" + str(Cliente.__calcular_dv(self))
        if self.__conta_base == Cliente.__next_acount:
            Cliente__next_acount = str(int(Cliente.__next_acount) + 1)
        print(self.__nome, self.__nr_conta)

    def depositar(self, deposito):
        pass

    def sacar(self, saque):
        pass

    def consulta_saldo(self):
        pass

    def __calcular_dv(self):
        mult = 10
        soma = 0
        for n in self.__conta_base:
            soma += int(n) * mult
            mult -= 1
        resto = soma % 11
        return resto if resto < 2 else 11 - resto

    def registrar_cliente(self):
        with open('lista_de_clientes.txt', 'a') as arq:
            arq.write(f'{self.__nome:<20} {self.__nr_conta}\n')

    def consultar_registro(self):
        pass


cliente = Cliente("Leozão")
