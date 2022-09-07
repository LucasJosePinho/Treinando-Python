vel = int(input('Digite a velocidade do carro: '))
if (vel>80):
    print('Atenção, você será multado em R${} por ultrapassar a velocidade maxima em {}Km/h'.format((vel-80)*7,(vel-80)))
else:
    print('Boa Viajem')