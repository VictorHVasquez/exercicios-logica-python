#### [Exercicio 015](exercicios/015.py)

'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.'''

class Colaborador:
    empresa = 'ADP'
    count = 0
    porcentIR = 0.11
    porcentINSS = 0.08
    porcentSindicato = 0.05

    def __init__(self,nome,salarioHora=9.49,horasMes=160):
        Colaborador.count = Colaborador.count + 1
        self.nome = str(nome)
        self.salarioHora = float(salarioHora)
        self.horasMes = float(horasMes)
    
    def show(self):
        print(Colaborador.count, self.nome, self.empresa, self.salarioHora, self.horasMes)
    def calcular_salario(self):
        salarioBruto = self.salarioHora*self.horasMes
        descontoIR = Colaborador.porcentIR * salarioBruto
        descontoINSS = Colaborador.porcentINSS * salarioBruto
        descontoSindicato = Colaborador.porcentSindicato * salarioBruto
        salarioLiquido = salarioBruto - descontoIR - descontoINSS - descontoSindicato
        print('========================')
        print(f'+ Salário Bruto : R${salarioBruto:.2f}\n- IR (11%) : R${descontoIR:.2f}\n- INSS (8%) : R${descontoINSS:.2f}\n- Sindicato (5%) : R${descontoSindicato:.2f}\n= Salário Líquido : R${salarioLiquido:.2f}')
        print('========================\n')


def cadastrar_colaborador():
    nome = str(input('Digite seu nome: '))
    salarioHora = float(input('Digite o quanto voce ganha por hora: '))
    horasMes = float(input('Digite quantas horas trabalhadas por mês:'))
    return nome,salarioHora,horasMes
dados = cadastrar_colaborador()
print(dados)
print(*dados)
c0 = Colaborador(*dados)
print(c0)
c0.show()
c0.calcular_salario()
