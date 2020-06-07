import urllib.request, urllib.parse, urllib.error
import json
import ssl

url = ' http://py4e-data.dr-chuck.net/comments_544306.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
try:
	js = json.loads(data)
except:
	js = None
 
count = 0
sum = 0 
for i in js['comments']:
    count = count+1
    sum = sum + i['count']
print(sum)   

























