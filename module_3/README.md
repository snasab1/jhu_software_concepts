# Week 3: SQL Data Analysis

**Name:** Sara Nasab  
**Email:** snasab1@jh.edu  
**Module:** Week 3: SQL Data Analysis  
**Due Date:** 6/08/2025

---

## Project Overview

This project analyzes graduate admissions data using SQL and Python.  
**Note:** The SQL queries are based on the JSON data file generated from Module 2 (Grad Cafe data) which has been updated and can be found within the `module_2` directory. This current version has been updated to reflect **valid** range of scores (GPA, GRE); the user submitted scores that do not fall within the valid range are not recorded (replaced with None). Additionally, this version includes all available Applicant Type (i.e., American, International, Other); before, only International students were recorded.  The changes are reflected in scrape.py and clean.py. 

---

## Instructions for Use (Module 3)

1. **Create the Database:**
   - Run `create_applicants_data_db.py` to create the PostgreSQL database and table structure. This will not work if the database has already been created. 

2. **Populate the Database:**
   - Use `load_data.py` to load data from `applicant_data.json` (from Module 2) into your database.
   - The database will be populated with the number of applicants found in `applicant_data.json` (15,000 applicants).

3. **Run SQL Queries:**
   - Use `query_data.py` to run SQL queries and obtain statistics about the applicants. For the reasoning of SQL query choice, refer to `desciptions_sqlqueries.pdf`. 

4. **View Results in the Browser:**
   - Start the Flask web app with `app.py` to view the SQL query results in a styled HTML page. It is very simple, but does take advantage of some customization using CSS styling. 
   - The web interface uses:
     - `app.py` (Flask application)
     - `templates/index.html` (HTML template)
     - `static/style.css` (CSS styling)
     - `query_data.py` (SQL query functions)

---

## File Structure

- `create_applicants_data_db.py` — Creates the PostgreSQL database and tables.
- `load_data.py` — Loads applicant data from JSON into the database.
- `query_data.py` — Contains SQL query functions for data analysis.
- `app.py` — Flask app to display query results in the browser.
- `templates/index.html` — HTML template for the web page.
- `static/style.css` — CSS file for styling the web page.

