import urllib.request, os, argparse
from urllib.parse import urljoin # converts relative links to absolute
from bs4 import BeautifulSoup
def scrapy(base_url, out_dir):
    # Dowload the index page 
    # base_url = "https://apod.nasa.gov/apod/archivepix.html"

    # when creating the set, we need the trailing period or it will split into
    # letters
    to_visit = set((base_url,))
    visited = set()
    print(to_visit)

    while to_visit:
        # pick a link to visit
        current_page = to_visit.pop()
        print("Current page: {}".format(current_page))
        print("visiting: {}".format(current_page))
        visited.add(current_page)
        content = urllib.request.urlopen(current_page).read()

        # Extract any new links from that page.
        for link in BeautifulSoup(content, 'lxml').findAll('a'):
            absolute_link = urljoin(base_url, link["href"])
            if absolute_link not in visited:
                to_visit.add(absolute_link)
            else:
                print("Already visited:", absolute_link)

        # Download any images on the page 
        for img in BeautifulSoup(content, "lxml").findAll('img'):
            img_href = urljoin(current_page, img["src"])
            print("Downloading image: {}".format(img_href))
            img_name = img_href.split("/")[-1]
            urllib.request.urlretrieve(img_href,
                                       os.path.join(out_dir,img_name))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out_dir', help='''output directory for nasa
                        images. Must place arg in between quotes
                        ex: "~/myTestDir"''')
    parser.add_argument('-u', '--url', help='''base url to visit.
                        Must place arg in between quotes
                        ex: "https://test.com"''')
    args = parser.parse_args()

    if args.url and args.out_dir:
        scrapy(args.url, args.out_dir)
    else:
        print("""Missing command line arguments. Please use --help to see script
              params""")

if __name__ == "__main__":
    main()
