print("Calculo de área e tinta necessária")

cobertura_tinta = 2**2

altura = input('Digite a altura da parede: ')
altura = float(altura)

largura = input('Digite a largura da parede: ')
largura = float(largura)

area_parede = altura * largura
qtd_de_latas = area_parede / cobertura_tinta

print(f'Àrea da parede = {area_parede}m')
print(f"Latas de tinta necessárias para pintar a parede = {qtd_de_latas:.2f}")
