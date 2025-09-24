linha = '=' * 45

print(linha)
print('PRODUTO COM DESCONTO'.center(45))
print(linha)

nome_produto = input("Digite o nome do produto: ")
valor_produto = input('Digite o valor do produto: ')
valor_produto = float(valor_produto)
valor_atualizado = valor_produto - (valor_produto * 0.05)

print(linha)
print(f'Produto: {nome_produto}\n'
      f'Valor: {valor_produto} R$')

print(f'Valor com 5% de desconto: {valor_atualizado:.2f} R$')
print(linha)
