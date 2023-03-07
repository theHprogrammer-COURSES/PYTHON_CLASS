# Escreva um programa que leia um valor em metros e o exima convertido em centímetros e milímetros.

mValue = float(input('Informe um valor em metros para ser convertido: '))

kmValue = mValue / 1000
hmValue = mValue / 100
damValue = mValue / 10
dmValue = mValue * 10
cmValue = mValue * 100
mmValue = mValue * 1000

print(f'Valor em metros: {mValue}m\n')
print('Conversão para:')
print(f'Quilômetros: {kmValue}km')
print(f'Hectômetros: {hmValue}hm')
print(f'Decâmetros: {damValue}dam')
print(f'Decímetros: {dmValue}dm')
print(f'Centímetros: {cmValue}cm')
print(f'Milímetros: {mmValue}mm')
