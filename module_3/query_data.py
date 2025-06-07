import psycopg

# --- Database Connection Parameters ---
DB_HOST = "localhost"
DB_NAME = "applicant_data"
DB_USER = "postgres"
DB_PASSWORD = ""

TABLE_NAME = "applicants"

def execute_and_fetch(query, params=None, fetch_one=True):
    """Executes a query and fetches results."""
    connection = None
    try:
        connection = psycopg.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        with connection.cursor() as cur:
            cur.execute(query, params)
            return cur.fetchone() if fetch_one else cur.fetchall()
    except psycopg.Error as e:
        print(f"Database error executing query: {query}\nError: {e}")
        return None
    finally:
        if connection:
            connection.close()

# --- Private Helper Function ---
def _get_result(query, params=None):
    """
    Executes a query expected to return a single value and safely extracts it.

    Args:
        query (str): The SQL query string (e.g., "SELECT COUNT(*) FROM ...").
        params (tuple, optional): Parameters for the query.

    Returns:
        int: The extracted count, or 0 if no valid count is returned.
    """
    result = execute_and_fetch(query, params, fetch_one=True)
    # This line safely extracts the count from the tuple (e.g., (123,))
    # or defaults to 0 if result is None (meaning execute_and_fetch failed)
    count = result[0] if result else 0
    return count

def total_applicants_fall_2024():
    """Prints the total number of applicants for Fall 2024."""
    query = f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE term = %s;"
    count = _get_result(query, ("Fall 2024",))
    print(f"Total applicants for Fall 2024: {count}")

def percent_international():
    """Prints the percentage of international students (not American or Other) overall."""
    query_total = f"SELECT COUNT(*) FROM {TABLE_NAME};"
    query_international = f"""
        SELECT COUNT(*) FROM {TABLE_NAME}
        WHERE us_or_international IS NOT NULL
        AND us_or_international NOT IN ('American', 'Other');
    """
    total = _get_result(query_total)
    intl = _get_result(query_international)
    percent = (intl / total * 100) if total > 0 else 0.0
    print(f"Percentage of international students (overall): {percent:.2f}%")

def average_GPA_and_GRE():
    return

def average_gpa_american_fall_2024():
    return

def acceptance_percentage_fall_2024():
    return

def average_gpa_accepted_fall_2024():
    return

def jhu_applicants_masters_CS():
    return


def main():
    print("--- Applicant Statistics ---\n")
    total_applicants_fall_2024()
    percent_international()
    # Add more query functions here as needed

if __name__ == "__main__":
    main()