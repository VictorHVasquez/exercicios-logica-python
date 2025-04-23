#### [Exercicio 027](exercicios/027.py)

'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

n1 = int(input('Digite o n1: '))
n2 = int(input('Digite o n2: '))
n3 = int(input('Digite o n3: '))

if n1 < n2 < n3:
    print(n1, n2, n3)
elif n2 < n1 < n3:
    print( n2, n1, n3)
elif n3 < n2 < n1:
    print(n3,n2,n1)
elif n2 < n3 < n1:
    print(n2, n3, n1)
elif n1 < n3 < n2:
    print(n1,n3,n2)




