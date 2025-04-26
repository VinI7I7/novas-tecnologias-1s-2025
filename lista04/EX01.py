#Escreva uma função chamada formatar_data que recebe três parâmetros: dia, mês e ano. A função deve
#retornar uma string com a data formatada no formato "dd/mm/aaaa". Permita que os parâmetros
#ejam passados com seus respectivos nomes e em qualquer ordem. Teste a função com diferentes
#ombinações de argumentos nomeados.

import datetime


def formatar_data(dd,mm,aaaa):
    data = datetime.date(aaaa,mm,dd)
    print(data.strftime("%d/%m/%Y"))


print(formatar_data(12,4,2025))
