# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

# O método input() é usado para receber dados do usuário. Ele retorna uma string.
# O método str() é usado para converter o valor recebido para string. Pode ser usado para garantir que o valor recebido é uma string.
nome = input(str('Qual é o seu nome?'))

# O formato de string f permite que você insira variáveis ​​em uma string usando um par de chaves {}.
print(f'Olá, {nome}, seja bem-vindo!')
