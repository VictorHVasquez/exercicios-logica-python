#### [Exercicio 010](exercicios/010.py)

'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre
em graus Farenheit.'''

grauCelsius = float(input('Digite a temperatura em Celsius Cº: '))
grauFarenheit = float(1.8 * grauCelsius + 32) 
print(f'{grauCelsius:.2f}Cº equivale a {grauFarenheit:.2f}Fº')