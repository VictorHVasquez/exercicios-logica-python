#### [Exercicio 037](exercicios/037.py)

'''Faça um Programa que leia um número inteiro maior que 0 e menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros.

Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades

Testar com:
326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''

n = int(input('Digite um numero: '))

c = n // 100
print(c)
d = (n - (c * 100)) // 10
print(d)
u = n - c * 100 - d * 10
print(u)

if c > 1:
    msgCentena = f'{c} centenas'
else:
    msgCentena = f'{c} centena'
if d > 1:
    msgDezena = f'{d} dezenas'
else:
    msgDezena = f'{d} dezena'
if u > 1:
    msgUnidade = f'{u} unidades'
else:
    msgUnidade = f'{u} unidade'

if c > 0:
    if d > 0:
        if u > 0:
            print(f'{msgCentena}, {msgDezena} e {msgUnidade}.')
        else:
            print(f'{msgCentena} e {msgDezena}.')
    elif u > 0:
        print(f'{msgCentena} e {msgUnidade}.')
    else:
        print(f'{msgCentena}')
elif d > 0:
    if u > 0:
            print(f'{msgDezena} e {msgUnidade}.')
    else:
        print(f'{msgDezena}.')
else:
    print(f'{msgUnidade}.')