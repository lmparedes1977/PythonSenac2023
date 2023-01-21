

# class ListaLouca:
#     def __init__(self, lista) -> None:
#         self.lista = lista
#         pass

#     def __add__(self, alter):
#         if len(self.lista) > len(alter.lista):
#             return [self.lista[i] + alter.lista[i] for i in range(len(self.lista))]
#         else:
#             return [self.lista[i] + alter.lista[i] for i in range(len(alter.lista))]


# lista = [1, 2, 3] + [4, 5, 6]
# print(lista)

# lista1 = ListaLouca([1, 2, 3])
# lista2 = ListaLouca([4, 5, 6])
# print(lista1 + lista2)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista2 = list(filter(lambda x: x % 2 == 0, lista))

print(lista2)

lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista4 = tuple(filter(lambda x: x % 2, lista3))

print(lista4)
