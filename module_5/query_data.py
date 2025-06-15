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

def _get_result(query, params=None):
    result = execute_and_fetch(query, params, fetch_one=True)
    return result[0] if result else 0

def total_applicants_fall_2024():
    query = f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE term = %s;"
    count = _get_result(query, ("Fall 2024",))
    return f"{count}"

def percent_international():
    query_total = f"SELECT COUNT(*) FROM {TABLE_NAME};"
    total = _get_result(query_total)
    if total == 0:
        return "No applicants found."
    query_international = f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE us_or_international = %s;"
    intl = _get_result(query_international, ("International",))
    percent = (intl / total * 100) if total > 0 else 0.0
    return f"{percent:.2f}%"

def average_GPA_and_GRE():
    query_avg_gpa = f"SELECT AVG(gpa) FROM {TABLE_NAME} WHERE gpa IS NOT NULL;"
    avg_gpa = _get_result(query_avg_gpa)
    query_avg_gre = f"SELECT AVG(gre) FROM {TABLE_NAME} WHERE gre IS NOT NULL;"
    avg_gre = _get_result(query_avg_gre)
    query_avg_gre_v = f"SELECT AVG(gre_v) FROM {TABLE_NAME} WHERE gre_v IS NOT NULL;"
    avg_gre_v = _get_result(query_avg_gre_v)
    query_avg_gre_aw = f"SELECT AVG(gre_aw) FROM {TABLE_NAME} WHERE gre_aw IS NOT NULL;"
    avg_gre_aw = _get_result(query_avg_gre_aw)
    return (f"GPA: {avg_gpa:.2f}, GRE: {avg_gre:.2f}, "
            f"GRE Verbal: {avg_gre_v:.2f}, GRE Analytical Writing: {avg_gre_aw:.2f}")

def average_gpa_american_fall_2024():
    query = f"""
        SELECT AVG(gpa) FROM {TABLE_NAME}
        WHERE term = %s 
        AND us_or_international = %s 
        AND gpa IS NOT NULL;
    """
    avg_gpa = _get_result(query, ("Fall 2024", "American"))
    return f"{avg_gpa:.2f}"

def acceptance_percentage_fall_2024():
    query_total = f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE term = %s;"
    total = _get_result(query_total, ("Fall 2024",))
    if total == 0:
        return "No applicants for Fall 2024."
    query_accepted = f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE term = %s AND status LIKE %s;"
    accepted = _get_result(query_accepted, ("Fall 2024", "%Accepted%"))
    percent = (accepted / total * 100)
    return f"{percent:.2f}%"

def average_gpa_accepted_fall_2024():
    query = f"""
        SELECT AVG(gpa) FROM {TABLE_NAME}
        WHERE term = %s 
        AND status LIKE %s
        AND gpa IS NOT NULL;
    """
    avg_gpa = _get_result(query, ("Fall 2024", "%Accepted%"))
    return f"{avg_gpa:.2f}"

def jhu_applicants_masters_CS():
    query = f"""
        SELECT COUNT(*) FROM {TABLE_NAME}
        WHERE program LIKE %s
        AND degree LIKE %s
    """
    count = _get_result(query, ("%Johns%Hopkins%Comp%Sci%", "%Mas%"))
    return f"{count}"