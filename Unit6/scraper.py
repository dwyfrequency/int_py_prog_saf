"""Task: from the archive (link below), follow each link, find the image
in that linked page, and download the image
url = https://apod.nasa.gov/apod/archivepix.html

Concepts:
    1. Download stuff => urllib
    2. Parsing stuff out of html => BeautifulSoup
"""

import urllib.request
from urllib.parse import urljoin # converts relative links to absolute
from bs4 import BeautifulSoup

# Dowload the index page 
base_url = "https://apod.nasa.gov/apod/archivepix.html"
download_directory = "/home/jdwy215/intPyProg_Jess_McK/Unit6/output/"
resp = urllib.request.urlopen(base_url).read()

# For each link on the index page: 
for link in BeautifulSoup(resp, "lxml").findAll('a'):
    print("Following link:", link)
    href = urljoin(base_url, link["href"])

    content = urllib.request.urlopen(href).read()
    for img in BeautifulSoup(content, "lxml").findAll('img'):
        img_href = urljoin(href, img["src"])
        print("Downloading image:", img_href)

        # split the image on the forward slash and take the last part
        img_name = img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href, download_directory + img_name)

# a tags start <a href> which gives us links
# print(BeautifulSoup(resp, "lxml").findAll('a'))

print(type(tags[0]))
# print(tags[0])

tag = tags[0]

# calling the indiv tag with href with give us the underlying link
print(tag["href"])


