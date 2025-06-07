from urllib import request, parse
from bs4 import BeautifulSoup
import re, time

def scrape_data(url_base, pages):
    """
    Scrape data from the url_base (i.e., Grad Cafe page) for a given number of pages.

    Args:
        url_base (str): The base URL of the Grad Cafe survey page.
        pages (int): The number of pages to scrape.
    Returns:
        list: HTML pages scraped from the Grad Cafe survey page.
    """
    html_pages = []
    print(f"Scraping data from {url_base} for {pages} pages.")
    # Loop through the pages and fetch the HTML content
    for page_num in range(1, pages + 1):
        if page_num == 1:
            url = url_base
        else:
            url = parse.urljoin(url_base, f"?page={page_num}")
        print(f"Fetching HTML from: {url}")
        page = request.urlopen(url)
        html = page.read().decode("utf-8")
        html_pages.append(html)

        # Pause every 50 scrapes
        if page_num % 50 == 0:
            print(f"Pausing for 1 second after {page_num} pages...")
            time.sleep(1)

    return html_pages

def _extract_specs(text):
    """
    Extract specifications (Applicant type, GRE Scores, GPA, Program Start) from the given text.

    Args:
        text (str): The text from which to extract specs.
    Returns:
        dict: A dictionary containing the extracted specs.
    """
    specs = {}
    # Extract Applicant Type
    if "International" in text:
        specs["Applicant Type"] = "International"
    elif "American" in text:
        specs["Applicant Type"] = "American"
    elif "Other" in text:
        specs["Applicant Type"] = "Other"
    else:
        specs["Applicant Type"] = None
    # Extract GRE
    if "GRE" in text:
        m = re.search(r"GRE\s+(\d+)", text)
        if m:
            specs["GRE"] = m.group(1)
        else:
            specs["GRE"] = None
    else:
        specs["GRE"] = None
    # Extract GRE V (Verbal)
    if "GRE V" in text:
        m = re.search(r"GRE V\s*([\d.]+)", text)
        if m:
            specs["GRE V"] = m.group(1)
        else:
            specs["GRE V"] = None
    else:
        specs["GRE V"] = None
    # Extract GRE AW (Analytical Writing)
    if "GRE AW" in text:
        m = re.search(r"GRE AW\s*([\d.]+)", text)
        if m:
            specs["GRE AW"] = m.group(1)
        else:
            specs["GRE AW"] = None
    else:
        specs["GRE AW"] = None
    # Extract GPA
    if "GPA" in text:
        m = re.search(r"GPA\s+([\d.]+)", text)
        if m:
            specs["GPA"] = m.group(1)
        else:
            specs["GPA"] = None
    else:
        specs["GPA"] = None
    # Extract Program Term
    m = re.search(r"(Fall|Spring)\s+\d{4}", text)
    if m:
        specs["Program Start"] = m.group(0)
    else:
        specs["Program Start"] = None
    return specs

def parse_html(html_file, url_base):
    """
    Parse the HTML file to extract applicant data into a structured raw JSON file.

    Args:
        html_file (str): The path to the HTML file containing the scraped data.
        url_base (str): The base URL to resolve relative links.
    Returns:
        list: A list of dictionaries containing the extracted applicant data.
    """
    # Read the HTML file and split it into pages
    with open(html_file, "r", encoding="utf-8") as f:
        html = f.read()
    # Split the HTML content using the page break comment
    pages = html.split("<!-- PAGE BREAK -->")
    data = []
    # Loop through each page and extract the data
    for page in pages:
        soup = BeautifulSoup(page, "html.parser")
        # Find the table containing the applicant data
        table = soup.find("table")
        if not table:
            continue
        # Find all rows in the table, skipping the header row
        rows = table.find_all("tr")[1:]  # skip header
        i = 0
        # Loop through the rows and extract the data
        while i < len(rows):
            row = rows[i]
            cols = row.find_all("td") 
            if len(cols) < 4:
                i += 1
                continue
            # Extract the university, program name, added on date, and decision
            university = cols[0].get_text(strip=True)
            program = cols[1].get_text(strip=True)
            added_on = cols[2].get_text(strip=True)
            decision = cols[3].get_text(strip=True)

            # Extract the applicant link from the last <td> in the row using html parsing
            url_link = None
            if len(cols) > 4:
                link_td = cols[-1]
            else:
                link_td = cols[3]
            a_tag = link_td.find("a", href=True) 
            if a_tag:
                url_link = a_tag["href"]
                url_link = parse.urljoin(url_base, url_link)  

            # Check the next row for extra details (like GRE, GPA, Program Start) if it contains only one <td> cell (colspan).
            specs = {}
            comments = None
            if i + 1 < len(rows):
                next_row = rows[i + 1]
                next_cols = next_row.find_all("td")
                if len(next_cols) == 1:
                    specs = _extract_specs(next_row.get_text(" ", strip=True))
                    i += 1  # skip the specs row 
            else:
                # If no next row, assume no specs are available (returns None for all)
                specs = _extract_specs("")

            # Find pattern that indicates comments, then extract comments
            if i + 1 < len(rows):
                comment_row = rows[i + 1]
                comment_cols = comment_row.find_all("td")
                if (
                    len(comment_cols) == 1 and
                    comment_cols[0].has_attr("colspan") and
                    comment_cols[0]["colspan"] == "100%"
                ):
                    p_tag = comment_cols[0].find("p")
                    if p_tag:
                        comments = p_tag.get_text(strip=True)
                    i += 1  # skip the comment row
            entry = {
                "University": university,
                "Program Name": program,
                "Program Type": None, # Program Type will be set later
                "Program Start": specs.get("Program Start"),
                "Added On": added_on,
                "Applicant Status": decision,
                "GRE": specs.get("GRE"),
                "GRE V": specs.get("GRE V"),
                "GRE AW": specs.get("GRE AW"),
                "GPA": specs.get("GPA"),
                "Applicant Type": specs.get("Applicant Type"),
                "Comments": comments,
                "URL Link": url_link
            }
            data.append(entry)
            i += 1
    return data