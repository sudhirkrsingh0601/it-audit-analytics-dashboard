import csv
import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CSV_FILE = PROJECT_ROOT / "data" / "raw" / "transactions.csv"
DATABASE_FILE = PROJECT_ROOT / "data" / "processed" / "audit.db"
SCHEMA_FILE = PROJECT_ROOT / "sql" / "schema.sql"


def main():
    DATABASE_FILE.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DATABASE_FILE) as connection:
        schema = SCHEMA_FILE.read_text(encoding="utf-8")
        connection.executescript(schema)

        with CSV_FILE.open("r", newline="", encoding="utf-8-sig") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = [
                (
                    row["transaction_id"],
                    row["transaction_date"],
                    row["employee_id"],
                    row["vendor"],
                    float(row["amount"]) if row["amount"].strip() else None,
                    row["currency"],
                    row["department"],
                    row["payment_method"],
                )
                for row in reader
            ]

        # Replace the table contents so rerunning this script won't duplicate rows.
        connection.execute("DELETE FROM transactions")
        connection.executemany(
            """
            INSERT INTO transactions (
                transaction_id, transaction_date, employee_id, vendor,
                amount, currency, department, payment_method
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            rows,
        )

        count = connection.execute(
            "SELECT COUNT(*) FROM transactions"
        ).fetchone()[0]

    print(f"Loaded {count} fictional transactions into {DATABASE_FILE}")


if __name__ == "__main__":
    main()