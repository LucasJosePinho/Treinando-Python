a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if (a<b and a<c):
    print('Menor = a')
elif (b<a and b<c):
    print('Menor = b')
elif (c<a and c<b):
    print('Menor = c')

if (a>b and a>c):
    print('Maior = a')
elif (b>a and b>c):
    print('Maior = b')
elif (c>a and c>b):
    print('Maior = c')

