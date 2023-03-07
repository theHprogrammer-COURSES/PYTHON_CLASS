# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...\n')
print(f'Nome com letras maiúsculas: {nome.upper()}')
print(f'Nome com lestras minúsculas: {nome.lower()}')
print(f'Quantidade de letras: {len(nome) - nome.count(" ")}')
print(f'Quantidade de letras no primeiro nome: {nome.find(" ")}')
