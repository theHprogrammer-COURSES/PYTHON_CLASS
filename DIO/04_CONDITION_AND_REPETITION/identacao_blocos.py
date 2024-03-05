def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print('Valor sacado!')
        print('Retire o valor na boca do caixa')
    print('Obrigado por ser nosso cliente, tenha um bom dia!')
    
sacar(100)

def depositar(valor):
    saldo = 500
    saldo += valor
    print('Valor depositado!')

depositar(100)
