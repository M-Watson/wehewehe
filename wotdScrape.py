import requests
from bs4 import BeautifulSoup as bs
import re


def find_key_words(url):
    site = requests.get(url)
    page = site.text
    soup = bs(page)
    body = soup.find('body')

    site_contents = str(body)#body.findChildren(recursive=False)
    print(site_contents)
    pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
    setnences = re.findall(pat,site_contents)


    keywords = ['means']

    found_list = []

    for sentence in sentences:
        for keyword in keywords:
            if keyword in sentence:
                found_list.append(sentence)

    print(found_list)

    return(found_list)

find_key_words("https://www.hpr2.org/post/hawaiian-word-day-january-18th#stream/0")
