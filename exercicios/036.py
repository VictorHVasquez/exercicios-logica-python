#### [Exercicio 036](exercicios/036.py)

'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma
é uma data válida.'''

'''Common format codes include:
%Y: 4-digit year
%y: 2-digit year
%m: Month as a zero-padded number (01-12)
%B: Full month name
%b: Abbreviated month name
%d: Day of the month as a zero-padded number (01-31)
%A: Full weekday name
%a: Abbreviated weekday name
%H: Hour (00-23)
%I: Hour (01-12)
%M: Minute (00-59)
%S: Second (00-59)
%p: AM or PM'''
from datetime import datetime

data = input('Digite uma data em formato dd/mm/aaaa: ')
#date_format = '%d/%m/%Y'

#data_object = datetime.strptime(d,date_format).date()

#print(data_object)
#print(type(data_object))

dia,mes,ano = data.split('/')

dia,mes,ano = int(dia), int(mes), int(ano)

if ano <= 0:
    print('Ano Inválido!')
else:
    if mes < 1 or mes > 12:
        print('Mês Inválido!')
    elif mes in [1,3,5,7,8,10,12]:
        if dia > 0 and dia < 32:
            print('Data Valida!')
        else:
            print('Dia Invalido!')
    elif mes in [4,6,9,11]:
        if dia > 0 and dia < 31:
            print('Data Válida!')
        else:
            print('Dia Inválido!')
    else:
        if ano % 4 == 0:
            if dia > 0 and dia < 30:
                print('Data Válida!')
            else:
                print ('Dia inválido!')
        else:
            if dia > 0 and dia < 29:
                print('Data Válida')
            else:
                print('Dia inválido!')







