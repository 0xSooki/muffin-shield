import requests
from bs4 import BeautifulSoup


def extract_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    h1 = soup.find('h1')

    return h1.text
