# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.

dias = int(input('Quantidade de dias alugados: '))
km =float(input('Quantidade de Km percorridos: '))

valorDia = 60
valorkm = 0.15

total = (dias * valorDia) + (km * valorkm)

print(f'O total a pagar é de R$ {total:.2f}')
