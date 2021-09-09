# Operadores Aritméticos

#   +   Adição  (5 + 2 == 7)                    *   Multiplicação   (5 * 2 == 10)
#   -   Subtração   (5 - 2 == 3)                /   Divisão    (5 / 2 == 2.5)
#   %   Resto da Divisão   (5 % 2 == 1)         //  Dvisião Inteira    (5 // 2 == 2)
#   **  ou pow(x,y) Potência    (5 ** 2 == 25)  x**(1/y) Raíz

# ------------------------------------------------------------------------------------- #

# Ordem de Prescendência

# Primeiro = ()        Terceiro = * / // %
# Segundo = **         Quarta = + -

# ------------------------------------------------------------------------------------- #

# Exercícios

nome = input('Qual é o seu nome? ')
print('Prazer me te conhecer {:20}!'.format(nome))
print('Prazer me te conhecer {:>20}!'.format(nome))
print('Prazer me te conhecer {:<20}!'.format(nome))
print('Prazer me te conhecer {:^20}!'.format(nome))
print('Prazer me te conhecer {:=^20}!'.format(nome))

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('O valor da soma é: {}'.format(n1 + n2))

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
re = n1 % n2
di = n1 // n2
p = n1 ** n2
r = n1 ** n2 / 2
print("O valor da soma é {}, a subtração é {}, o produto é {} e a divisão é {} ".format(a, s, m, d), end='  ')
print('O valor do resto da divisão é {} e da divisão inteira é {} '.format(re, di), end='  ')
print('O valor da potência é {} e raíz quadrada de {} e {} é: {:.2f}'.format(p, n1, n2, r))
