#### [Exercicio 004](exercicios/004.py)

'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''

nota1 = float(input('Digite o valor da primeira prova:'))
nota2 = float(input('Digite o valor da segunda prova: '))
nota3 = float(input('Digite o valor da terceira prova: '))
nota4 = float(input('Digite o valor da quarta prova: '))
somaNotas = nota1 + nota2 + nota3 + nota4

media = somaNotas/4

print(f'A media das notas e: {media:.2f}')

