from urllib import request, parse

def scrape_data(url_base, pages=10):
    html_pages = []
    for page_num in range(1, pages + 1):
        if page_num == 1:
            url = url_base
        else:
            url = parse.urljoin(url_base, f"?page={page_num}")
        print(f"Fetching HTML from: {url}")
        page = request.urlopen(url)
        html = page.read().decode("utf-8")
        html_pages.append(html)
    return html_pages