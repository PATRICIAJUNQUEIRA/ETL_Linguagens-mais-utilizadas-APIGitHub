# GitHub ETL Project

## Descrição do Projeto
Este projeto é um pipeline ETL (Extract, Transform, Load) que utiliza a API do GitHub para extrair, transformar e carregar dados. Implementado com a biblioteca `requests` do Python, o projeto realiza operações CRUD (Create, Read, Update, Delete) com dados de repositórios GitHub, além de gerenciar autenticação e paginação eficientemente.

## Funcionalidades do Projeto
- **Requisições HTTP**: Executa operações GET, POST, PUT e DELETE.
- **Manipulação de JSON**: Extrai e transforma dados no formato JSON.
- **Interage com Vários Endpoints**: Acessa diferentes endpoints da API do GitHub.
- **Tratamento de Status Codes**: Gerencia diversos status codes HTTP.
- **Autenticação e Paginação**: Administra a autenticação e paginação de resultados.
- **Orientação a Objetos**: Estrutura o código em classes e métodos para melhor organização e manutenção.

## Pré-requisitos
- Python 3.8 ou superior
- Biblioteca `requests`

## Instalação
1. **Clone o repositório**:
    ```bash
    git clone [URL do seu repositório]
    ```
2. **Navegue até o diretório do projeto**:
    ```bash
    cd API_Github_ETL
    ```
3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

## Configuração
- **Variáveis de Ambiente**: Copie o arquivo `.env.example` para `.env` e preencha as variáveis necessárias (ex: `GITHUB_TOKEN=seu_token_aqui`).

## Uso
- **Execução dos scripts**:
    ```bash
    python dados_repos.py
    python manipula_repos.py
    ```
- **Visualização no Jupyter Notebook**:
    Abra o `ETL.ipynb` para uma visão interativa e detalhada do processo ETL.

## Contribuições
Para contribuir com o projeto, siga estes passos:
1. **Fork** o repositório.
2. **Crie sua Feature Branch** (`git checkout -b feature/AmazingFeature`).
3. **Commit suas mudanças** (`git commit -m 'Add some AmazingFeature'`).
4. **Push para a Branch** (`git push origin feature/AmazingFeature`).
5. **Abra um Pull Request**.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Contato
- **Nome:** Patrícia Miranda
- **E-mail:** patricia.junqueira11@gmail.com
