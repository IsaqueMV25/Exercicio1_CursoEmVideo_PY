from math import sqrt

print('Digite um número para saber o dobro, triplo e a sua raiz quadrada')
numero = input('Digite o número: ')
numero = int(numero)

dobro = numero * 2
triplo = numero * 3
raiz = sqrt(numero)

print(f'O dobro de {numero} = {dobro}\n' \
f'O Triplo de {numero} = {triplo}\n' \
f'A raiz de {numero} = {raiz}')
