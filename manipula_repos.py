import requests
import base64
import os

class ManipulaRepositorios:
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.getenv('access_token')
        self.headers = {
            'Authorization': "Bearer " + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo, pasta='data'):
        # Codificando o arquivo
        with open(caminho_arquivo, "rb") as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)

        # Realizando o upload
        path = f'{pasta}/{nome_arquivo}'  # Correção aqui para incluir a pasta no caminho
        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{path}"
        data = {
            "message": f"Adicionando um novo arquivo {nome_arquivo}",
            "content": encoded_content.decode("utf-8")
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f'status_code upload do arquivo: {response.status_code}')

    def cria_repo(self, nome_repo):
        data = {
            "name": nome_repo,
            "description": "Dados dos repositórios de algumas empresas",
            "private": False
        }
        response = requests.post(f"{self.api_base_url}/user/repos", 
                                 json=data, headers=self.headers)
        print(f'status_code criação do repositório: {response.status_code}')

# instanciando um objeto
novo_repo = ManipulaRepositorios('PATRICIAJUNQUEIRA')

# Supondo que o repositório 'ETL_linguagens-utilizadas-da-Amazon' já foi criado anteriormente
nome_repo = 'ETL_linguagens-utilizadas-da-Amazon'

# Adicionando arquivos salvos no repositório criado
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')