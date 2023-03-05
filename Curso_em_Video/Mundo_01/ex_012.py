# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

precoProduto = float(input('Preço do produto: '))

# Porcentagem de desconto
desconto = 0.05

novoPreco = precoProduto * (1 - desconto)

print(f'O produto que custava R$ {precoProduto:.2f}, na promoção com desconto de 5% vai custar R$ {novoPreco:.2f}')
