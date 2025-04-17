#### [Exercicio 007](exercicios/007.py)

'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro
desta área para o usuário.'''

solicitarMedidaQuadrado = float(input('Digite a area a largura ou altura do quadrado: '))
calcularAreaQuadrado = solicitarMedidaQuadrado**2

print(f'A área do quadrado é: {calcularAreaQuadrado:.2f} \nE o dobro da área é: {calcularAreaQuadrado*2:.2f}')