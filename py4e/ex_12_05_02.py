# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
cnt = input('Enter count: ')
c = int(cnt)
pos = input('Enter position: ')
n = int(pos)
lst = list()
i = 0

# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
# tags = soup('a')
print('Retrieving:', url)
while i < c:
    i = i + 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        lst.append(tag.get('href', None))
    url = lst[n-1]
    lst.clear()
    print('Retrieving:', url)
