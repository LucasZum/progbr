n1 = int(input('Digite o 1° numero: '))
n2 = int(input('Digite o 2° numero: '))
if n1 > n2:
    print('O numero {} é maior que o {} '.format(n1, n2))
elif n2 > n1:
    print('O numero {} é maior que o {} '.format(n2, n1))
else:
    print('Não tem numero maior: {} = {} '.format(n1, n2))