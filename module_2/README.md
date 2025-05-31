# Module 2: Web Scraping

This project is a basic web scraper for Grad Cafe admissions results. It fetches multiple pages, parses the HTML, and saves the data as JSON. 

## Approach
- Checks `robots.txt` for scraping permission using the function _parsing_crawler_access contained in run.py.
- Scrapes the required number of pages (determined on the desired number of applicants).
- Parses and cleans the data, saving first a raw JSON file, then a cleaned JSON file.
- Skips scraping if a sufficient dataset (desired number of applicants) already exists.

## Structure of Program
- **run.py**: Main script that coordinates the workflow—checks robots.txt, determines if scraping is needed, and calls scraping, parsing, and cleaning functions.
- **scrape.py**: Contains functions to scrape HTML pages from Grad Cafe and parse the HTML into structured data (raw JSON file).
- **clean.py**: Provides functions to save/load JSON data and further clean and process the scraped data.

- **requirements.txt**: Lists required Python packages.
- **applicant_data_raw.json**: Raw scraped data.
- **applicant_data.json**: Cleaned and processed data.

## Potential Bugs
- The parsing method is dependent on the HTML structure of Grad Cafe. If the HTML structure changes, then extracting applicant data may not work as desired.
- Duplicate or missing entries if the site format is inconsistent.