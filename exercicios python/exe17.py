from math import hypot
co = float(input('Digite o valor do primeiro cateto: '))
ca = float(input('Digite o valor do segundo cateto: '))
hip = hypot(co, ca)
print('A hipotenusa deste triangulo é: {}'.format(hip))