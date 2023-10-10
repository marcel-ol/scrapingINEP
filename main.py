import requests
import zipfile
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# import psycopg2 as psy
# from conexao import *

arquivoURL = 'https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/taxa_transicao/tx_transicao_municipios_2019_2020.zip'
arquivo = 'arquivo.zip'


class getFile:
    def __init__(self, file_url, file):
        self.execucao(file_url, file)

    def execucao(self, file_url, file):
        # Desativa a verificação de certificado SSL
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(file_url, verify=False)
        with open(file, 'wb') as f:
            f.write(response.content)
        print("download OK")


class extractFile:
    def __init__(self, file):
        self.execucao(file)

    def execucao(self, file):
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall()
            print("extração OK")


getFile(arquivoURL, arquivo)
extractFile(arquivo)
