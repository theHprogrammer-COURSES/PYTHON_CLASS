# Escreva um programa que converta uma temperatura digitada em °C para °F.

tempC = float(input('Temperatura em °C: '))

tempF = (tempC * 9/5) + 32
tempK = tempC + 273.15

print(f'Temperatura em °C: {tempC:.2f}')
print(f'Temperatura convertida em °F: {tempF:.2f}')
print(f'Temperatura convertida em °K: {tempK:.2f}')
