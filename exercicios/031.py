#### [Exercicio 031](exercicios/031.py)

'''Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.'''

n = int(input('Digite um numero de 1 a 7: '))

if n == 1:
    print('1 - Domingo')
elif n == 2:
    print('2 - Segunda-Feira')
elif n == 3:
    print('3 - Terça-Feira')
elif n == 4:
    print('4 - Quarta-Feira')
elif n == 5:
    print('5 - Quinta-Feira')
elif n == 6:
    print('6 - Sexta-Feira')
elif n == 7:
    print('7 - Sábado')
else:
    print('Valor inválido')

