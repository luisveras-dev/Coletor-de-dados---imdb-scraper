# -*- coding: utf-8 -*-
import requests
import logging
from bs4 import BeautifulSoup
import pandas as pd

# Configura um sistema de mensagens (logging) para sabermos o que o script está fazendo.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_page(url):
    """
    Acessa a URL fornecida e retorna o conteúdo da página se a requisição for bem-sucedida.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    logging.info(f"Acessando a URL: {url}")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        logging.info("Página acessada com sucesso!")
        return response.content
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao acessar a página: {e}")
        return None

def parse_movies(page_content):
    """
    Analisa o conteúdo HTML, extrai os dados dos filmes e os retorna em uma lista.
    """
    soup = BeautifulSoup(page_content, "html.parser")
    movie_list = soup.select("li.ipc-metadata-list-summary-item")
    
    if not movie_list:
        logging.warning("Nenhum filme encontrado. A estrutura do site pode ter mudado.")
        return []

    logging.info(f"Encontrados {len(movie_list)} filmes. Iniciando extração de dados...")
    
    movies_data = []
    for position, movie_item in enumerate(movie_list, 1):
        try:
            # 1. Título do Filme
            title_element = movie_item.select_one("h3.ipc-title__text")
            # Lógica de extração de título mais robusta
            title_text = title_element.text.strip()
            title = title_text.split('.', 1)[1].strip() if '.' in title_text else title_text

            # 2. Ano de Lançamento - SELETOR CORRIGIDO
            metadata_elements = movie_item.select("span.cli-title-metadata-item")
            year = metadata_elements[0].text.strip() if metadata_elements else "N/A"
            
            # 3. Nota (Rating)
            rating_element = movie_item.select_one("span.ipc-rating-star--base")
            rating_text = rating_element.text.strip().split()
            rating = rating_text[0] if rating_text else "N/A"

            movies_data.append({
                "Posição": position,
                "Título": title,
                "Ano": year,
                "Nota IMDb": rating
            })
            logging.info(f"Coletado: #{position} - {title}")

        except (AttributeError, IndexError) as e:
            logging.warning(f"Não foi possível extrair dados de um item na posição {position}. Erro: {e}")
            continue
            
    return movies_data

def save_to_csv(data, filename="movies.csv"):
    """
    Salva os dados em um arquivo .csv usando pandas.
    """
    if not data:
        logging.warning("Nenhum dado para salvar.")
        return

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    logging.info(f"Dados salvos com sucesso no arquivo '{filename}'!")

# Ponto de Entrada Principal do Script 
if __name__ == "__main__":
    imdb_url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
    
    page_content = fetch_page(imdb_url)
    
    if page_content:
        movies = parse_movies(page_content)
        if movies:
            save_to_csv(movies)
    else:
        logging.error("Não foi possível obter o conteúdo da página. O script será encerrado.")