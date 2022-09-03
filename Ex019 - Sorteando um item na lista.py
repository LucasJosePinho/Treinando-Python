import random
al1 = (input('Escreva o nome do 1º Aluno: '))
al2 = (input('Escreva o nome do 2º Aluno: '))
al3 = (input('Escreva o nome do 3º Aluno: '))
al4 = (input('Escreva o nome do 4º Aluno: '))
n = random.sample(range(0,4),4)
print('O Aluno {} sortiou o número {}'.format(al1,n[0]))
print('O Aluno {} sortiou o número {}'.format(al2,n[1]))
print('O Aluno {} sortiou o número {}'.format(al3,n[2]))
print('O Aluno {} sortiou o número {}'.format(al4,n[3]))

