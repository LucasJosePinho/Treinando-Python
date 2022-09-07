from operator import le

nc = input('Digite seu nome completo: ')
print(nc.upper())
print(nc.lower())
print('O nome possui {} letras'.format(len(nc.strip())))
lista = nc.split()
print('O primeiro nome possui {} letras'.format(len(lista[0])))
