#####################################
# Python para Pentesters            #
# https://solyd.com.br/treinamentos #
#####################################

import requests

url = 'https://solyd.com.br'

cabecalho = {'user-agent': 'Mozilla/5.0 (X11; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0 Iceweasel/43.0.4',
             }
parametros = {'id': '10'}

resposta = requests.get(url, headers=cabecalho)

print resposta.text
