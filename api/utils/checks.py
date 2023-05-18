from soup import *
import Levenshtein


def find_similar_strings(target, string_list):
    min_distance = float('inf')
    most_similar_string = None

    for string in string_list:
        distance = Levenshtein.distance(target, string)
        if distance < min_distance:
            min_distance = distance
            most_similar_string = string
            print(string)
            print(distance)
    if min_distance == 0:
        return 1
    elif min_distance < 3:
        return 0
    else:
        return None


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
