from scrape import scrape_data, parse_html
from clean import save_data, load_data, clean_data
from urllib import robotparser, parse
import math 

def file_exists(filename):
    try:
        with open(filename, "r"):
            return True
    except FileNotFoundError:
        return False

def _parsing_crawler_access(url_base):
    user_agent = "*"

    parser = robotparser.RobotFileParser()
    parser.set_url(parse.urljoin(url_base, "/robots.txt"))
    parser.read()
    return parser.can_fetch(user_agent, url_base)


def _has_enough_applicants(filename, min_count):
    data = load_data(filename)
    if len(data) >= min_count:
        return True
    return False

def main():
    url_base = "http://thegradcafe.com/survey/index.php"
    applicant_file_raw = "applicant_data_raw.json"
    applicant_file_cleaned = "applicant_data.json"
    min_count = 201

    if file_exists(applicant_file_raw):
        if _has_enough_applicants(applicant_file_raw, min_count):

            print(f"\nThe file {applicant_file_raw} already has at least {min_count} applicants.\n Skipping webscraping step and advancing to the cleaning step.\n")

            clean_data(applicant_file_raw, applicant_file_cleaned)
            loaded = load_data(applicant_file_cleaned)
            print(f"Cleaned and loaded {len(loaded)} entries from {applicant_file_cleaned}\n")
            return

    if _parsing_crawler_access(url_base):
        print(f"Web crawling is allowed for: {url_base}\n")
    else:
        print(f"Web crawling is not allowed for: {url_base}\n")

    pages = math.ceil(min_count / 20) # 20 applicants per page
    html_pages = scrape_data(url_base, pages)
    with open("all_pages.html", "w", encoding="utf-8") as f:
        for html in html_pages:
            f.write(html)
            f.write("\n<!-- PAGE BREAK -->\n")
    data = parse_html("all_pages.html", url_base)
    save_data(data, applicant_file_raw)

    clean_data(applicant_file_raw, applicant_file_cleaned)
    loaded = load_data(applicant_file_cleaned)
    print(f"Cleaned and loaded {len(loaded)} entries from {applicant_file_cleaned}")

if __name__ == "__main__":
    main()