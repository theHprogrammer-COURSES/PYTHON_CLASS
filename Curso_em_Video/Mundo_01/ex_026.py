# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

texto = str(input('Digite uma frase: ')).strip()

print(f'Quantidade de vezes que a letra "A" aparece: {texto.upper().count("A")}')
print(f'Primeira posição da letra "A": {texto.upper().find("A")+1}')
print(f'Última posição da letra "A": {texto.upper().rfind("A")+1}')
