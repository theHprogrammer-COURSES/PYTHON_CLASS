saldo = 1000
limite = 1000

print(saldo is limite)  # False
print(f'id(saldo): {id(saldo)}')
print(f'id(limite): {id(limite)}')

limite = 500

print(saldo is not limite)  # True
print(f'id(saldo): {id(saldo)}')
print(f'id(limite): {id(limite)}')
