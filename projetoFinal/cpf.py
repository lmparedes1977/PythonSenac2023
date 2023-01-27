
import time


class Cpf:

    def __init__(self, cpf) -> None:
        """Construtor do objeto"""
        self.__cpf = cpf
        

    @classmethod
    def recebe_cpf(cls, cpf):
        """Class Method de validação da entrada e instanciação do objeto Cpf"""
        recebido = cpf.replace('.', '').replace('-', '')
        if not recebido.isnumeric():
            msg = 'Caracter(es) INVÁLIDOS. Entre apenas números, "." e "-" .'
            Arquivo.registra_erro(recebido, msg)
            raise CpfException(msg)
        if len(recebido) != 11:
            msg = f'Número de dígitos INVÁLIDO: {len(recebido)} (NECESSÁRIO 11).'
            Arquivo.registra_erro(recebido, msg)
            raise CpfException(msg)        
        if len(set(list(recebido))) == 1:  # verificação se todos os dígitos são iguais
            msg = 'Entrada INVALIDA (DÍGITOS IGUAIS).'
            Arquivo.registra_erro(recebido, msg)
            raise CpfException(msg)    

        return cls(recebido)

    def valida_cpf(self):
        '''Testa cpf (dígitos verificadores)'''

        cpf_str = list(self.__cpf)

        soma = 0   # verificação do primeiro algarismo do dígito
        mult = 10
        for i in range(9):
            soma += int(cpf_str[i]) * mult
            mult -= 1
        digito_1 = 0 if (soma % 11) < 2 else 11 - (soma % 11)
        if digito_1 != int(cpf_str[9]):
            msg = 'Primeiro Digito Verificador INVÁLIDO.'
            Arquivo.registra_erro(self.__cpf, msg)
            raise CpfException(msg)

        soma = 0   # verificação do segundo algarismo do dígito
        mult = 11
        for i in range(10):
            soma += int(cpf_str[i]) * mult
            mult -= 1

        digito_2 = soma % 11 if (soma % 11) < 2 else 11 - (soma % 11)

        if digito_2 != int(cpf_str[10]):
            msg = 'Segundo Digito Verificador INVÁLIDO.'
            Arquivo.registra_erro(self.__cpf, msg)
            raise CpfException(msg)

        Arquivo.registra_sucesso(self.__cpf)

        return 'OK => CPF VÁLIDO.'  # retorno caso cpf válido


    def __str__(self) -> str:
        """Método mágico de string de retorno"""
        return f'CPF {self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[9:]}' 

    def __del__(self) -> str:
        print(self.__str__() + " deletado com sucesso.")


class Arquivo(Cpf):

    HORA = time.gmtime(time.time() - 10800)

    def __init__(self) -> None:        
        self.__txt_sucesso = './cpf_valido.txt'
        self.__log_erro = './cpf_invalido.log'


    @classmethod
    def gera_arquivo(cls):
        return cls()


    @staticmethod
    def registra_sucesso(cpf):
        '''registro das entradas válidas'''
        with open('./cpf_valido.txt', 'a', encoding='utf-8') as valido:
            valido.write(
                f'{cpf} OK - {time.strftime("%d/%m/%Y %H:%M:%S", Arquivo.HORA)}\n')

    @staticmethod
    def registra_erro(cpf, msg):
        '''log de de erros'''
        with open('./cpf_invalido.log', 'a', encoding='utf-8') as log:
            log.write(
                f'{cpf} - {msg} - {time.strftime("%d/%m/%Y %H:%M:%S", Arquivo.HORA)}\n')
        
  
    def __str__(self) -> str:
        return super().__str__(self)

    def __del__(self) -> str:
        return super().__del__(self)                    


class CpfException(Exception):
    pass
