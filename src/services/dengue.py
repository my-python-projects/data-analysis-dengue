import requests
import json
#import csv
from datetime import datetime

# geocode: código IBGE da cidade
# disease: tipo de doença a ser consultado (str:dengue|chikungunya|zika)
# format: formato de saída dos dados (str:json|csv)
# ew_start: semana epidemiológica de início da consulta (int:1-53)
# ew_end: semana epidemiológica de término da consulta (int:1-53)
# ey_start: ano de início da consulta (int:0-9999)
# ey_end: ano de término da consulta (int:0-9999)

# Todos os parâmetros acima mencionados são obrigatórios para a consulta.

api = "http://info.dengue.mat.br/api/alertcity"

class Requests():

    def call(self, url):

        search_filter = '?geocode=3304557&disease=dengue&format=json&ew_start=1&ew_end=50&ey_start=2017&ey_end=2017'

        url = url + search_filter

        request = requests.get(url)
        #print("akiiii" + str(request.status_code), flush=True)
        #print(request.content, flush=True)
        reddit_data = (request.status_code == 200) and json.loads(request.content) or [] 

        request.connection.close()
        request.close()

        return reddit_data
    

    def data1(self):
        url = api
        reddit = self.call(url)

        data = []

        for info in reddit:
            info['data_iniSE'] = int(str(info['data_iniSE'])[0:10])
            info['data_iniSE'] = datetime.fromtimestamp(info['data_iniSE'])

            #print("Date time object:", info['data_iniSE'], flush=True )

            info['data_iniSE']  = info['data_iniSE'].strftime("%d/%m/%Y")
            info['nivel']       = self.getNivel(info['nivel'])
            info['transmissao'] = self.getTransmissao(info['transmissao'])

            #print('new', info['data_iniSE'], flush=True)
            data.append(info)
        
        return data       
    

    # nivel: Nível de alerta (1 = verde, 2 = amarelo, 3 = laranja, 4 = vermelho)
    def getNivel(self, nivel) -> str:
        n = ''

        if   nivel == 1:    n = 'Verde'
        elif nivel == 2:    n = 'Amarelo'
        elif nivel == 3:    n = 'Laranja'
        else:               n = 'Vermelho'

        # opcao match é aceita apartir da versao 3.10 do python
        # match nivel:
        #     case 1:     n = 'Verde'
        #     case 2:     n = 'Amarelo'
        #     case 3:     n = 'Laranja'
        #     case 4:     n = 'Vermelho'
        #     case _:     n = ''

        return n

    
    # transmissao: Evidência de transmissão sustentada: 0 = nenhuma evidência, 1 = possível, 2 = provável, 3 = altamente provável
    def getTransmissao(self, transmissao) -> str:
        n = ''

        if   transmissao == 0:      n = 'Nenhuma evidência'
        elif transmissao == 1:      n = 'Possível'
        elif transmissao == 2:      n = 'Provável'
        else:                       n = 'Altamente provável'

        return n


    # def getDatas(self, red):
    #     informacoes = []

    #     # Obter as informacoes dos boletins do dia anterior
    #     for info in red['results']:
            
    #         if info['state'] == state and info['date'] == "2020-09-25":
    #             print('aki323')
    #             print(info['state'])
    #             informacoes.append(info)

    #     return informacoes



    # def createDataSet(self, lista_itens):
    #     print('create: ', lista_itens)
    #     with open(covid, 'w', newline='') as file:
    
    #         writer = csv.writer(file, delimiter=';',
    #                     quotechar=';', quoting=csv.QUOTE_MINIMAL)
            
    #         for item in lista_itens:
    #             writer.writerow([item])

