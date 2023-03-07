# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'O número {num} é \033[1;32mPAR\033[m')
else:
    print(f'O número {num} é \033[1;31mÍMPAR\033[m')
