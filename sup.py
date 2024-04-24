import pandas as pd
import re

def verificar_tamanho_agencia_e_conta(agencia:str):
    """Verifica se a quantidade de caracteres da agência e da conta está correta."""
    if len(agencia) != 4:
        return {'validacao':False,'Retorno': "Agência deve conter 4 digitos."}
    
    ag = pd.read_excel('integrate/agencias.xlsx')
    agencias_cod = ag['COD_COMPE_AG']
    cd_ag = int(agencia)
    if cd_ag  in agencias_cod:
        
        # Função para remover espaços extras de uma string
        def remover_espacos_extra(string):
            return re.sub(r'\s+', ' ', string.strip())

        # Encontrar o índice da linha onde o valor ocorre na coluna "COD_COMPE_AG"
        indice_linha = ag.index[ag['COD_COMPE_AG'] == cd_ag ]

        # Obter a linha do DataFrame
        linha = ag.loc[indice_linha]
        #Criando lista de retorno de dados
        retorno_info = list()
        # Converter a linha em um dicionário
        linha_dict = linha.to_dict(orient='records')
        for i in linha_dict:
            # Remover espaços extras das strings no dicionário e adicionar na lista de retorno
            retorno_info.append({chave: remover_espacos_extra(valor) for chave, valor in i.items() if isinstance(valor, str)})
        
        
        return {"validate":True,'return':'Agência válida!','data':retorno_info}
    

    else:
        return {"validacao":False,'retorno':'Agência inválida!'}
    

print(verificar_tamanho_agencia_e_conta('3546'))

    
