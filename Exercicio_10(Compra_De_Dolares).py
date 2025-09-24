print('Compra de Dólar com Real')
dollar = 5.28

saldo = input('Saldo da carteira: ')
saldo = int(saldo)
resultado = saldo / dollar
resultado = int(resultado)
print(f'Com {saldo}R$ você consegue comprar: {resultado}$.')

