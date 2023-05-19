from utils.soup import *
import Levenshtein


def finalCheck(url):
    cont = extract_content(url)
    f1 = domainCheck(url)
    f2 = capsCheck(cont)
    f3 = googleSearch2(cont)
    print(f1, f2, f3)
    return (f1*3+f2*2+(f3))/6


def googleSearch2(title):
    return countClose(title, search(title))


def countClose(target, string_list):
    min_distance = float('inf')
    c = 0
    print(string_list)
    most_similar_string = None
    for string in string_list:
        distance = Levenshtein.distance(target, string)
        print(distance)
        if distance < 45:
            c += 1
    return (c/len(string_list))


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
        if (word.isupper()):
            c += 1
    return (capsCheckH(c, words))


a = ["co", "ru", "lo"]
b = ["index", "origo"]


def domainCheck(url):
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

