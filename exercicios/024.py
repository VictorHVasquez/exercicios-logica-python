
#### [Exercicio 024](exercicios/024.py)

'''Faça um Programa que leia três números e mostre o maior deles.'''

numeros = [10,9,7,4,39]
print(max(numeros))

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print('O maior numero é n1: ', n1)
elif n2 > n1 and n2 > n3:
    print('O maior numero é n2: ', n2)
elif n3>n1 and n3>n2:
    print('O maior numero é n3: ', n3)
else:
    print('O maior numero é: ',max(n1,n2,n3))
