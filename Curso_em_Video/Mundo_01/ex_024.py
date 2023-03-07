# Crie um programa leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade: ')).strip().upper()

print(f'A cidade {cidade.title()} começa com "SantoSanto ok"? {cidade[:5] == "SANTO"}')
