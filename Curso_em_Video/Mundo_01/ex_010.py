# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1,00 = R$ 5,20

dinheiro = float(input('Quanto dinheiro você tem na carteira? R$ '))

dollarCotacao = 5.20
ConvertDollar = dinheiro / dollarCotacao

print(f'Com R$ {dinheiro:.2f} você pode comprar US$ {ConvertDollar:.2f}')
