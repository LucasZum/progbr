#Exercício Python 15: Escreva um programa que pergunte a
#quantidade de Km percorridos por um carro alugado e a 
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.



kp = float(input('Quantidade de Km percorridos: '))
da = int(input('Por quantos dias o carro ficou alugado: '))
pr = (da * 60) + (kp * 0.15)
print('O preço total a ser pago é R${} '.format(pr))