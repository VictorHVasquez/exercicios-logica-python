#### [Exercicio 043](exercicios/043.py)

'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
        até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro
    Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''


litros = float(input('Digite a quantidade de litros: '))
precoAlcool = 1.90
precoGasolina = 2.5

if litros <= 20:
    precoAlcool *= 0.97
    precoGasolina *= 0.96
elif litros > 20:
    precoAlcool *= 0.95
    precoGasolina *= 0.94
else:
    print('erro')

valorAlcool = litros * precoAlcool
valorGasolina = litros * precoGasolina

print(f'Litros: {litros}\n'
      f'A-álcool - Preço: R${precoAlcool:.2f} - Valor: R${valorAlcool:.2f}\n'
      f'G-gasolina - Preço: R${precoGasolina:.2f} - Valor: R${valorGasolina:.2f}\n')

