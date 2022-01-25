from random import randint
print('Sou seu oponente, consegue acertar o numero que estou pensando ?!')
comp = randint(0, 10)
pal = 0
acertou = False
while not acertou:
    jog = int(input('Em que numero estou pensando: '))
    pal += 1
    if jog == comp:
        acertou = True
    else:
        if comp > jog:
            print('Mais...tente novamente: ')
        elif comp < jog:
            print('Menos...Tente de novo: ')
print('Voce acertou com {} tentativas parabens !!!'.format(pal))