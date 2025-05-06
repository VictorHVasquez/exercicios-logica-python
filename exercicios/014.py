#### [Exercicio 014](exercicios/014.py)

'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
o rendimento diário de seu trabalho.

Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa
de R$ 4,00 por quilo excedente.

João precisa que você faça um programa que leia a variável peso
(peso de peixes) e calcule o excesso.

Gravar na variável excesso a quantidade de quilos além do limite
e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.'''

'''regulamentoPesoSP = float(50)
multa = float(4)

pesoPescado = float(input('Digite o peso de peixes: '))

if pesoPescado > regulamentoPesoSP:
    excedente = pesoPescado - regulamentoPesoSP
    cobrancaMulta = excedente * multa
    print(f'O excedente foi de {excedente:.2f}Kg\nO valor da multa será de: R${cobrancaMulta:.2f}.')
else:
    print('Não haverá multa, peso abaixo do excedente. ')'''


class Peixe:
    regulamentoPesoSP = float(50)
    multa = float(4)
    def __init__(self, pesoPescado):
        self.pesoPescado = pesoPescado

    def show(self):
        print('Peso Limite SP: ', Peixe.regulamentoPesoSP, 'Valor multa por KG excedente SP: ', Peixe.multa, 'Peso medido: ', self.pesoPescado)

    def calcula_multa(self):
        if self.pesoPescado > Peixe.regulamentoPesoSP:
            excedente = self.pesoPescado - Peixe.regulamentoPesoSP
            cobrancaMulta = excedente * Peixe.multa
            print(f'O excedente foi de {excedente:.2f}Kg\nO valor da multa será de: R${cobrancaMulta:.2f}.')
        else:
            somaPeso=self.pesoPescado - Peixe.regulamentoPesoSP
            print(f'Não haverá multa, peso {somaPeso:.2f}Kg abaixo do excedente. ')
    @classmethod
    def mudar_limite_regulamento_sp(cls,novo_peso_limite:float):
        cls.regulamentoPesoSP = novo_peso_limite
    @classmethod
    def mudar_valor_multa_sp(cls,novo_valor_multa:float):
        cls.multa = novo_valor_multa

p0 = Peixe(float(input('Digite o peso de peixes: ')))
p0.show()
Peixe.mudar_limite_regulamento_sp(60)
p0.show()
Peixe.mudar_valor_multa_sp(6)
p0.show()
p0.calcula_multa()
p1 = Peixe(float(input('Digite o peso de peixes: ')))
p1.show()
p1.calcula_multa()


