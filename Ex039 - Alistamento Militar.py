id = int(input('Digite seu ano de nascimento: '))
id = 2022 - id
if (id<18):
    print('Ele ainda vai se alistar')
elif (id>18):
    print('Ele já si alistou')
else:
    print('Já é hora de se alistar')