# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))

sucessor = n + 1
antecessor = n - 1

print(f'Analisando o valor \033[1;31m{n}\033[m, seu antecessor é \033[1;33m{antecessor}\033[m e o seu sucessor é \033[1;34m{sucessor}\033[m.')
