import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    print('Count:', len(counts))

    nlst = list()
    for num in counts:
        inum = int(num.text)
        nlst.append(inum)
    print('Sum:',sum(nlst))
    
    break
