# Testing Methodology

## Purpose

Demonstrate basic, rule-based checks on a small fictional transaction dataset.

## Scope and data

The input is `data/raw/transactions.csv`. Every record is fictional and created for this learning project. The results are simulated examples, not real audit evidence or audit findings.

## Procedure

1. Load the CSV into a local SQLite database.
2. Run the documented SQL checks against the loaded records.
3. Review each flagged row and compare the results with the sample data.
4. Record the exceptions and note the limits of the checks.

## Planned control checks

| Check ID | Rule | Example to investigate |
| --- | --- | --- |
| DUP-01 | Flag transaction IDs that appear more than once. | TX1002 appears twice. |
| AMT-01 | Flag transactions above $50,000. | TX1004 is $74,250. |
| MISS-01 | Flag records missing a transaction date, employee ID, vendor, or amount. | TX1005 has no vendor. |
| AMT-02 | Flag zero or negative transaction amounts. | TX1011 has an amount of $0.00. |

## Limitations

These simple rules identify records for review; they do not establish fraud, error, or a control failure. The dataset is very small and intentionally includes examples for demonstration. Thresholds and required fields are assumptions for this exercise, not organization-approved criteria.