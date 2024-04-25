import pandas as pd
import re

ag = pd.read_excel('integrate/agencias.xlsx')

instituicoes = ag['NOME_INSTITUICAO']
def remover_espacos_extra(string):
    return re.sub(r'\s+', ' ', string.strip())
lista = instituicoes.to_list()
lista_bancos = list()
for i in lista:
    lista_bancos.append(remover_espacos_extra(str(i)))

retorno_lista = list(set(lista_bancos))
retorno_lista.sort()
retorno_lista.remove('nan')

for i in retorno_lista:
    print(i)

    
