#### [Exercicio 040](exercicios/040.py)

'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.'''

n = float(input('Digite um número: '))

inteiro = round(n)

if n - inteiro == 0:
    print('Numero é Inteiro.')
else:
    print('Numero é decimal.')
