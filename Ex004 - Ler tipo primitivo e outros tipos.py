algo = input('Escreva alguma coisa: ')
print('A classe dele é {}'.format(type(algo)))
print('Ele é um número: {}'.format(algo.isnumeric()))
print('Ele é uma letra: {}'.format(algo.isalpha()))
print('Ele esta em letras minúsculas apenas: {}'.format(algo.islower()))
print('Ele é um número decimal: {}'.format(algo.isdecimal()))
print('Ele esta em letras maiusculas apenas: {}'.format(algo.isupper()))
print('Ele é alfanumérico: {}'.format(algo.isalnum()))
print('Ele tem um carctere Ascii: {}'.format(algo.isascii()))

