import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATABASE_FILE = PROJECT_ROOT / "data" / "processed" / "audit.db"
CHECKS_FILE = PROJECT_ROOT / "sql" / "control_checks.sql"


def main():
    sql = CHECKS_FILE.read_text(encoding="utf-8")

    with sqlite3.connect(DATABASE_FILE) as connection:
        connection.row_factory = sqlite3.Row
        exceptions = connection.execute(sql).fetchall()

    print("Check ID | Transaction ID | Amount | Issue")
    print("-" * 65)

    for item in exceptions:
        print(
            f"{item['check_id']} | {item['transaction_id']} | "
            f"{item['amount']} | {item['issue']}"
        )

    print(f"\nTotal exception rows: {len(exceptions)}")


if __name__ == "__main__":
    main()