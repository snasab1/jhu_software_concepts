from scrape_data import scrape_data
from load_data import load_data
import json

url_base = "http://thegradcafe.com/survey/index.php"

def main():  
    html_pages = scrape_data(url_base, pages=1)
    print(f"Fetched {len(html_pages)} HTML pages for parsing.")
    with open("all_pages.html", "w", encoding="utf-8") as f:
        for html in html_pages:
            f.write(html)
            f.write("\n<!-- PAGE BREAK -->\n")
    print("Saved all HTML pages to all_pages.html")

    data = load_data("all_pages.html")
    with open("program_university_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)  # <--- Add ensure_ascii=False here!
    print(f"Saved {len(data)} entries to program_university_data.json")

if __name__ == "__main__":
    main()