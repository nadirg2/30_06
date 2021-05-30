from bs4 import BeautifulSoup as bs4
from request import get_html

def get_good_details(url):
    html = get_html(url)
    soup = bs4(html, 'html.parser')

    desc = get_desc(soup)
    price = get_price(soup)
    name = soup.select_one('.element-right h1').getText()

    return {"url": url, "price": price, "name": name, "desc": desc}



def get_desc(soup):
    descs = {}
    i=0
    for desc_item in soup.select('.description.des2 td.td-1'):
        i+=1
        if i%2==1:
            name = desc_item.getText()
        else:
            value = desc_item.getText()
            descs[name] = value
    return descs


def get_price(soup):
    price = soup.select_one('.price').getText().replace(' ', '')
    price = price[:len(price)-3]
    return int(price)