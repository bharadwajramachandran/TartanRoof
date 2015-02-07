from bs4 import BeautifulSoup
import sys
import urllib2

def URLtoTitle(url):
    response = urllib2.urlopen(url)
    page_source = response.read()
    soup = BeautifulSoup(page_source)
    return soup.title.string

def readWebPage(url):
    assert(url.startswith("http://"))
    fin = contents = None
    try:
        fin = urllib.urlopen(url)
        contents = fin.read()
    finally:
        if (fin != None): fin.close()
    return contents

def readFile(filename, mode="rt"):
    # rt stands for "read text"
    fin = contents = None
    try:
        fin = open(filename, mode)
        contents = fin.read()
    finally:
        if (fin != None): fin.close()
    return contents

def getTitles(textfile):
    URL_list = (readFile(textfile)).split()
    return map(URLtoTitle, URL_list)

print getTitles(sys.argv[1])
