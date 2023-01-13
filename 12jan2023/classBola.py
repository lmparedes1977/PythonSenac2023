

class Bola:
    def __init__(self, cor, circunferencia, material) -> None:
        self.__cor = cor
        self.__circ = circunferencia
        self.__mater = material

    def __str__(self) -> str:
        return f'A bola é {self.__cor}, {self.__circ} de circunferência e feita de {self.__mater}.'

    def get_cor(self):
        return self.__cor

    def set_cor(self, cor):
        self.__cor = cor


futimbas = Bola('Branca', 5, 'couro')
print(futimbas)

futimbas.set_cor('Preta')
print(futimbas.get_cor())
