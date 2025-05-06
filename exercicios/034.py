import math

#### [Exercicio 034](exercicios/034.py)

''''Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax² + bx + c.

O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo
        grau e o programa não deve fazer pedir os demais valores,
        sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raízes reais.
        Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz
        real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais;
        informe-as ao usuário;'''

a = float(input('Informe o valor a: '))
if a == 0:
    print('Se a = 0 então a equação não é de segundo grau.')
else:
    b = float(input('Informe o valor b: '))
    c = float(input('Informe o valor c: '))


delta = b**2 - 4*a*c
if delta <0:
    print('Nenhuma raiz real.')
elif delta ==0:
    raiz = (-b) / (2 * a)
    print('Delta é zero. A raíz é: ', raiz)
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f'x1: {raiz1}',
          f'\nx2: {raiz2}' )# Duas raízes reais

