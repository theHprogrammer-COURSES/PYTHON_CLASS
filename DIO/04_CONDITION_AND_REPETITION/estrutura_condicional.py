MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Informe sua idade: '))

# Primeira forma
if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH.')

if idade < MAIOR_IDADE:
    print('Ainda não pode tirar a CNH.')

# Segunda forma
if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH.')
else:
    print('Ainda não pode tirar a CNH.')

# Terceira forma
if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH.')
elif idade == IDADE_ESPECIAL:
    print('Pode fazer as aulas teóricas, mas não as práticas')
else:
    print('Ainda não pode tirar a CNH.')

# Forma com if aninhados
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso do cheque especial!')
    else:
        print('Não foi possível realizar o saque, saldo insuficiente!')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente!')
else:
    print('Sistema não reconheceu seu tipo de conta. Entre em contato com o seu gerente.')

# Forma com operador ternário
status = 'Sucesso' if saldo >= saque else 'Falha'
print(f'{status} ao realizar saque!')
