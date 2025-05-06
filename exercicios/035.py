#### [Exercicio 035](exercicios/035.py)

'''Faça um Programa que peça um número correspondente a um determinado ano e em
seguida informe se este ano é ou não bissexto.'''

a = int(input('Digite um ano: '))

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print('É bissexto.')
        else:
            print('Não é bissexto.')
    else:
        print('É bissexto.')
else:
    print('Não é bissexto')