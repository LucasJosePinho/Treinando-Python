casa = int(input('Digite o valor da Casa: '))
sala = int(input('Digite o salário do comprador: '))
id = int(input('Digite em quantos anos ele vai pagar: '))
parcela = (casa/(id*12))
if ((sala*0.3)<parcela):
    print('Infelizmente seu empréstimo não vou aprovado tente novamente mais tarde')
else:
    print('Parabén seu empréstimo foi aprovado \n O valor da parcela será de {}'.format(parcela))