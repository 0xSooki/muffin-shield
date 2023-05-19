from utils.soup import *
import Levenshtein


def find_similar_strings(target, string_list):
    min_distance = float('inf')
    most_similar_string = None
    for string in string_list:
        print(target)
        print(string)
        distance = Levenshtein.distance(target, string)
        if distance < min_distance:
            min_distance = distance
            most_similar_string = string
            print(string)
            print(distance)
    if min_distance == 0:
        return 1
    elif min_distance < 33:
        return 0
    else:
        return None


def countClose(target, string_list):
    min_distance = float('inf')
    c = 0
    most_similar_string = None
    for string in string_list:
        print(target)
        print(string)
        distance = Levenshtein.distance(target, string)
        if distance < 45:
            c += 1
    return c


"""""
# Example usage
target_string = "apple"
string_list = ["apppkhfuzfuzfle", "app", "kiwi", "ple", "mango"]
similar_string = find_similar_strings(target_string, string_list)

if similar_string is not None:
    print(f"A similar string to '{target_string}' is '{similar_string}'.")
else:
    print(f"No similar string found for '{target_string}'.")
"""


def capsCheckH(allCaps, wordCount):
    if (allCaps/wordCount > 0.7):
        return 1
    else:
        return 0


def finalCheck(url):
    cont = extract_content(url)
    f1 = domainCheck(url)
    f2 = capsCheck(cont)
    return (f1*3+f2*2)/5


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


def googleSearch(title):
    find_similar_strings(title, search(title))
# 11 ugyanaz 41 még jó
# print(googleSearch("Sofa in the sky: Furniture flies during Turkey storm"))
