import os
from scrape import scrape_data, parse_html
from clean import save_data, load_data, clean_data
from urllib import robotparser, parse
import math 

def _parsing_crawler_access(url_base):
    """
    Private function: Check if the crawler is allowed to access the URL base by reading the robots.txt file

    Args: 
        url_base (str): The base URL to check

    Returns: 
        bool: True if crawling is allowed, False otherwise
    """
    user_agent = "*" # Using a univeral user agent 
    parser = robotparser.RobotFileParser()
    parser.set_url(parse.urljoin(url_base, "/robots.txt"))
    parser.read()
    return parser.can_fetch(user_agent, url_base) 

def _has_enough_applicants(filename, min_count):
    """
    Private function: Check if the raw JSON file has at least min_count applicants

    Args:
        filename (str): The name of the raw JSON file to check
        min_count (int): The minimum number of applicants required

    Returns:
        bool: True if the file has enough applicants, False otherwise
    """
    data = load_data(filename)
    if len(data) >= min_count:
        return True
    return False

def main():
    url_base = "http://thegradcafe.com/survey/index.php"
    applicant_file_raw = "applicant_data_raw.json" # Raw JSON file
    applicant_file_cleaned = "applicant_data.json" # Cleaned JSON file
    min_count = 15000 # Minimum number of applicants requested

    # To save time, check if the raw JSON file exists and contains at least the minimum number of applicants. If so, skip the scraping step and proceed directly to data cleaning.
    if os.path.exists(applicant_file_raw):
        # Check to see if the raw JSON file has enough applicants
        if _has_enough_applicants(applicant_file_raw, min_count):
            print(f"\nThe file {applicant_file_raw} already has at least {min_count} applicants.\n Skipping scraping step and advancing to the cleaning step.\n")

            # Go straight to the cleaning step
            clean_data(applicant_file_raw, applicant_file_cleaned)
            loaded = load_data(applicant_file_cleaned)
            print(f"Cleaned and loaded {len(loaded)} entries from {applicant_file_cleaned}\n")
            return 

    # If the raw JSON file doesn't exist or doesn't have enough applicants, we need to scrape the website:
    # Check if the crawler is allowed to access the URL
    if _parsing_crawler_access(url_base):
        print(f"Web crawling is allowed for: {url_base}\n")
    else:
        print(f"Web crawling is not allowed for: {url_base}\n")
        return # Exit the program if crawling is not allowed

    # Determine the number of pages to scrape 
    applicants_per_page = 20 
    pages = math.ceil(min_count / applicants_per_page)

    # Scrape the required number of pages and save each page's HTML, separated by a page break
    html_pages = scrape_data(url_base, pages)
    with open("all_pages.html", "w", encoding="utf-8") as f:
        for html in html_pages:
            f.write(html)
            f.write("\n<!-- PAGE BREAK -->\n")
    # Convert the HTML to raw JSON data
    data = parse_html("all_pages.html", url_base) 
    save_data(data, applicant_file_raw) # Save the raw JSON data 

    # Further clean the raw JSON data
    clean_data(applicant_file_raw, applicant_file_cleaned)
    loaded = load_data(applicant_file_cleaned)
    print(f"Cleaned and loaded {len(loaded)} entries from {applicant_file_cleaned}")

if __name__ == "__main__":
    main()