import time


class Calculadora:
    """
        Classe contendo operações de soma, subtração,
        multiplicação, divisão e potenciação
    """

    def __init__(self, calculo: str) -> None:
        self.registros = Arquivo()
        self.calculo = calculo
        try:
            self.dados = self.trata_calculo()
            self.num1 = self.dados[0]
            self.num2 = self.dados[2]
            self.operacao = self.dados[1]
            self.resultado = self.calcula()
            self.registros.registra_sucesso(self.__str__())
        except Exception as exc:
            meu_dict = {'operacao': exc}
            str(meu_dict)
            abre_chave = '{'
            fecha_chave = '}'
            self.registros.registra_falha(
                f'{abre_chave}"operacao": "{self.calculo}", {exc}, "data e hora": \
                    "{time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(time.time() - 10800))}"{fecha_chave}')

    def calcula(self):
        """Identifica operação e chama função do cálculo"""
        try:
            if self.operacao == '+':
                return self.soma(self.num1, self.num2)
            elif self.operacao == '-':
                return self.subtrai(self.num1, self.num2)
            elif self.operacao == '*':
                return self.multiplica(self.num1, self.num2)
            elif self.operacao == '/':
                return self.divide(self.num1, self.num2)
            elif self.operacao == '**':
                return self.potencia(self.num1, self.num2)
            else:
                raise Exception('"erro": "operador inválido"')
        except ZeroDivisionError as exc:
            print("Divisão por 0 inválida")
            raise Exception(
                '"erro":"não é possível dividir por zero"') from exc

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
            self.registros.registra_falha('parametros em excesso')

        lista_parametros = self.split_calculo()
        lista_parametros = self.str_p_int(lista_parametros)
        return lista_parametros

    def split_calculo(self):
        """Desmembra operador e operandos"""
        if len(self.calculo.split()) < 3:
            raise Exception(
                '"erro": "entrada sem espaços entre operação e operandos"')
        return self.calculo.split()

    def str_p_int(self, lista):
        """Converte strings em inteiros"""
        lst = []
        try:
            lst.append(int(lista[0]))
        except TypeError as exc:
            raise Exception(
                '"erro": "primeiro dígito inválido"') from exc
        try:
            lst.append(int(lista[2]))
        except TypeError as exc:
            raise Exception(
                '"erro": "segundo dígito inválido"') from exc
        lst.insert(1, lista[1])
        return lst

    def __str__(self):
        """Formata """
        abre_chave = '{'
        fecha_chave = '}'
        return f'{abre_chave}"operacao": "{self.calculo}", "resultado": "{self.resultado}",\
             "data e hora": "{time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(time.time() - 10800))}"{fecha_chave}'


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


conta = Calculadora('5 + e')
