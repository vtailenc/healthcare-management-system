"""Insert clearly fictional sample data into the local demo database."""
import sqlite3
import os

db_path = os.getenv("DATABASE_PATH", "healthcare_demo.db")
with sqlite3.connect(db_path) as db:
    db.execute(
        "INSERT INTO patients (name, date_of_birth, email) VALUES (?, ?, ?)",
        ("Alex Example", "1990-01-01", "alex@example.test"),
    )
    db.execute(
        "INSERT INTO patients (name, date_of_birth, email) VALUES (?, ?, ?)",
        ("Jamie Sample", "1985-06-15", "jamie@example.test"),
    )
print("Inserted fictional demo patients.")
