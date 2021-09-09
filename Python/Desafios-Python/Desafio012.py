# Faça um algortimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Informe o preço do produto:\nR$ '))
d = (p * 5) / 100
np = p - d
print('O desconto foi de R$ {}.'.format(d), end=' ')
print('O preço do produto com desconto é R$ {}.'.format(np))
