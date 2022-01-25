s = 0
cont = 0
for c in range(0, 6):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        s += n1
        cont += 1
print('A some de {} numeros PARES é = {}'.format(cont, s))