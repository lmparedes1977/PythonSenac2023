from random import shuffle
from random import randint
from time import sleep

palavras = open('palavras.txt', 'r', encoding='utf-8')
lista_palavras = palavras.readlines()
lista_palavras = [palavra.rstrip().upper() for palavra in lista_palavras]
palavras.close()
num_palavra = randint(0, len(lista_palavras)-1)
palavra = list(lista_palavras[num_palavra])

shuffle(palavra)
palavra_embaralhada = ' '.join(palavra)

print('='*30)
print('JOGO DA PALAVRA EMBARALHADA'.center(30))
print('='*30)
print('Descubra que palavra é...\n')
sleep(3)
print(palavra_embaralhada)
print()


for i in range(6):
    palpite = input(f'Digite seu palpite [{6-i} tentativas]: ').upper().strip()
    if palpite == lista_palavras[num_palavra]:
        print(f'BINGO! A palavra é {lista_palavras[num_palavra]}')
        break
    else:
        print('Bela tentativa, mas não...')
else:
    print(
        f'Infelizmente não deu pra você... A palavra era {lista_palavras[num_palavra]}')
