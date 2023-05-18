import requests
import urllib
from bs4 import BeautifulSoup


def extract_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    h1 = soup.find('h1')

    return h1.text


text= "origo"
text = urllib.parse.quote_plus(text)
url = 'https://google.com/search?q=' + text
request_result=requests.get( url )
soup = BeautifulSoup(request_result.text,"html.parser")
print(soup)
heading_object=soup.find_all('p')
print(heading_object)
for info in heading_object:
    print(info.getText())
    print("------")
