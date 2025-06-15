"""
The script loads applicant data from a JSON file into a PostgreSQL database.
"""
import json
import psycopg

# --- Database Connection Parameters ---
DB_HOST = "localhost"
DB_NAME = "applicant_data"
DB_USER = "postgres"
DB_PASSWORD = ""

# --- File Path ---
DATA_FILE = "../module_2/applicant_data.json"

# --- Table Name ---
TABLE_NAME = "applicants"

# --- Table Schema ---
CREATE_TABLE_SQL = f"""
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    p_id SERIAL PRIMARY KEY,
    program TEXT,
    comments TEXT,
    date_added DATE,
    url TEXT,
    status TEXT,
    term TEXT,
    us_or_international TEXT,
    gpa FLOAT,
    gre FLOAT,
    gre_v FLOAT,
    gre_aw FLOAT,
    degree TEXT
);
"""

# --- Insert Statement ---
INSERT_SQL = f"""
INSERT INTO {TABLE_NAME} (
    program, comments, date_added, url, status, term, us_or_international,
    gpa, gre, gre_v, gre_aw, degree
) VALUES (
    %(program)s, %(comments)s, %(date_added)s, %(url)s, %(status)s, %(term)s, %(us_or_international)s,
    %(gpa)s, %(gre)s, %(gre_v)s, %(gre_aw)s, %(degree)s
);
"""

def map_json_to_sql(entry):
    """Map JSON keys to SQL columns, handling missing keys."""
    return {
        "program": f"{entry.get('University', '')} - {entry.get('Program Name', '')}",
        "comments": entry.get("Comments"),
        "date_added": entry.get("Added On"),
        "url": entry.get("URL Link"),
        "status": entry.get("Applicant Status"),
        "term": entry.get("Program Start"),
        "us_or_international": entry.get("Applicant Type"),
        "gpa": float(entry["GPA"]) if entry.get("GPA") not in (None, "") else None,
        "gre": float(entry["GRE"]) if entry.get("GRE") not in (None, "") else None,
        "gre_v": float(entry["GRE V"]) if entry.get("GRE V") not in (None, "") else None,
        "gre_aw": float(entry["GRE AW"]) if entry.get("GRE AW") not in (None, "") else None,
        "degree": entry.get("Program Type"),
    }

def main():
    """
    Main function to load data from JSON file into PostgreSQL database.
    """
    # Load JSON data
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Connect to PostgreSQL
    with psycopg.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    ) as conn:
        with conn.cursor() as cur:
            # Create table if not exists
            cur.execute(CREATE_TABLE_SQL)
            conn.commit()

            # Insert data
            for entry in data:
                sql_entry = map_json_to_sql(entry)
                cur.execute(INSERT_SQL, sql_entry)
            conn.commit()
    print(f"Loaded {len(data)} records into '{TABLE_NAME}'.")

if __name__ == "__main__":
    main()
