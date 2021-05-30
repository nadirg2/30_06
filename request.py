import requests

def get_html(url, params={}):
    html = get_respones(url, params)
    if html is not None: return html.text


def get_respones(url, params):
    HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    r = requests.get(url=url, headers=HEADERS, params=params)
    return r
