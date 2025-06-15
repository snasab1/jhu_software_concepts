# Module 5: Software Assurance, Static Code Analysis, and SQL Injections

**Name:** Sara Nasab  
**Email:** snasab1@jh.edu  
**Due Date:** 6/15/2025

---

## Project Overview

This project builds on data from Module 3 and demonstrates:
- Secure SQL data analysis, defending against SQL injection
- Code quality improvements using Pylint (score 10/10)
- Visualization of module dependencies with pydeps and graphviz

---
## How to Run

1. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```
2. **Set up the database:**  
   Ensure PostgreSQL is running and the applicant data is loaded (see Module 3 for setup).
3. **Run the Flask app:**  
   ```sh
   python app.py
   ```
   Then open [http://localhost:8080](http://localhost:8080) in your browser.

---

## Static Analysis

- Run Pylint on code:
  ```sh
  pylint app.py query_data.py
  ```
  All modules should score 10/10.

---

## Dependency Visualization

- Generate a dependency graph:
  ```sh
  pydeps app.py
  ```
  The SVG (`app.svg`) shows how modules and dependencies are connected.



