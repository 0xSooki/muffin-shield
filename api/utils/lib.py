from soup import extract_content
from serpapi import GoogleSearch

def test() -> str:
    return "Hello, world!"

def capsCheckH(allCaps, wordCount):
    if (allCaps/wordCount > 0.7):       
        return 1
    else:
        return 0
    
def capsCheck(content):
    conList = content.split()
    filter(None, conList)
    words = len(conList)
    c = 0
    for word in conList:
        if(word.isupper()):
            c += 1
    return (capsCheckH(c,words))


a = ["co", "ru", "lo"]
b = ["index", "origo"]
def domainCheck(url) :
    sep = url.rsplit('/')
    dom = sep[2].rsplit('.')
    l1 = 0
    l2 = 1
    for i in a:
        if i == dom[-1]:
            l1 = 1

    for j in b:
        if j == dom[1]:
            l2 = 0
    return (l1+l2)/2


url= "https://www.origo.hu/tudomany/20230517-nem-ajanlja-a-szintetikus-es-a-termeszetes-edesitoszerek-hosszu-tavu-hasznalatat-a-who.html"
print(capsCheck(extract_content(url)))
print(domainCheck(url))

