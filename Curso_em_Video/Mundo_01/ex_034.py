# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário do funcionário: '))

if salario <= 1250:
    aumento = salario * 1.15
else:
    aumento = salario * 1.10
    
print(f'\033[1;32mO salário do funcionário é R${salario:.2f} e com o aumento passa a ser R${aumento:.2f}\033[m') 
