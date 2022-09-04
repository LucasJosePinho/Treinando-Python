# desconto de 5%
pc = float(input('Digite o Valor do produto para aplicar o Desconto de 5%: '))
print('O produto de R${} terá um desconto de R${}'.format(pc,(pc*5/100)))
print('O novo valor do produto será de R${}'.format((pc-pc*5/100)))