nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')

print('Olá', nome, 'você tem', idade, 'anos')
print('Olá ' + nome + ' você tem ' + idade + ' anos')
print(f'Olá {nome} você tem {idade} anos')
print('Olá {} você tem {} anos'.format(nome, idade))

print('Olá', nome, 'você-tem', idade, 'anos', sep='-', end='!!!\n')
