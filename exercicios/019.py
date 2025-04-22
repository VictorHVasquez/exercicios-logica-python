#### [Exercicio 019](exercicios/019.py)

'''Faça um Programa que peça dois números e imprima o maior deles.'''

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}.')
elif n1 < n2:
    print(f'{n2} é maior que {n1}.')
elif n1 == n2:
    print(f'São iguais')
else:
    pass