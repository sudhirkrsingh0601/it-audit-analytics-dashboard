CREATE TABLE IF NOT EXISTS transactions (
    row_id INTEGER PRIMARY KEY,
    transaction_id TEXT,
    transaction_date TEXT,
    employee_id TEXT,
    vendor TEXT,
    amount REAL,
    currency TEXT,
    department TEXT,
    payment_method TEXT
);