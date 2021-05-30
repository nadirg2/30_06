from bs4 import BeautifulSoup as bs4
from request import get_html

def get_last_page():
    html = get_html("https://30-06.ru/catalog/")
    soup = bs4(html, 'html.parser')
    last_page_url = soup.find('a', string="Конец").get('href')
    last_page_num = last_page_url[18-len(last_page_url):]
    return last_page_num


def get_pages():
    # ?PAGEN_1=2
    last_page_num = get_last_page()
    urls = []
    for i in range(1, last_page_num+1):
        urls.append(f"https://30-06.ru/catalog/?PAGEN_1={i}")
    return urls


def get_urls_to_goods(url):
    urls = []
    html = get_html(url)
    soup = bs4(html, 'html.parser')
    for el in soup.select('.section-items .item'):
        link = el.select_one('a').get('href')
        urls.append(link)
    return urls
