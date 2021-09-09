# int = 7 ; -4 ; 0 ; 9875 #
# float = 4.5 ; 0.076 ; -15.223 ; 7.0 #
# bool = True ; False #
# str= 'Olá' ; '7.5' ; '' #

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
s = n1 + n2
print('A soma do números é:', s)

# OU #

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
s = n1 + n2
print('A soma do números é: {}'.format(s))

# Colocando em Prática #

n = input('Digite um número: ')
print(type(n))

n = int(input('Digite um número: '))
print(type(n))

n = float(input('Digite um número: '))
print(n)

n = bool(input('Digite um número: '))
print(n)

n = input('Digite algo: ')
print(n.isnumeric())

n = input('Digite algo: ')
print(n.isalpha())

n = input('Digite algo: ')
print(n.isalnum())

n = input('Digite algo:')
print(n.isupper())

n = input('Digite algo:')
print(n.islower())

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
s = n1 + n2
print('A soma entre os números', n1, 'e', n2, 'é: {}'.format(s))

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
s = n1 + n2
print('A soma entre os números {} e {} é: {}'.format(n1, n2, s))
