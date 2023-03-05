# Faça um algoritmo que leia a largura e a altura de uma parede metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura

# Consumo da tinta por metro quadrado
consumoTinta = 2

quantidadeTinta = area / consumoTinta

print(f'Para uma parede de {largura}x{altura} metros (area de {area} m²), será necessário {quantidadeTinta} litros de tinta.')
