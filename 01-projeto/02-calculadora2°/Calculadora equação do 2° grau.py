from math import sqrt
a = int(input('Qual o valor de "a" na equação: '))
b = int(input('Qual o valor de "b" na equação: '))
c = int(input('Qual o valor de "c" na equação: '))
delta = b**2 - 4*a*c
if delta >= 0:
    rdelta = sqrt(delta)
    t1 = -b + rdelta
    t2 = -b - rdelta
    t3 = 2*a
    x1 = t1/t3
    x2 = t2/t3
    if delta == 0:
        print('Só possui uma raiz: {:.2f}'.format(x1))
    else:
        print('As raizes dessa equação são: X1 = {:.2f} e X2 = {:.2f}'.format(x1, x2))
else:
    print('Não tem raiz real!')