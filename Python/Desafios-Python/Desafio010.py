# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
# ela pode comprar. Considere US$ 1.00 = R$ 3,27

r = float(input('Informe quantos reias tem na sua carteira:\nR$ '))
u = r / 3.27
print('Você poderá comprar US$ {:.2f} com R$ {:.2f}'.format(u, r))
