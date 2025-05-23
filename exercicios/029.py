#### [Exercicio 029](exercicios/029.py)

'''As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa que calculará os
reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante :
        aumento de 5% Após o aumento ser realizado,
    informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.'''

salario = float(input('Digite o salario: '))


if salario <= 280:
    aumento = 20
elif salario > 280 and salario <= 700:
    aumento = 15
elif salario > 700 and salario < 1500:
    aumento = 10
else:
    aumento = 5

novoSalario = salario * (aumento/100)+ salario
print(f'Salario atual: R${salario:.2f}',
      f'\nPorcentual a ser aplicado: {aumento}%',
      f'\nValor do aumento: R${(salario * (aumento/100)):.2f}',
      f'\nNova base salarial: R${novoSalario:.2f}'
      )
print('==============================================')