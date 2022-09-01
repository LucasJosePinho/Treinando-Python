# Largura e Altura / Área = Largura*Altura / Cda litro de tinta é 2m²
larg = int(input('Digite a Altura: '))
alt = int(input('DIgite a Largura: '))
print('A Área é de {}m²'.format(larg*alt))
print('A quantidade de tinta necessária será de {:2}m²'.format((alt*larg)/2))