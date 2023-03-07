# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

print('\033[1;33m-=-\033[m' * 10)
print('\033[1;33mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[1;33m-=-\033[m' * 10)

num = int(input('Número: '))
print('\033[1;33mPROCESSANDO...\033[m')

if num < 0 or num > 5:
    print('\033[1;31mNúmero inválido!\033[m')
else:
    num_pc = random.randint(0, 5)
    if num == num_pc:
        print('\033[1;32mVocê venceu!\033[m')
    else:
        print('\033[1;31mVocê perdeu!\033[m')
        print(f'\033[1;31mO número que eu pensei foi {num_pc}\033[m')
