import pandas as pd
import requests

lista_bancos = requests.get('http://15.229.91.141/bancos').json()


print(len(lista_bancos))



    
