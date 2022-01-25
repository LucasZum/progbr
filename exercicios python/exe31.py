des = float(input('Digite a distancia da viagem (Em KM): '))
p1 = des*0.50
p2 = des*0.45
if des <= 200:
    print('O preço será de R${}'.format(p1))
else:
    print('O preço será de R${}'.format(p2))