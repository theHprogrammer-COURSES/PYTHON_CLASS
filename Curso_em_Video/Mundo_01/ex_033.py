# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# Verifica se os números são iguais
if n1 == n2 == n3:
    print('Os números são iguais')
else:
    # Verifica qual é o maior número
    if n1 > n2 and n1 > n3:
        maior = n1
    elif n2 > n3:
        maior = n2
    else:
        maior = n3

    # Verifica qual é o menor número
    if n1 < n2 and n1 < n3:
        menor = n1
    elif n2 < n3:
        menor = n2
    else:
        menor = n3
    
    print(f'O maior número é {maior} e o menor é {menor}')
