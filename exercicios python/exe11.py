alt = float(input('Qual a altura da parede ? '))
lar = float(input('Qual  a largura da parede ? '))
ar = lar*alt
tinta = ar/2
# ou (lar*alt)/2
print('Sera nescessario {:.2f} Litros de tinta'.format(tinta))