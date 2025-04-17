#### [Exercicio 008](exercicios/008.py)

'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

horaSalario = float(input('Digite sua hora/salario: '))
horaMes = float(input('Digite a quantidade de horas trabalhadas no mes: '))
salario = horaSalario*horaMes

print(f'Seu salario no mês foi: {salario}')