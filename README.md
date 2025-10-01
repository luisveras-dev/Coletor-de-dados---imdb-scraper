# Coletor de Dados do IMDb - Most Popular Movies

## 1. What (O que é?)
Um projeto em Python que realiza web scraping na página "Most Popular Movies" do IMDb. Ele coleta automaticamente o ranking, título, ano de lançamento e a nota de cada filme listado, utilizando a biblioteca `BeautifulSoup` para a extração de dados e `Pandas` para o tratamento e exportação para um arquivo `movies.csv`.

## 2. Why (Por que?)
Este projeto foi desenvolvido como uma solução prática para aprender e aplicar conceitos fundamentais de programação em Python, incluindo:
- Automação de coleta de dados (Web Scraping).
- Manipulação e estruturação de dados com a biblioteca Pandas.
- Organização de um projeto de software, incluindo gerenciamento de dependências e documentação.

A solução final pode ser usada em análises de dados, criação de relatórios ou simplesmente para consultar a lista de filmes populares de forma rápida e offline.

## 3. Who (Quem participa?)
- **Desenvolvedores**: Ideal para estudantes e programadores que desejam praticar web scraping, automação e análise de dados com Python.
- **Usuários Finais**: Qualquer pessoa interessada em cinema que queira uma lista atualizada dos filmes mais populares do IMDb em um formato de planilha.

## 4. Where (Onde será usado?)
- **Ambiente de Execução**: O script é multiplataforma, projetado para rodar tanto em sistemas **Windows** quanto **Linux** (e macOS).
- **Saída de Dados**: Os resultados são salvos localmente em um arquivo `movies.csv`, que pode ser aberto em qualquer software de planilha (Excel, Google Sheets, etc.).

## 5. When (Quando usar?)
- Para obter uma "fotografia" instantânea dos filmes mais populares do momento.
- Quando for necessário coletar informações públicas de forma automatizada para projetos de análise de dados.

## 6. How (Como funciona?)

### Pré-requisitos
- Python 3.6 ou superior
- Git

### Passos para Execução
1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/luisveras-dev/Coletor-de-dados---imdb-scraper.git
    cd Coletor-de-dados---imdb-scraper
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Cria o ambiente
    python3 -m venv venv

    # Ativa no Linux/macOS
    source venv/bin/activate

    # Ativa no Windows
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o script principal:**
    ```bash
    python3 scraper.py
    ```

Após a execução, um arquivo chamado `movies.csv` será criado no diretório com todos os dados coletados.
