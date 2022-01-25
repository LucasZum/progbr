from time import sleep
from math import sqrt
print('=-='*7)
n1 = float(input('Digite o 1° Número: '))
n2 = float(input('Digite o 2° Número: '))
print('=-='*7)
op = 0
raiz = sqrt(n1)
while op != 8:
    op = int(input("""Oque quer fazer com os Números {:.0f}, {:.0f}:
    [ 1 ] Soma
    [ 2 ] Subtração
    [ 3 ] Multiplicação
    [ 4 ] Divisão
    [ 5 ] Raiz Quadrada do 1° Numero
    [ 6 ] Mostrar Maior
    [ 7 ] Novos Números
    [ 8 ] Fechar
    >>>>> """.format(n1,n2)))
    print('=-='*5)
    if op == 1:
        print('{:.0f} + {:.0f} = {}'.format(n1, n2, n1 + n2))
        print('=-='*5)
        sleep(5)
    elif op == 2:
        print('{:.0f} - {:.0f} = {}'.format(n1, n2, n1 - n2))
        print('=-='*5)
        sleep(5)
    elif op == 3:
        print('{:.0f} x {:.0f} = {}'.format(n1, n2, n1 * n2))
        print('=-='*5)
        sleep(5)
    elif op == 4:
        print('{:.0f} / {:.0f} = {}'.format(n1, n2, n1 / n2))
        print('=-='*5)
        sleep(5)
    elif op == 5:
        print('A raiz quadrada de {:.0f} é {:.2f}'.format(n1, raiz))
        sleep(5)
    elif op == 6:
        if n1 > n2:
            print('{:.0f} é maior que {:.0f} !'.format(n1, n2))
            print('=-='*7)
            sleep(5)
        if n2 > n1:
            print('{:.0f} é maior que {:.0f} !'.format(n2, n1))
            print('=-='*7)
            sleep(5)
    elif op == 7:
        print('=-='*8)
        n1 = float(input('Digite o 1° Número: '))
        n2 = float(input('Digite o 2° Número: '))
        print('=-='*8)
        sleep(5)
print('=-==-', 'FIM', '-==-=')