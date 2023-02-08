from classes import Calculadora

print('='*30)
print('SUPER CALCULADORA'.center(30))
print('='*30)
print('SOMA SUBTRAÇÃO MULTIPLICAÇÃO\n   DIVISÃO E POTENCIAÇÃO')
while True:
    conta = input("Digite o cálculo desejado [num1 operação num2]: ")
    try:
        calculo = Calculadora(conta)
        print(calculo)
    except KeyboardInterrupt:
        print("Não adianta Ctrl-C")
    except:
        print("Falha no cálculo")
    continua = input("Deseja Continuar: [S/N]").upper()
    while continua not in 'SN':
        continua = input("INVALIDO. Entre com S ou N: ").upper()
    if continua == 'N':
        break
