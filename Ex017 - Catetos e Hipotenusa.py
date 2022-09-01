#comprimento CO e CA // Calcule H
#sen = CO/H | cos = CA/H | tg = CO/CA | H²=CA²+CO²
CO = int(input('Digite o Cateto Oposto: '))
CA = int(input('Digite o Cateto Adjacente: '))
print('A hipotenusa é igual a {:.2}'.format((CO**2+CA**2)**(1/2)))
