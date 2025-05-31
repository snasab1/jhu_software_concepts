from scrape import scrape_data, parse_html
from clean import save_data, load_data, clean_data

def main():
    url_base = "http://thegradcafe.com/survey/index.php"
    html_pages = scrape_data(url_base, pages=2)
    with open("all_pages.html", "w", encoding="utf-8") as f:
        for html in html_pages:
            f.write(html)
            f.write("\n<!-- PAGE BREAK -->\n")
    data = parse_html("all_pages.html", url_base)
    save_data(data, "applicant_data.json")

    clean_data("applicant_data.json")
    loaded = load_data("applicant_data.json")
    print(f"Loaded {len(loaded)} entries from applicant_data.json")

if __name__ == "__main__":
    main()