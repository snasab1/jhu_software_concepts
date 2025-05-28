from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import re

url = "http://thegradcafe.com/survey/index.php"

def scrape_data(url, limit=10):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    entries = []
    table = soup.find("table")
    if not table:
        return entries
    rows = table.find_all("tr")[1:]  # skip header
    count = 0
    for row in rows:
        if count >= limit:
            break
        cols = row.find_all("td")
        if len(cols) < 5:
            continue
        university = cols[0].get_text(strip=True)
        program = cols[1].get_text(strip=True)
        status_text = cols[3].get_text(strip=True)
        date = cols[4].get_text(strip=True)
        if "Accepted" in status_text:
            status = "Accepted"
        elif "Rejected" in status_text:
            status = "Rejected"
        else:
            status = status_text
        entries.append({
            "University": university,
            "Program Name": program,
            "Applicant Status": status,
        })
        count += 1
    return entries

def clean_data(data):
    # For this simple case, assume data is already clean
    return data

def save_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def main():
    raw_data = scrape_data(url, limit=10)
    cleaned = clean_data(raw_data)
    save_data(cleaned, "applicant_data.json")
    print(f"Saved {len(cleaned)} entries to applicant_data.json")

if __name__ == "__main__":
    main()
