"""
This script creates a new PostgreSQL database named 'applicant_data'
and sets up its initial schema if it doesn't already exist.
"""

import psycopg
from psycopg import Error

# --- Database Connection Parameters ---
# Connect to the default administrative database 'postgres' to create 'applicant_data'
DB_HOST = "localhost"
DB_NAME_INITIAL = "postgres" # Connect to 'postgres'
DB_USER = "postgres"
DB_PASSWORD = "" # empty string due to 'trust' authentication for localhost

# --- New Database to Create ---
NEW_DB_NAME = "applicant_data" # database load_data.py script needs

print(f"Attempting to create database: '{NEW_DB_NAME}'")


try:
    with psycopg.connect(
        host=DB_HOST,
        dbname=DB_NAME_INITIAL,
        user=DB_USER,
        password=DB_PASSWORD
    ) as conn:
        # Crucial: Set autocommit mode for CREATE DATABASE
        conn.autocommit = True

        print(f"Connected to database '{DB_NAME_INITIAL}' successfully.")

        with conn.cursor() as cur:
            # SQL command to create the new database
            CREATE_DB_QUERY = f"CREATE DATABASE {NEW_DB_NAME};"

            print(f"Executing SQL: {CREATE_DB_QUERY}")
            cur.execute(CREATE_DB_QUERY)

            print(f"Database '{NEW_DB_NAME}' created successfully!")

except Error as e:
    print(f"Error creating database '{NEW_DB_NAME}': {e}")
    # This error is expected if the database already exists from a previous run.

finally:
    print("\nScript finished.")
