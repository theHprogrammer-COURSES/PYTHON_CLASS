# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from time import sleep
from datetime import date

ano = int(input('Digite um ano para ver se ele é bissexto: '))

bissexto = False

if ano <= 0:
    ano = date.today().year
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    bissexto = True
    
print('\n\033[1;33mCalculando...')
sleep(2)

if bissexto:
    print(f'\033[1;34mO ano {ano} é bissexto\033[m')
else:
    print(f'\033[1;34mO ano {ano} não é bissexto\033[m')    
