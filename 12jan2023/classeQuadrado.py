

class Quadrado:
    def __init__(self, lado) -> None:
        self.__lado = lado

    def set_quadrado(self, lado):
        self.__lado = lado

    def get_quadrado(self):
        return f'Quadrado de lado {self.__lado}'

    def area(self):
        return self.__lado * self.__lado


qua = Quadrado(5)

print(qua.get_quadrado())

qua.set_quadrado(10)

print(qua.area())
