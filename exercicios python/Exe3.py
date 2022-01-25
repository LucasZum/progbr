from typing import Optional


a = input('Digite algo: ')
print('Tipo primitivo: ',type(a))
print('é um numero ? ',a.isnumeric())
print('é uma letra ? ',a.isalpha())
print('só tem espaços ? ', a.isspace())
print('é sla ? ',a.isdigit())
print('esta em maiusculas ? ',a.isupper())
print('{} esta em minusculas ? '.format(a),a.islower())