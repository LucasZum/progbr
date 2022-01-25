nas = int(input('Ano de nascimento: '))
idade = 2021 - nas
idadep = idade - 18
idadef = (idade - 18) * -1
if idade == 18:
    print('Esta na hora de você se alistar !!!')
elif idade > 18:
    print('Ja passou da hora, voce deveria ter se alistado à {} anos atrás !!!'.format(idadep))
elif idade == 17:
     print('Fique tranquilo, você só devera se alista daqui à {} ano !!!'.format(idadef))
elif idade == 19:
     print('Ja passou da hora, voce deveria ter se alistado à {} ano atrás !!!'.format(idadep))
else:
    print('Fique tranquilo, você só devera se alista daqui à {} anos !!!'.format(idadef))