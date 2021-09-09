# Crie um algoritmo que leia um número e mostra o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número para saber seu dobro, triplo e sua raiz quadrada.\n'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro é {}, o triplo é {} e a raiz quadrada é {}.'.format(d, t, r))
