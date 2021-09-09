# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

est = input('Qual o nome do estudante?\n')
n0 = int(input('Quantas notas serão lidas?\n'))
n1 = float(input('Digite a primeira nota do estudante.\n'))
n2 = float(input('Digite a segunda nota do estudante:\n'))
media = (n1 + n2) / n0
print('O {} teve {} na média.'.format(est, media))
