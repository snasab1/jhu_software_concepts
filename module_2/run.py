from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import re

url_base = "http://thegradcafe.com/survey/index.php"

def scrape_data(url_base, pages=10): # Edit the number of pages as needed
    html_pages = []
    for page_num in range(1, pages + 1):
        if page_num == 1:
            url = url_base
        else:
            url = f"{url_base}?page={page_num}"
        print(f"Fetching HTML from: {url}")
        page = urlopen(url)
        html = page.read().decode("utf-8")
        html_pages.append(html)
    return html_pages

def main():  
    html_pages = scrape_data(url_base, pages=10)
    print(f"Fetched {len(html_pages)} HTML pages for parsing.")
    # Save all HTML pages as one file
    with open("all_pages.html", "w", encoding="utf-8") as f:
        for html in html_pages:
            f.write(html)
            f.write("\n<!-- PAGE BREAK -->\n")  # Optional: add a marker between pages
    print("Saved all HTML pages to all_pages.html")

if __name__ == "__main__":
    main()