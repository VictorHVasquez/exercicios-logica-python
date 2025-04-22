#### [Exercicio 012](exercicios/012.py)

'''Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58'''

altura = float(input('Digite a sua altura: '))
pesoIdeal = 72.7*altura - 58

print(f'Seu peso ideal é de {pesoIdeal:.2f}Kgs')