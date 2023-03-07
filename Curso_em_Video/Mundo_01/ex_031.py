# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

from time import sleep

dist = float(input('\033[1;33mQual a distância (Km) da sua viagem? '))

if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45

print('\n\033[1;33mCalculando...')
sleep(2)

print(f'\033[1;34mO valor da sua passagem é R${valor:.2f}\033[m')