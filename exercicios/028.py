#### [Exercicio 028](exercicios/028.py)

'''Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.

Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso.'''


turno = str(input('Digite a letra do turno que você estuda:\n'
                  'M-Matutino\n'
                  'V-Vespertino\n'
                  'N-Noturno\n')).upper()

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido')
