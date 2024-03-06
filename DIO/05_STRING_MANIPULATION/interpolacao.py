nome = 'João'
idade = 30
profissao = 'Programador'
linguagem = 'Python'

dados = {"nome": "João", "idade": 30}

PI = 3.14159

# OLD STYLE
print('Nome: %s Idade: %d' % (nome, idade))

# FORMAT STYLE
print('Nome: {} Idade: {}'.format(nome, idade))
print('Nome: {1} Idade: {0}'.format(idade, nome))
print('Nome: {1} Idade: {0} Nome: {1} {1}'.format(idade, nome))
print('Nome: {nome} Idade: {idade}'.format(idade=idade, nome=nome))
print('Nome: {name} Idade: {age} Idade: {age} {name}'.format(age=idade, name=nome))
print('Nome: {nome} Idade: {idade}'.format(**dados))

# f-string
print(f'Nome: {nome} Idade: {idade}')
print(f'PI = {PI}')
print(f'PI = {PI:.0f}')
print(f'PI = {PI:.2f}')
print(f'PI = {PI:.10f}')
