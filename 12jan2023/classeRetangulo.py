class Retangulo:
    def __init__(self, base, altura) -> None:
        self.__base = base
        self.__altura = altura

    def get_lados(self):
        return f'Base: {self.__base}, Altura: {self.__altura}'

    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura

    def area(self):
        return self.__altura * self.__base

    def perimetro(self):
        return self.__altura * 2 + self.__base * 2


a4 = Retangulo(17, 21)

print(a4.area())
print(a4.perimetro())
