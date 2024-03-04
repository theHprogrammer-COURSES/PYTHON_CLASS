# AND: tudo tem que ser verdadeiro
print(f'True and True: {True and True}')
print(f'True and False: {True and False}')
print(f'False and True: {False and True}')
print(f'False and False: {False and False}')

# OR: pelo menos um tem que ser verdadeiro
print(f'True or True: {True or True}')
print(f'True or False: {True or False}')
print(f'False or True: {False or True}')
print(f'False or False: {False or False}')

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp_1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(f'Expressão 1: {exp_1}')

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(f'Expressão 2: {exp_2}')

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(f'Expressão 3: {exp_3}')
