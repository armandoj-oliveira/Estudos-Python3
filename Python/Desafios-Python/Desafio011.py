# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma
# área de 2m².

w = float(input('Informe a largura da parede: \n'))
h = float(input('Iforme a altura da parede: \n'))
a = (w * h) / 2
print('O pintor gastará {:.2f} l.'.format(a))
