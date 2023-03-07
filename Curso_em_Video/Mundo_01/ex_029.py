# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual a velocidade do carro em (Km/h)? '))
valorMulta = 7

if velocidade > 80:
    multa = (velocidade - 80) * valorMulta
    print('\033[31mMultado!\033[m')
    print(f'\033[31mO valor da multa é de R${multa:.2f}\033[m')
else:
    print('\033[32mDentro do limite de velocidade! Dirija com segurança!\033[m')