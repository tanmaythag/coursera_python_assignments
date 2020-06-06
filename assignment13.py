import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('enter url:')

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('counts:',len(counts))
x = 0
for count in counts:
    x += int(count.text)  

print(x)
