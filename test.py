from good import get_desc, bs4, get_html, get_price

soup = bs4(get_html('https://30-06.ru/catalog/product/101808/'), 'html.parser')

print(get_price(soup))