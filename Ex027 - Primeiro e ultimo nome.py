nome = input('Digite seu nome completo: ')
sep = nome.split()
nome1 = sep[0]
num = len(sep)
nomeult = sep[num-1]
print("O primeiro nome é {} e o último é {}".format(nome1,nomeult))