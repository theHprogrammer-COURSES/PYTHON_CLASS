# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Primeiro nome: {nome.split()[0]}')
print(f'Último nome: {nome.split()[-1]}')
