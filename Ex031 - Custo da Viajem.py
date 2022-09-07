dist = int(input('Digite a distância em Km : '))
if (dist>200):
    print('O preço será de {}'.format(dist*0.5))
else:
    print(('O preço será de {}'.format(dist*0.45)))