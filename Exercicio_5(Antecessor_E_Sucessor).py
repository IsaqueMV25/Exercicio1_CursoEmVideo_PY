print('Digite um número para mostrar seu sucessor e antecessor')

numero = input('Digite um número: ')
numero = int(numero)

antecessor = numero -1
sucessor = numero + 1

print(f'Numero escolhido: {numero}\n'
      f'Sucessor: {sucessor}\nAntecessor: {antecessor}')
