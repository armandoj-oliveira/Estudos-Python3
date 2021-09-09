# Faça um programa que leia um número inteiro e mostra na tela o seu sucessor e seu antecessor

n = int(input('Digite um número para saber seu sucessor e seu antecessor.\n '))
s = n + 1
a = n - 1
print('O sucessor de {} é {}.'.format(n, s), end=' ')
print('O antecessor de {} é {}'.format(n, a))
