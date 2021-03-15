import os
import sys

import requests
import markdown
from bs4 import BeautifulSoup


MD_EXTENSION = ".md"
BASE_URL = "https://github.com/kubeflow/kfserving/blob/master"


def find_pages(base_path : str) -> list:
    print("[*] Finding all .md pages")

    pages = []
    for root, _, files in os.walk(base_path):
        for f in files:
            if f.endswith(MD_EXTENSION):
                pages.append(f"{root[len(base_path):]}/{f}")

    print(f"\t[*] Found {len(pages)} pages")
    return pages


def find_links(base_path : str, pages : list) -> list:
    print("[*] Finding all links in pages")

    links = []
    for page in pages:
        base_dir = os.path.dirname(page)

        with open(f"{base_path}{page}", "r") as p:
            soup = BeautifulSoup(markdown.markdown(p.read()), features="lxml")
            for link in soup.findAll('a'):
                l = link.get('href')
                if l.startswith('#'):
                    continue
                elif l.startswith('http'):
                    links.append((page, l))
                else:
                    if l.startswith("./"):
                        l = l[2:]
                    links.append((page, f"{BASE_URL}/{base_dir}/{l}"))

    print(f"\t[*] Found {len(links)} links")
    return links


def try_links(links : list):
    print("[*] Trying links")

    for idx, (page, link) in enumerate(links):
        try:
            r = requests.get(f"{link}", allow_redirects=True)
        except Exception:
            if r.status_code == 429:
                # We were rate-limited, try again
                links.append((page, link))
            else:
                print(f"Page: {page}, Link: {link}, Status: {r.status_code}")
            continue

        if r.status_code != 200:
            print(f"Page: {page}, Link: {link}, Status: {r.status_code}")


if __name__ == "__main__":
    pages = find_pages(sys.argv[1])
    links = find_links(sys.argv[1], pages)
    try_links(links)
