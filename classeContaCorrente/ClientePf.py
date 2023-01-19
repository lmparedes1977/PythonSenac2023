from Cliente import *
from Util import *
from DB import *


class ClientePf(Cliente, DB):

    def __init__(self, id, name, adress, acount_nr=DB.get) -> None:
        Cliente.__init__(self, id)
        self.__name = name
        self.__adress = adress
        self.__acount_nr = acount_nr
        self.registrar_lista_clientes_pf(
            self.__id, self.__namename, self.__adress, self.__acount_nr)
