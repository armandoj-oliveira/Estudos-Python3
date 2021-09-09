# Escreva um programa que leia um valor em metros e o exiba convertendo em centímetros ou milímetros.

n = float(input('Digite o valor desejado em metros.\n'))
cm = n * 100
mm = n * 1000
print('Em centímetros fica: {}cm\nEm milímetros fica: {}mm'.format(cm, mm))
