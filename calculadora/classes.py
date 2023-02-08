import time


class Calculadora:
    """
        Classe contendo operações de soma, subtração,
        multiplicação, divisão e potenciação
    """

    def __init__(self, calculo: str) -> None:
        self.registros = Arquivo()
        self.calculo = calculo   
        self.dados = self.trata_calculo()     
        self.num1 = self.dados[0]
        self.num2 = self.dados[2]
        self.operador = self.dados[1]        
        self.resultado = self.calcula()
        self.registros.registra_sucesso(self.__str__())

    def calcula(self):
        """Identifica operação e chama função do cálculo"""        
        if self.operador == '+':
            return self.soma(self.num1, self.num2)
        elif self.operador == '-':
            return self.subtrai(self.num1, self.num2)
        elif self.operador == '*':
            return self.multiplica(self.num1, self.num2)        
        elif self.operador == '**':
            return self.potencia(self.num1, self.num2)
        elif self.operador == '/':
            try:
                return self.divide(self.num1, self.num2)
            except ZeroDivisionError: 
                self.registros.registra_falha("deu ruim")
                print("divisão por zero")   
        else:
            self.registros.registra_falha("deu ruim")
            print("operador inválido")  
            
        

    def soma(self, num1: int, num2: int):
        """Realiza somas"""
        return num1 + num2

    def subtrai(self, num1: int, num2: int):
        """Realiza subtrações"""
        return num1 - num2

    def multiplica(self, num1: int, num2: int):
        """Reazliza multiplicações"""
        return num1 * num2

    def divide(self, num1: int, num2: int):
        """Realiza divisões"""
        return num1 / num2

    def potencia(self, num1: int, num2: int):
        """Realiza potenciações"""
        return num1 ** num2

    def trata_calculo(self):
        """ Recebo chamada de cálculo e desemebra os parâmetros
            num1, num2 e operação
        """
        lista_parametros = self.calculo.split()        
        if len(lista_parametros) != 3:
            self.registros.registra_falha(str({"operacao": self.calculo,
                                               "erro": "entrada inválida (sem operador ou sem espaços)",
                                               "data e hora": time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(time.time() - 10800))}))
            
        operador = lista_parametros[1]        
        try:
            num1 = int(lista_parametros[0])
        except TypeError:
            self.registros.registra_falha(str({"operacao": self.calcula(),
                                               "erro": "primeiro dígito inválido",
                                               "data e hora": time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(time.time() - 10800))}))
        try:
            num2 = int(lista_parametros[2])
        except TypeError:
            self.registros.registra_falha(str({"operacao": self.calcula(),
                                               "erro": "segundo dígito inválido",
                                               "data e hora": time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(time.time() - 10800))}))
        return [num1, operador, num2]

    def __str__(self):
        """Formata objeto"""
        return str({"operação": {self.calculo}, "resultado": {self.resultado},
                    "data e hora": {time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(time.time() - 10800))}})


class Arquivo:

    def __init__(self):
        pass

    ARQ_SUCESSO = 'acertos.txt'
    ARQ_FALHA = 'erros.log'

    def registra_sucesso(self, txt):
        """Grava sucesso em arquivo"""
        with open(Arquivo.ARQ_SUCESSO, 'a', encoding='utf-8') as arq:
            arq.write(txt + '\n')

    def registra_falha(self, txt):
        """Grava falha em arquivo"""
        with open(Arquivo.ARQ_FALHA, 'a', encoding='utf-8') as arq:
            arq.write(txt + '\n')
