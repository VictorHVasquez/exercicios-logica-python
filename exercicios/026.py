#### [Exercicio 026](exercicios/026.py)

'''Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

p1 = float(input('Digite o preco do produto 1: '))
p2 = float(input('Digite o preço do produto 2: '))
p3 = float(input('Digite o preço do produto 3: '))

if p1 < p2 and p1 < p3:
    print('Compre o Produto 1.')
if p2 < p1 and p2 < p3:
    print('Compre o Produto 2.')
if p3 < p1 and p3 < p2:
    print('Compre o Produto 3.')
