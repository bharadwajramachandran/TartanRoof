from bs4 import BeautifulSoup
import sys
import urllib2

def URLtoTitle(url):
    if url == '':
        return ''
    else:
        print url
        response = soup = None
        assert(url.startswith("http"))
        try:
            response = urllib2.urlopen(url)
            page_source = response.read()
            soup = BeautifulSoup(page_source)
        finally:
            if (response != None): 
                response.close()
        if (soup.title == None):
            return ''
        else:
            return soup.title.string

def readFile(filename, mode="rt"):
    # rt stands for "read text"
    fin = contents = None
    try:
        fin = open(filename, mode)
        contents = fin.read()
    finally:
        if (fin != None): fin.close()
    return contents

def removeSource(raw_text):
    data_arr = raw_text.split()
    len_d = len(data_arr)
    if (len_d > 1):
        print data_arr
        return data_arr[1]
    elif (len_d == 0):
        return ''
    else:
        print data_arr
        return ''

def getTitles(textfile):
    raw_file = readFile(textfile).split('\n')
    last_elem = raw_file.pop()
    URL_list = map(removeSource, raw_file)
    return map(URLtoTitle, URL_list)

print getTitles(sys.argv[1])
