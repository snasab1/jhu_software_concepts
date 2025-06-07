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
    """Prints the average GPA and GRE scores of applicants who submitted them."""
    # Get the average GPA of applicants who submitted their GPA
    query_avg_gpa = f"SELECT AVG(gpa) FROM {TABLE_NAME} WHERE gpa IS NOT NULL;"
    avg_gpa = _get_result(query_avg_gpa)

    # Get the average GRE scores of applicants who submitted their GRE scores
    query_avg_gre = f"SELECT AVG(gre) FROM {TABLE_NAME} WHERE gre IS NOT NULL;"
    avg_gre = _get_result(query_avg_gre)

    # Get the average GRE Verbal scores of applicants who submitted their GRE Verbal scores
    query_avg_gre_v = f"SELECT AVG(gre_v) FROM {TABLE_NAME} WHERE gre_v IS NOT NULL;"
    avg_gre_v = _get_result(query_avg_gre_v)

    # Get the average GRE Analytical Writing scores of applicants who submitted their GRE Analytical Writing scores
    query_avg_gre_aw = f"SELECT AVG(gre_aw) FROM {TABLE_NAME} WHERE gre_aw IS NOT NULL;"
    avg_gre_aw = _get_result(query_avg_gre_aw)

    print(f"Average GPA: {avg_gpa:.2f}")
    print(f"Average GRE: {avg_gre:.2f}")
    print(f"Average GRE Verbal: {avg_gre_v:.2f}")
    print(f"Average GRE Analytical Writing: {avg_gre_aw:.2f}")

    return

def average_gpa_american_fall_2024():
    """Prints the average GPA of American applicants for Fall 2024."""
    query = f"""
        SELECT AVG(gpa) FROM {TABLE_NAME}
        WHERE term = %s 
        AND us_or_international = %s 
        AND gpa IS NOT NULL;
    """
    avg_gpa = _get_result(query, ("Fall 2024", "American"))
    print(f"Average GPA of American applicants for Fall 2024: {avg_gpa:.2f}")
    return

def acceptance_percentage_fall_2024():
    """Prints the percentage of Fall 2024 entries that are Acceptances."""
    # Total Fall 2024 entries
    query_total = f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE term = %s;"
    total = _get_result(query_total, ("Fall 2024",))
    if total == 0:
        print("No applicants for Fall 2024.")
        return

    # Accepted Fall 2024 entries (status contains 'Accepted')
    query_accepted = f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE term = %s AND status LIKE %s;"
    accepted = _get_result(query_accepted, ("Fall 2024", "%Accepted%"))

    percent = (accepted / total * 100) if total > 0 else 0.0
    print(f"Percentage of Acceptances for Fall 2024: {percent:.2f}%")
    return


def average_gpa_accepted_fall_2024():
    """Prints the average GPA of Accepted applicants for Fall 2024."""
    query = f"""
        SELECT AVG(gpa) FROM {TABLE_NAME}
        WHERE term = %s 
        AND status LIKE %s
        AND gpa IS NOT NULL;
    """
    avg_gpa = _get_result(query, ("Fall 2024", "%Accepted%"))
    print(f"Average GPA of Accepted applicants for Fall 2024: {avg_gpa:.2f}")
    return

def jhu_applicants_masters_CS():
    """Prints the total number of JHU applicants for Master's in Computer Science."""
    query = f"""
        SELECT COUNT(*) FROM {TABLE_NAME}
        WHERE program LIKE %s
        AND degree LIKE %s
    """
    # Using wildcards to match JHU Masters CS applicants
    count = _get_result(query, ("%Johns%Hopkins%Comp%Sci%", "%Mas%"))
    print(f"Total JHU applicants for Master's in Computer Science: {count}")

    return


def main():
    print("--- Applicant Statistics ---\n")
    total_applicants_fall_2024()
    percent_international()
    average_GPA_and_GRE()
    average_gpa_american_fall_2024()
    acceptance_percentage_fall_2024()
    average_gpa_accepted_fall_2024()
    jhu_applicants_masters_CS()
    # Add more query functions here as needed

if __name__ == "__main__":
    main()