#### [Exercicio 030](exercicios/030.py)

'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita).

O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.

Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''

horaSalario = float(input('Digite o valor da hora trabalho: '))
horasMes = float(input('Digite a quantidade de horas mes de trabalho: '))
descontoIR = 0
descontoINSS = 10
porcentFGTS = 11
salarioBruto = horaSalario * horasMes

if salarioBruto <= 900:
    descontoIR = 0
elif salarioBruto > 900 and salarioBruto <= 1500:
    descontoIR = 5
elif salarioBruto > 1500 and salarioBruto <= 2500:
    descontoIR = 10
else:
    descontoIR= 20
totalDescontos = salarioBruto*(descontoIR/100) + salarioBruto*(descontoINSS/100)
salarioLiquido = salarioBruto - totalDescontos

print(f'Salário Bruto: ({horaSalario} * {horasMes}): R$ {salarioBruto}',
      f'\n(-) IR ({descontoIR}%): R$   {salarioBruto*(descontoIR/100)}',
      f'\n(-) INSS ({descontoINSS}%): R$  {salarioBruto*(descontoINSS/100)}',
      f'\nFGTS ({porcentFGTS}%): R$  {salarioBruto*(porcentFGTS/100)}',
      f'\nTotal de descontos: R$  {totalDescontos}',
      f'\nSalário Liquido: R$  {salarioLiquido}'
    )
