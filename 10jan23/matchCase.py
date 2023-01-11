
var = int(input("Digita aê: "))

match var:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sábado")
    case _:
        print("Não sei")


match var:
    case 1 | 7:
        print("Finde")
    case 2 | 3 | 4 | 5 | 6:
        print("Dia útil")
    case _:
        print("Não sei")
