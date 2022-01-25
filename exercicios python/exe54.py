s = 0
cont = 0
cont2 = 2

for c in range(0, 3):
    n1 = int(input('Sua data de nascimento: '))
    ma = n1-2021
    if ma >= 18:
        cont += 1
        print('{} pessoas são maiores de idade: '.format(cont))
        print('{} Pessoas são menores de idade'.format(cont))
