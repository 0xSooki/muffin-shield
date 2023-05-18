import requests
import urllib
from bs4 import BeautifulSoup


def extract_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    h1 = soup.find('h1')

    return h1.text

def search(text):
    headers={"Accept-Language":"en-US,en;q=0.9"}
    cookies = {"CONSENT": "YES+cb.20210720-07-p0.en+FX+410"}
    text = urllib.parse.quote_plus(text)
    url = 'https://google.com/search?q=' + text
    request_result=requests.get( url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(request_result.text,"html.parser")
    heading_object=soup.find_all('h3')
    """for info in heading_object:
        print(info.getText())
        print("------")"""
    resList = ""
    for info in heading_object:
        resList = resList + info.getText()
    return resList

print(search("Italy floods leave 13 dead and force 13,000 from their homes"))