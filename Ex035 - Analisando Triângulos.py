a = int(input('Digite o comprimento da reta 1 :'))
b = int(input('Digite o comprimento da reta 2 :'))
c = int(input('Digite o comprimento da reta 3 :'))

if b+c>a:
    print('Será formado um triângulo')
elif a+c>b:
    print('Será formado um triângulo')
elif a+b>c:
    print('Será formado um triângulo')
else:
    print('Não será formado um triângulo')
