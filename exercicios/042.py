#### [Exercicio 042](exercicios/042.py)

'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".'''
def questionar_suspeito():
    print('Responsa Sim ou Não para as perguntas seguintes: ')
    pontuacao = 0
    r1 = input('Telefonou para a vítima? ').upper()
    if 'S' in r1:
        pontuacao += 1
    elif 'N' in r1:
        pass
    else:
        print('Valor inválido')
        return
    r2 = input('Esteve no local do crime? ').upper()
    if 'S' in r2:
        pontuacao += 1
    elif 'N' in r2:
        pass
    else:
        print('Valor inválido')
        return
    r3 = input('Mora perto da vítima? ').upper()
    if 'S' in r3:
        pontuacao += 1
    elif 'N' in r3:
        pass
    else:
        print('Valor inválido')
        return
    r4 = input('Devia para a vítima? ').upper()
    if 'S' in r4:
        pontuacao += 1
    elif 'N' in r4:
        pass
    else:
        print('Valor inválido')
    r5 = input('Já trabalhou com a vítima? ').upper()
    if 'S' in r5:
        pontuacao += 1
    elif 'N' in r5:
        pass
    else:
        print('Valor inválido')
        return
    print(pontuacao)
    return pontuacao

def classificar_suspeito(pontuacao):
    if pontuacao == 5:
        print('Assassino')
    elif pontuacao >=3 and pontuacao <=4:
        print('Cúmplice')
    elif pontuacao == 2:
        print('Suspeita')
    else:
        print('Inocente')

pontuacao = int(questionar_suspeito())
classificar_suspeito(pontuacao)

