# for
texto = input('Informe um texto: ')
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
# else:
    # print()

# Usando range()
# range(stop) -> range object
# range(start, stop[, step]) -> range object

print(end='\n\n')
print(list(range(10)))
print(end='\n\n')

for numero in range(0, 51, 5):
    print(numero, end=' ')

print(end='\n\n')

# While
opcao = 1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n\nOpção:  '))
    if opcao == 1:
        print('Sacando...\n')
    elif opcao ==2:
        print('Exibindo o extrato...\n')
# else:
    # print('Origado por usar o nosso sistema bancário, até logo')

# BREAK e CONTINUE

while True:
    numero = int(input('Informe um número: '))
    if numero == 10:
        break
    if numero % 2 == 0:
        continue # pula
    print(numero)

for numero in range(100):
    if numero % 2 == 0:
        continue # pula
    print(numero, end=' ')
