#Ciar lista de alunos e sortear um deles

from random import choice
a = str(input('Digite o nome do aluno: '))
b = str(input('Digite o nome do aluno: '))
c = str(input('Digite o nome do aluno: '))
d = str(input('Digite o nome do aluno: '))
lista = [a, b, c, d] # couchte para criar a lista
escolhido = choice(lista) # choice para escolher aleatorio dentro de (lista)
print('o aluno escolhido foi {}'.format(escolhido))