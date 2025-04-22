import math

#### [Exercicio 017](exercicios/017.py)

'''Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas
e os respectivos preços em 3 situações:

    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor.
        Acrescente 10% de folga e sempre arredonde os valores para cima,
        isto é, considere latas cheias.'''

area = float(input('Digite a area a ser pintada em metros quadrados: '))
cobertura = area / 6
print(cobertura)
capacidadeLata = 18
rendimentoLata = cobertura * capacidadeLata
custoLata = 80
capacidadeGalao = 3.6
rendimentoGalao = cobertura * capacidadeGalao
custoGalao = 25

if cobertura <= capacidadeLata:
    quantidadeLata = 1
    custoTotal = 80
    print(f'Comprar {quantidadeLata} lata que custará R${custoTotal}')
else:
    quantidadeLata = math.ceil(cobertura/capacidadeLata)
    custoTotalLata = quantidadeLata * custoLata
    print(f'Comprar {quantidadeLata} latas que custarão R${custoTotalLata}')
print('ou')
if cobertura <= capacidadeGalao:
    quantidadeGalao = 1
    custoTotal =  25
    print(f'Comprar {quantidadeGalao} galao que custará R${custoTotal}')
else:
    quantidadeGalao = math.ceil(cobertura/capacidadeGalao)
    custoTotalGalao = quantidadeGalao * custoGalao
    print(f'Comprar {quantidadeGalao} galões que custarão R${custoTotalGalao}')
print('ou')
latas = math.floor(cobertura/capacidadeLata)
galoes = math.ceil(
    (cobertura % capacidadeLata) / capacidadeGalao
)

print(f'Latas: {latas}, '
      f'Galões: {galoes}\n'
      f'Custando R${((latas*custoLata)+(galoes*custoGalao))}')
