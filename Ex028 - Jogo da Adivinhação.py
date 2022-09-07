nu = int(input('Digite um número entre 0 e 5: \n '))
from random import randint
pc = randint(0,5)
if (nu == pc):
    print('Parabéns você acertou')
else:
    print('Você errou tente novamente')