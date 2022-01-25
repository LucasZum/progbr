casa = float(input('Valor da casa: '))
temp = float(input('Tempo para pagar (anos): '))
sal = float(input('Seu salario: '))
pre = casa/temp
temm = temp * 12
if sal>= (pre * 0.7):
    print('O valor de cada prestação sera em {:.0f} vezes de R${:.2f}'.format(temm, pre))
else:
    print('Você não esta qualificado para financiar a casa')

    
    