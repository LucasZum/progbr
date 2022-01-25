vel = int(input('Quantos KM você estava ? '))
mult = (vel - 80) * 7
if vel >= 81:
    print('Você levou uma multa no valor de R$ {},00'.format(mult))
else:
    print('Fique tranquilo, Voce não foi multado !!!')