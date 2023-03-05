# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um número: '))

dobro = n * 2
triplo = n * 3
raizQuadrada = n ** (1/2)

print(f'\nO dobro de {n} é {dobro:.2f}')
print(f'O triplo de {n} é {triplo:.2f}')
print(f'A raiz quadrada de {n} é {raizQuadrada:.2f}')
