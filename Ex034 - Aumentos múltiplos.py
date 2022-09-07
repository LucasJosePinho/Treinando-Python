sal = int(input('Digite o salário: '))
if sal>1250:
    print('O saláio de R${} será aumentado em R${} totalizando R${}'.format(sal,sal*0.1,sal+(sal*0.1)))
else:
    print('O saláio de R${} será aumentado em R${} totalizando R${}'.format(sal,sal*0.15,sal+(sal*0.15)))