# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

# O método hypot() retorna a hipotenusa de um triângulo retângulo.
from math import hypot

catOp = float(input('Digite o comprimento do cateto oposto: '))
catAd = float(input('Digite o comprimento do cateto adjacente: '))

# Opção 1 - Usando o método hypot()
hipo = hypot(catOp, catAd)

# Opção 2 - Usando a fórmula de Pitágoras
# hipo = (catOp ** 2 + catAd ** 2) ** (1/2)

print(f'O comprimento da hipotenusa é {hipo:.2f}')
