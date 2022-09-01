# carro usado:300 / carro novo:500 / Tempo por dia:
car = int(input('Qual carro você gostaria de usar:\n 1-Usado 2-Novo :'))

if (car==1):
    car = car*300
else:
    car = car*500

temp = int(input('Por quantos dias você quer aluga-lo: '))
print('O valor total do aluguel do carro por {} dias será de R${}'.format(temp,car*temp))
