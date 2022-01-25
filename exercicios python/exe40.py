n1 = float(input('Digite sua 1° Nota: '))
n2 = float(input('Digite sua 2° Nota: '))
med = (n1 + n2) / 2
if med > 7:
    print('APROVADO :D !!!')
elif med < 5:
    print('Você esta Reprovado :( estude mais !!!')
else:
    print('Você está em Recuperação -_-')