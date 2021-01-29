import re
from urllib.request import urlopen
from urllib.parse  import urlencode
def getWithUrl(url):
    res = urlopen(url)

def postWithUrl(url):
    data = {'name': 'erik', "age": '25'}
    s = urlencode(data)
    res = urlopen(url, s.encode())
    print(res.read().decode())

def getHTMLContent(url):
    res = urlopen(url)
    htmlText = res.read()

getWithUrl('http://www.baidu.com')
postWithUrl('http://www.baidu.com')