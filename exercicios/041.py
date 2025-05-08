#### [Exercicio 041](exercicios/041.py)

'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
operação ele deseja realizar.

O resultado da operação deve ser acompanhado de uma
frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.'''

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

operacao = input('Digite qual operacao deseja realizar: ')

if 'div' in operacao or '/' in operacao:
    resultado = n1 / n2
if 'mult' in operacao or '*' in operacao:
    resultado = n1 * n2
if 'sub' in operacao or '-' in operacao:
    resultado = n1 - n2
if 'som' in operacao or '+' in operacao:
    resultado = n1 + n2

print(f'O resultado da operação é: {resultado}')

if (resultado // 1) % 2 == 0:
    print('Par')
else:
    print('ímpar')

if resultado >= 0:
    print('Positivo')
else:
    print('Negativo')

if resultado % 1 == 0:
    print('Inteiro')
else:
    print('Decimal')