"""Task: from the archive (link below), follow each link, find the image
in that linked page, and download the image
url = https://apod.nasa.gov/apod/archivepix.html

Concepts:
    1. Download stuff => urllib
    2. Parsing stuff out of html => BeautifulSoup
"""

import urllib.request, os, argparse
from urllib.parse import urljoin # converts relative links to absolute
from bs4 import BeautifulSoup

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out_dir', help='output directory for nasa images')
    args = parser.parse_args()

    # Dowload the index page 
    base_url = "https://apod.nasa.gov/apod/archivepix.html"
    download_directory = args.out_dir
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
            urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))

if __name__ == "__main__":
    main()
