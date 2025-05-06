'''#### [Exercicio 038](exercicios/038.py)

Faça um Programa para um caixa eletrônico.

O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas.

As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.

O programa não deve se preocupar com a quantidade de notas existentes na
máquina.

Exemplo 1:
Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2:
Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

valorSaque = int(input('Digite a o valor que deseja sacar em notas: '))
if valorSaque < 10:
    print('O valor mínimo é de 10 reais.')
elif valorSaque > 600:
    print('O Valor máximo é de 600 reais.')
else:
    valor = valorSaque
    notaCem = valorSaque // 100
    valor -= notaCem * 100
    notaCinquenta = valor // 50
    valor -= notaCinquenta * 50
    notaDez = valor // 10
    valor -= notaDez * 10
    notaCinco = valor // 5
    valor -= notaCinco * 5
    notaUm = valor
    print(f'Para sacar a quantia de {valorSaque} reais, o programa fornece:')

    if notaCem > 0:
        print(f'{notaCem} notas de cem')
    if notaCinquenta > 0:
        print(f'{notaCinquenta} notas de cinquenta')
    if notaDez > 0:
        print(f'{notaDez} notas de dez')
    if notaCinco > 0:
        print(f'{notaCinco} notas de cinco')
    if notaUm > 0:
        print(f'{notaUm} notas de um')

