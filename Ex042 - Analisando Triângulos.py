a = int(input('Digite o comprimento da reta 1 :'))
b = int(input('Digite o comprimento da reta 2 :'))
c = int(input('Digite o comprimento da reta 3 :'))

if b+c>a:
  print('ok1')
elif a+c>b:
  print('ok2')
elif a+b>c:
  print('ok3')
else:
  print('Não será formado um triângulo')
if a == b and a == c:
   print('Equilátero')
elif a != b and a != c:
   print('Escaleno')
elif a == b or b == c:
   print('Isosceles')
