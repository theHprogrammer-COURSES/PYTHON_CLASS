# Faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo e todas as informações possíveis sobre ela.

algo = input('Digite algo: ')

print(f'Tipo primitivo: {type(algo)}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É decimal? {algo.isdecimal()}')
print(f'É dígito? {algo.isdigit()}')
print(f'É minúsculo? {algo.islower()}')
print(f'É maiúsculo? {algo.isupper()}')
print(f'Esta capitalizada? {algo.istitle()}')
print(f'É um espaço? {algo.isspace()}')
