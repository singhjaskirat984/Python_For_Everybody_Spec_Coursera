import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lst=[]

url = input('Enter location: ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
for item in counts:
    number = (item.find('count').text)
    lst.append(int(number))

print(sum(lst))
 