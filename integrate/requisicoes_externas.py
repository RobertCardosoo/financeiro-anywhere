import requests


def retorna_cartao(num:str):
    req = requests.get(f'https://lookup.binlist.net/{num}').json()

    return req


