soma = 0
med = 0
maiorh = 0
nomev = ''
for p in range(1, 5):
    print('----- {}a PESSOA -----'.format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
        maiorh = idade
        nomev = nome
    if sexo in 'mM' and idade > maiorh:
        maiorh = idade
        nomev = nome

med = soma / 4
print('A média de idade do grupo é de {} anos'.format(med))
print('O nome do mais velho tem {} anos e se chama {}'.format(maiorh, nomev))

