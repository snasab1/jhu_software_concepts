"""
Module 5: Query Data - contains functions to query applicant data from a PostgreSQL database.
"""
import psycopg
from psycopg import sql, Error 

# pylint: disable=no-member 

# --- Database Connection Parameters ---
DB_HOST = "localhost"
DB_NAME = "applicant_data"
DB_USER = "postgres"
DB_PASSWORD = ""

TABLE_NAME = "applicants"

def execute_and_fetch(query, params=None, fetch_one=True):
    """
    Executes a given SQL query with optional parameters and fetches results.
    Can accept a raw string query or a psycopg.sql.SQL object.

    Args:
        query (str or psycopg.sql.SQL): The SQL query string or object.
        params (tuple, optional): Parameters to pass to the query. Defaults to None.
        fetch_one (bool): If True, fetches one row; otherwise, fetches all rows. Defaults to True.

    Returns:
        tuple or list: The fetched row(s) or None if an error occurs.
    """
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
    except Error as e:
        print(f"Database error executing query: {query}\nError: {e}")
        return None
    finally:
        if connection:
            connection.close()

def _get_result(query, params=None):
    """
    Helper function to execute a query that is expected to return a value
    (e.g., COUNT, AVG). Returns the value or None if no result or an error occurs.
    """
    result = execute_and_fetch(query, params, fetch_one=True)
    # Return the first element if result is not None and not empty, otherwise None
    return result[0] if result else None

def total_applicants_fall_2024():
    """Counts the total number of applicants for the 'Fall 2024' term."""
    # Using sql.SQL and sql.Identifier for safe query composition
    query_composed = sql.SQL("SELECT COUNT(*) FROM {} WHERE term = %s;").format(
        sql.Identifier(TABLE_NAME)
    )
    count = _get_result(query_composed, ("Fall 2024",))
    return count if count is not None else 0 # Return int, not formatted string

def percent_international():
    """Calculates the percentage of international applicants."""
    query_total_composed = sql.SQL("SELECT COUNT(*) FROM {};").format(
        sql.Identifier(TABLE_NAME)
    )
    total = _get_result(query_total_composed)
    if total is None or total == 0:
        return 0.0 # Return 0.0 as a float for no applicants

    query_international_composed = sql.SQL("SELECT COUNT(*) FROM {} WHERE us_or_international = %s;").format(
        sql.Identifier(TABLE_NAME)
    )
    intl = _get_result(query_international_composed, ("International",))
    if intl is None:
        intl = 0 # Ensure intl is a number for calculation

    percent = (intl / total * 100)
    return percent # Return float, not formatted string

def average_gpa_and_gre():
    """
    Calculates average GPA, GRE, GRE Verbal, and GRE Analytical Writing scores
    for applicants who have submitted them.
    """
    # Using sql.SQL and sql.Identifier for safe query composition for each average
    query_avg_gpa_composed = sql.SQL("SELECT AVG(gpa) FROM {} WHERE gpa IS NOT NULL;").format(
        sql.Identifier(TABLE_NAME)
    )
    avg_gpa = _get_result(query_avg_gpa_composed) or 0.0 # Default to 0.0 if None

    query_avg_gre_composed = sql.SQL("SELECT AVG(gre) FROM {} WHERE gre IS NOT NULL;").format(
        sql.Identifier(TABLE_NAME)
    )
    avg_gre = _get_result(query_avg_gre_composed) or 0.0

    query_avg_gre_v_composed = sql.SQL("SELECT AVG(gre_v) FROM {} WHERE gre_v IS NOT NULL;").format(
        sql.Identifier(TABLE_NAME)
    )
    avg_gre_v = _get_result(query_avg_gre_v_composed) or 0.0
    
    query_avg_gre_aw_composed = sql.SQL("SELECT AVG(gre_aw) FROM {} WHERE gre_aw IS NOT NULL;").format(
        sql.Identifier(TABLE_NAME)
    )
    avg_gre_aw = _get_result(query_avg_gre_aw_composed) or 0.0
    
    return {
        "gpa": avg_gpa,
        "gre_total": avg_gre,
        "gre_verbal": avg_gre_v,
        "gre_analytical_writing": avg_gre_aw
    }

def average_gpa_american_fall_2024():
    """Calculates the average GPA of American applicants for the 'Fall 2024' term."""
    query_composed = sql.SQL("""
        SELECT AVG(gpa) FROM {}
        WHERE term = %s 
        AND us_or_international = %s 
        AND gpa IS NOT NULL;
    """).format(
        sql.Identifier(TABLE_NAME)
    )
    avg_gpa = _get_result(query_composed, ("Fall 2024", "American"))
    return avg_gpa if avg_gpa is not None else 0.0 

def acceptance_percentage_fall_2024():
    """Calculates the acceptance percentage for the 'Fall 2024' term."""
    query_total_composed = sql.SQL("SELECT COUNT(*) FROM {} WHERE term = %s;").format(
        sql.Identifier(TABLE_NAME)
    )
    total = _get_result(query_total_composed, ("Fall 2024",))
    if total is None or total == 0:
        return 0.0 

    query_accepted_composed = sql.SQL("SELECT COUNT(*) FROM {} WHERE term = %s AND status LIKE %s;").format(
        sql.Identifier(TABLE_NAME)
    )
    accepted = _get_result(query_accepted_composed, ("Fall 2024", "%Accepted%"))
    if accepted is None:
        accepted = 0 # Ensure accepted is a number for calculation

    percent = accepted / total * 100
    return percent 

def average_gpa_accepted_fall_2024():
    """Calculates the average GPA of 'Accepted' applicants for the 'Fall 2024' term."""
    query_composed = sql.SQL("""
        SELECT AVG(gpa) FROM {}
        WHERE term = %s 
        AND status LIKE %s
        AND gpa IS NOT NULL;
    """).format(
        sql.Identifier(TABLE_NAME)
    )
    avg_gpa = _get_result(query_composed, ("Fall 2024", "%Accepted%"))
    return avg_gpa if avg_gpa is not None else 0.0 

def jhu_applicants_masters_cs():
    """Counts the number of Johns Hopkins applicants for a Master's in Computer Science."""
    query_composed = sql.SQL("""
        SELECT COUNT(*) FROM {}
        WHERE program LIKE %s
        AND degree LIKE %s
    """).format(
        sql.Identifier(TABLE_NAME)
    )
    # Changed "%Mas%" to "%Master%" for broader match, assuming this is intended
    count = _get_result(query_composed, ("%Johns%Hopkins%Comp%Sci%", "%Master%"))
    return count if count is not None else 0 