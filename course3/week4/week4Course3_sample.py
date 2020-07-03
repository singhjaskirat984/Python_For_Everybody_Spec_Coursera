import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

lst=list()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("enter - ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('span')
for tag in tags:
	lst.append(int(tag.contents[0]))

print(sum(lst))
