#### [Exercicio 022](exercicios/022.py)

'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = str(input('Digite uma letra: ')).upper()

if letra in ('A','E','I','O','U'):
    print('A letra é uma vogal')
else:
    print('A letra é uma consoante.')