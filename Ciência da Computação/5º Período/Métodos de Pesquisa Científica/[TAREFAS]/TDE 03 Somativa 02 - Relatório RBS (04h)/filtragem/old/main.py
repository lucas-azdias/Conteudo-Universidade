import requests
import pandas as pd
from bs4 import BeautifulSoup

USERNAME = "ladsword_api2"
PASSWORD = "ay5HB7phqn7fHK"

def get_html_for_page(url):
    payload = {
        "url": url,
        "source": "google",
    }
    response = requests.post(
        "https://realtime.oxylabs.io/v1/queries",
        auth=(USERNAME,PASSWORD),
        json=payload,
    )
    response.raise_for_status()
    return response.json()["results"][0]["content"]

def get_citations(article_id):
    url = f"https://scholar.google.com/scholar?q=info:{article_id}:scholar.google.com&output=cite"
    html = get_html_for_page(url)
    soup = BeautifulSoup(html, "html.parser")
    data = []
    for citation in soup.find_all("tr"):
        title = citation.find("th", {"class": "gs_cith"}).get_text(strip=True)
        content = citation.find("div", {"class": "gs_citr"}).get_text(strip=True)
        entry = {
            "title": title,
            "content": content,
        }
        data.append(entry)

    return data

def parse_data_from_article(article):
    title_elem = article.find("h3", {"class": "gs_rt"})
    title = title_elem.get_text() if title_elem else ""
    
    title_anchor_elem = article.select("a")
    if title_anchor_elem:
        url = title_anchor_elem[0]["href"]
        article_id = title_anchor_elem[0].get("id", "")  
    else:
        url = ""
        article_id = ""
    
    authors_elem = article.find("div", {"class": "gs_a"})
    authors = authors_elem.get_text() if authors_elem else ""
    
    abstract_elem = article.find("div", {"class": "gs_rs"})
    abstract = abstract_elem.get_text() if abstract_elem else ""
    return {
        "title": title,
        "authors": authors,
        "url": url,
        "citations": get_citations(article_id),
        "abstract": abstract
    }

def get_url_for_page(url, page_index):
    return url + f"&start={page_index}"

def get_data_from_page(url):
    html = get_html_for_page(url)
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find_all("div", {"class": "gs_ri"})
    return [parse_data_from_article(article) for article in articles]

data = []
url = "https://scholar.google.com/scholar?hl=pt-BR&as_sdt=0%2C5&as_ylo=2023&q=%22it+professionals%22+%22skills+gap%22+%22cybersecurity%22&btnG="

NUM_OF_PAGES = 13
page_index = 0
for i in range(NUM_OF_PAGES):
    page_url = get_url_for_page(url, page_index)
    entries = get_data_from_page(page_url)
    data.extend(entries)
    page_index += 10
    print(f"Page {i + 1} concluded.")


df = pd.DataFrame(data)

df.to_csv('dados_artigos.csv', index=True)
