# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# Para formar um triângulo, a soma de dois lados deve ser maior que o terceiro lado.

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

print('\n Digite o comprimento de três retas e descubra se elas podem formar um triângulo.')
n1 = float(input('Digite o comprimento da primeira reta: '))
n2 = float(input('Digite o comprimento da segunda reta: '))
n3 = float(input('Digite o comprimento da terceira reta: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\033[1;32mAs retas podem formar um triângulo.\033[m')
else:
    print('\033[1;31mAs retas não podem formar um triângulo.\033[m')
