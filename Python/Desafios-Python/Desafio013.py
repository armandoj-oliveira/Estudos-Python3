# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o salario: "))
aumento = salario + (salario * 15/100)
print('O salário atual é de {}'.format(aumento))
