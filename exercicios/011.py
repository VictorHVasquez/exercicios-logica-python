#### [Exercicio 011](exercicios/011.py)

'''Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo.
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.'''

def calcularNumeros ():
    aInt = int(input('Digite o primeiro numero inteiro: '))
    bInt = int(input('Digite o segundo numero inteiro: '))
    cReal = float(input('Digite um numero Real: '))
    
    primeiraEquacao = (aInt*2) * (bInt/2)
    segundaEquacao = (aInt*3) + cReal
    terceiraEquacao = cReal**3

    print(f'''Resultado Primeira Equacao: {primeiraEquacao}\nResultado Segunda Equacao: {segundaEquacao:.2f}\nResultado Terceira Equacao: {terceiraEquacao:.2f}''')
    
calcularNumeros()


