#### [Exercicio 016](exercicios/016.py)
import math

'''Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.'''


area = float(input('Digite a área em metros quadrados: '))
cobertura = area / 3
print(cobertura)
capacidadeLata = float(18)
custoLata = float(80)

if cobertura <= capacidadeLata:
    quantidadeLata = 1
    print(f'{area:.2f}m de área necessitará:\n{quantidadeLata} lata\nR${custoLata}')
else:
    quantidadeLata = math.ceil(cobertura/capacidadeLata)
    custoTotal =  quantidadeLata * custoLata
    print(f'{area:.2f}m de área necessitará:\n{quantidadeLata} latas\nR${custoTotal}')


