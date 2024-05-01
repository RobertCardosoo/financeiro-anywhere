import pandas as pd
import requests

for i in range(1,100):
    requests.get('http://15.229.91.141/bancos').json()



    
