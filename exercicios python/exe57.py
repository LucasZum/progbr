sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0] #para pegar apenas a primeira letra do que for digitado
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, favor enformar seu sexo [M/F]: ')).strip().upper()[0]
print('sexo {} registrado com suscesso !'.format(sexo))