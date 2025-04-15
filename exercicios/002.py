"""
Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
"""
try:
    numeroEscolhido = int(input('Digite um numero: '))
except:
    print ('Numero Inválido')
else:
    print (f'O numero escolhido foi {numeroEscolhido}')
finally:
    print("\033[92m S.D.G\033[00m")