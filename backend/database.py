
import json
import sqlite3
from pathlib import Path

DB_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "privacy_assessments.db"
)


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS assessments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                risk_score INTEGER NOT NULL,
                risk_level TEXT NOT NULL,
                total_questions INTEGER NOT NULL,
                category_results TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        columns = {
            row["name"]
            for row in connection.execute(
                "PRAGMA table_info(assessments)"
            ).fetchall()
        }

        if "category_results" not in columns:
            connection.execute(
                "ALTER TABLE assessments ADD COLUMN category_results TEXT"
            )


def save_assessment(result, category_results=None):
    with get_connection() as connection:
        cursor = connection.execute("""
            INSERT INTO assessments (
                risk_score,
                risk_level,
                total_questions,
                category_results
            )
            VALUES (?, ?, ?, ?)
        """, (
            result["risk_score"],
            result["risk_level"],
            result["total_questions"],
            json.dumps(category_results) if category_results is not None else None
        ))

        return cursor.lastrowid


def get_all_assessments():
    with get_connection() as connection:
        rows = connection.execute("""
            SELECT id, risk_score, risk_level,
                   total_questions, category_results, created_at
            FROM assessments
            ORDER BY id DESC
        """).fetchall()

        results = []

        for row in rows:
            item = dict(row)

            if item["category_results"]:
                item["category_results"] = json.loads(
                    item["category_results"]
                )
            else:
                item["category_results"] = {}

            results.append(item)

        return results


if __name__ == "__main__":
    initialize_database()
    print(f"Database initialized: {DB_PATH}")