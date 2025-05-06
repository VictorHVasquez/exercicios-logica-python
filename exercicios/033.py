#### [Exercicio 033](exercicios/033.py)

'''Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
    equilátero, isósceles ou escaleno.

Dicas:
    Três lados formam um triângulo quando a soma de
        quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;'''

l1 = float(input('Digite o tamanho do primeiro lado do triangulo: '))
l2 = float(input('Digite o tamanho do segundo lado do triângulo: '))
l3 = float(input('Digite o tamanho do terceiro lado do triângulo: '))

if (l1 + l2) <= l3 or (l2 + l3) <= l1 or (l3 + l1) <= l2:
    print('Não é um triangulo.')
else:
    if l1 == l2 == l3:
        print('Triangulo Equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triângulo Isósceles.')
    elif l1 != l2 != l3 != l1:
        print('Triângulo Escaleno.')
    else:
        print('Tipo não encontrado')




