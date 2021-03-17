import os
import sys

import requests
import markdown
from bs4 import BeautifulSoup


MD_EXTENSION = ".md"


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
        with open(f"{base_path}{page}", "r") as p:
            soup = BeautifulSoup(markdown.markdown(p.read()), features="lxml")
            for link in soup.findAll('a'):
                l = link.get('href')
                if l.startswith('#'):
                    continue
                links.append((page, l.split("#")[0]))  # split to remove anchors

    print(f"\t[*] Found {len(links)} links")
    return links


def try_links(base_path : str, links : list):
    print("[*] Trying links")

    for idx, (page, link) in enumerate(links):
        if link.startswith('http'):
            try:
                r = requests.get(f"{link}", allow_redirects=True)
            except Exception:
                print(f"Page: {page}, Link: {link}, Status: HTTP {r.status_code}")
                continue

            if r.status_code != 200:
                print(f"Page: {page}, Link: {link}, Status: HTTP {r.status_code}")

        else:
            page_dir = os.path.dirname(page)
            page_dir = f"{base_path}/{page_dir}"
            resolved_path = f"{page_dir}/{link}"

            if os.path.isfile(resolved_path) is False and os.path.isdir(resolved_path) is False:
                print(f"Page: {page}, Link: {resolved_path}, Status: local file/dir not found")


if __name__ == "__main__":
    pages = find_pages(sys.argv[1])
    links = find_links(sys.argv[1], pages)
    try_links(sys.argv[1], links)
