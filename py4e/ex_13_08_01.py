import urllib.request, urllib.parse, urllib.error
import json
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

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    js = json.loads(data)
    counts = js['comments']
    print('Count:', len(counts))

    nlst = list()
    for num in counts:
        inum = int(num['count'])
        nlst.append(inum)
    print('Sum:',sum(nlst))

    break
