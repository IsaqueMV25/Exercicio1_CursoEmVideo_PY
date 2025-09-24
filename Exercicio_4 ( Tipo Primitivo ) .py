print('Dados da entrada')
entrada = input('Digite algo: ')

print(f'A entrada ({entrada}) é do tipo: {type(entrada)}')

print('Mais informações:')
print(f'Só tem números? {entrada.isnumeric()}')
print(f'Só tem letras? {entrada.isalpha()}')
print(f'Possui Letras ou números? {entrada.isalnum()}')
print(f'É um espaço? {entrada.isspace()}')
print(f'Só tem letras minusculas? {entrada.islower()}')
print(f'Só tem letras maiúsculas? {entrada.isupper()}')
print(f'É um Título? {entrada.istitle()}')
