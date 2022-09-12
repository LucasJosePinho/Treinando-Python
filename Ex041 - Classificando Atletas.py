id = int(input('Digite a seu ano de nascimento: '))
id = 2022 - id
if (id<10):
    print('MIRIM')
elif (id<15):
    print('INFANTIL')
elif (id<20):
    print('JUNIOR')
elif (id<21):
    print('SENIOR')
else:
    print('MASTER')
