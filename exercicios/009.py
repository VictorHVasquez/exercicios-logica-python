#### [Exercicio 009](exercicios/009.py)

'''Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre
a temperatura em graus Celsius.
C = (5 * (F-32) / 9).'''

grauFarenheit = float(input('Digite a temperatura em Farenheit Fº: '))
grauCelsius = (5 * (grauFarenheit - 32) / 9)
print(f'{grauFarenheit:.2f}Fº equivale a {grauCelsius:.2f}Cº')

def converterTemperatura ():
    tempInput = float(input('Digite a tempuratura: '))
    whichMeasure = input('Escolha qual grau da temperatura "C" para celsius ou "F" para Farenheit: ')
    if whichMeasure == 'C':
        tempInput = (5 * (grauFarenheit - 32) / 9)
        print(f'{tempInput:.2f}Cº equivale a {grauFarenheit:.2f}Fº')
    elif whichMeasure == 'F':
        grauCelsius = (5 * (tempInput - 32) / 9)
        print(f'{tempInput:.2f}Fº equivale a {grauCelsius:.2f}Cº')
    else:
        print('Opcao incorreta, digite apenas "C" ou "F"')

converterTemperatura()
