from soup import extract_content

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
url= "https://www.origo.hu/tudomany/20230517-nem-ajanlja-a-szintetikus-es-a-termeszetes-edesitoszerek-hosszu-tavu-hasznalatat-a-who.html"
print(capsCheck(extract_content(url)))