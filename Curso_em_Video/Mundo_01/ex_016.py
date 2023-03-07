# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

# O método trunc() retorna o valor inteiro de um número real.
from math import trunc

num = float(input('Digite um número: '))

# Opção 1 - Usando o método trunc()
print(f'O número {num} tem a parte inteira {trunc(num)}')

# Opção 2 - Usando o método int()
#print(f'O número {num} tem a parte inteira {int(num)}')
