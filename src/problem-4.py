from urllib import request
from bs4 import BeautifulSoup


fp = request.urlopen("https://en.wikipedia.org/wiki/Artificial_intelligence")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

soup = BeautifulSoup(mystr)
print(soup.prettify())