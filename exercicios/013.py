#### [Exercicio 013](exercicios/013.py)

'''Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7'''

altura = float(input('Digite a sua altura: '))
pesoIdealH = 72.7*altura - 58
pesoIdealM = 62.1*altura - 44.7

print(f'O peso ideal para essa altura é de:\n{pesoIdealH:.2f}Kgs para Homens,\n{pesoIdealM:.2f}Kgs para Mulheres.')

