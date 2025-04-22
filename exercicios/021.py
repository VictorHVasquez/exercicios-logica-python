#### [Exercicio 021](exercicios/021.py)

'''Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

sexo = str(input('Digite o sexo, M para Masculino e F para Feminino: '))

if sexo == 'M' or sexo == 'm':
    print('M - Masculino.')
elif sexo == 'F' or sexo == 'f':
    print('F - Feminino.')
else:
    print('Sexo Inválido')

