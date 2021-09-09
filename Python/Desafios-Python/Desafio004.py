# Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo
# e todas as informações possíveis sobre ela.

n = input('Digite algo: ')
print('Qual tipo primitivo do valor: ', type(n))
print('Contém só espaços? ', n.isspace())
print('É um número? ', n.isnumeric())
print('Contém apenas caracteres decimais? ', n.isdecimal())
print('É alfabético? ', n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('Está em minúsculo? ', n.islower())
print('Está em maiúsculo? ', n.isupper())
print('Está captalizada? ', n.istitle())
