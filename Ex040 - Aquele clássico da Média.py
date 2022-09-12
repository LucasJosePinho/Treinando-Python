n1 = int(input('Digite a primeira nota '))
n2 = int(input('Digite a segunda nota '))
media = (n1+n2)/2
if (media<5):
    print('REPROVADO')
elif (media>6.9):
    print('APROVADO')
else:
    print('RECUPERAÇÃO')