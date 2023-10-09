import requests
import zipfile
from requests.packages.urllib3.exceptions import InsecureRequestWarning

file_url = 'https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/taxa_transicao/tx_transicao_municipios_2019_2020.zip'
file = 'arquivo.zip'


class getFile:
    def __init__(self):

        # Desativa a verificação de certificado SSL
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        response = requests.get(file_url, verify=False)

        with open(file, 'wb') as f:
            f.write(response.content)

        print("download OK")


class extractFile:
    def __init__(self):
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall()
            print("extração OK")


class getSheetSource():
    def __init__(self)
    pass


getFile()
extractFile()
getSheetSource()
