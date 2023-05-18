import requests
from bs4 import BeautifulSoup


def extract_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    h1 = soup.find('h1')

    if h1:
        print(h1.text)
    content = soup.find('article',{'class':'article-body'})
    print(content.text)

url = "https://www.origo.hu/tudomany/20230517-nem-ajanlja-a-szintetikus-es-a-termeszetes-edesitoszerek-hosszu-tavu-hasznalatat-a-who.html"

extract_content(url)