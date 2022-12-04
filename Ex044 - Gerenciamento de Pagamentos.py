prod = int(input('Digite o preço do produto:'))
pag = int(input('Selecione a forma de pagamento 
abaixo:\n|--------------------|\n|1 - A vista/cheque\n|2 
- A vista no cartão\n|3 - cartão em 2x\n|4 - cartão 3x 
ou mais\n|--------------------|\nOpção: '))
if pag ==1:
    print('O valor total do produto será: {}'.format
(prod-(prod/10)))
elif pag==2:
    print('O valor total do produto será: {}'.format
(prod-((prod*5)/100)))
elif pag==3:
    print('O valor total do produto será: {}'.format
(prod))
elif pag==4:
    print('O valor total do produto será: {}'.format(prod
+(prod/20)))
else:
    print('Número inválido')
