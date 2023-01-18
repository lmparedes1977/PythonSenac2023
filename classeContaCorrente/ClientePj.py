from Cliente import *


class ClientePj(Cliente):

    def __init__(self, id, name, adress, acount_nr) -> None:
        Cliente.__init__(self, id)
        self.__name = name
        self.__adress = adress
        self.__acount_nr = acount_nr
