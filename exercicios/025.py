#### [Exercicio 025](exercicios/025.py)

'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print('O maior numero é n1: ', n1)
elif n2 > n1 and n2 > n3:
    print('O maior numero é n2: ', n2)
elif n3>n1 and n3>n2:
    print('O maior numero é n3: ', n3)
else:
    print('O maior numero é: ',max(n1,n2,n3))

if n1<n2 and n1<n3:
    print('O menor numero é n1: ', n1)
elif n2<n1 and n2<n3:
    print('O menor numero é n2: ', n2)
elif n3<n1 and n3<n2:
    print('O menor numero é n3: ', n3)
else:
    print('O menor numero é: ',min(n1,n2,n3))

