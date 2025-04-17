#### [Exercicio 006](exercicios/006.py)
import math

'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''


solicitarRaio = float(input('Digite o Raio: '))
areaCirculo = math.pi * math.pow(solicitarRaio,2)

print(f'A área do circulo é: {areaCirculo:.2f}')

def calcularAreaCirculo (a):
    areaCirculo = math.pi * math.pow(float(a),2)
    return areaCirculo

print(calcularAreaCirculo(solicitarRaio))