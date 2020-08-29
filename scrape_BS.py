import [urllib2][1]
from bs4 import BeautifulSoup
from urlparse  import urljoin

url = "http://www.google.com/index-%d.html"
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

base = "http://www.google.com"

images = [urljoin(base,a["href"]) for a in soup.select("td a[href^=images/]")]

for url in images:
    img = BeautifulSoup(urllib2.urlopen(url).read(),"lxml").find("img")["src"]
with open("myimages/{}".format(img), "w") as f:
    f.write(urllib2.urlopen("{}/{}".format(url.rsplit("/", 1)[0], img)).read())
