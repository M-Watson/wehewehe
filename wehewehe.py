import requests
from xml.etree import ElementTree
import re
from bs4 import BeautifulSoup as bs


def get_definition(word):

    post_url = "http://wehewehe.org/gsdl2.85/cgi-bin/hdict"
    headers = {}
    payload = "a=xml&q={}&fqv=_textchd_".format(word)
    payload = payload.encode("utf8")
    a = requests.post(post_url,data=payload)

    return(a)


def parse_xml_tree(b):
    btree = ElementTree.fromstring(b.content)
    contents = []
    soups = []
    for node in btree:
        print("{}".format(node))
        for section in node:
            print("\t{}".format(section))
            if section.tag == 'Content':
                print("\t\t\t\n{}\n".format(section.text))
                contents.append(section.text)
                soups.append(bs(section.text))
            for subsection in section:
                print("\t\t{}".format(subsection))
    return(soups)

def inner_content(tt):
    pat = r'.*?\>(.*)\<.*'
    matches = []
    for tt in t:
        match = re.search(pat,str(tt))
        matches.append(match[1])
    return(matches)
