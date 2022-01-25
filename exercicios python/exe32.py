ano = int(input('Ano você quer saber se é bissexto: '))
if (ano % 4) == 0: #pq se a SOBRA da div for 0 então...
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} NÃO é bissexto!'.format(ano))