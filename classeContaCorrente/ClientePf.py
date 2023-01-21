
from Util import *
from DB import *


class ClientePf():

    def __init__(self, id, name, adress, acount_nr=Util.get_acount()) -> None:
        self.__id = id
        self.__name = name
        self.__adress = adress
        self.__acount_nr = acount_nr
        DB.set_clients_pf_list(
            self.__id, self.__name, self.__adress, self.__acount_nr)
