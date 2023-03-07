# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Salário do funcionário: '))

aumento = 0.15

novoSalario = salario * (1 + aumento)

print(f'O funcionário que ganhava R$ {salario:.2f}, com 15% de aumento, passa a receber R$ {novoSalario:.2f}')
