-- DUP-01: Return every row whose transaction ID occurs more than once.
SELECT
    'DUP-01' AS check_id,
    'Duplicate transaction ID' AS issue,
    t.row_id,
    t.transaction_id,
    t.transaction_date,
    t.employee_id,
    t.vendor,
    t.amount,
    t.department,
    t.payment_method
FROM transactions AS t
JOIN (
    SELECT transaction_id
    FROM transactions
    GROUP BY transaction_id
    HAVING COUNT(*) > 1
) AS duplicates
    ON t.transaction_id = duplicates.transaction_id

UNION ALL

-- AMT-01: Flag transactions above the exercise threshold of $50,000.
SELECT
    'AMT-01',
    'Amount above $50,000',
    row_id,
    transaction_id,
    transaction_date,
    employee_id,
    vendor,
    amount,
    department,
    payment_method
FROM transactions
WHERE amount > 50000

UNION ALL

-- MISS-01: Flag missing required fields.
SELECT
    'MISS-01',
    'Missing required field',
    row_id,
    transaction_id,
    transaction_date,
    employee_id,
    vendor,
    amount,
    department,
    payment_method
FROM transactions
WHERE transaction_date IS NULL OR TRIM(transaction_date) = ''
   OR employee_id IS NULL OR TRIM(employee_id) = ''
   OR vendor IS NULL OR TRIM(vendor) = ''
   OR amount IS NULL

UNION ALL

-- AMT-02: Flag zero or negative transaction amounts.
SELECT
    'AMT-02',
    'Zero or negative amount',
    row_id,
    transaction_id,
    transaction_date,
    employee_id,
    vendor,
    amount,
    department,
    payment_method
FROM transactions
WHERE amount <= 0;