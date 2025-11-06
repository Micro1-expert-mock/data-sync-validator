# 🧩 Data Sync Validator

A lightweight utility to validate data consistency between two systems during synchronization.

## 🚀 Features
 Verifies record parity between source and destination.
 Provides mismatch summary and integrity metrics.
 Runs cleanly in CI/CD environments.

## 🛠️ Quick Start
```bash
# Clone the repo
git clone https://github.com/Micro1-expert-mock/data-sync-validator.git
cd data-sync-validator

# Run the validator
python sync_validator.py
```

## 🐞 Bug fix — Missing destination records (Issue #2)

Behavior before: If a record existed in the source but not in the destination it was reported as a generic mismatch.

Fix implemented: `validate_sync` now separates two cases:
- "missing" — record IDs that are present in source but absent in destination
- "mismatches" — record IDs that exist in both but have different values

When a record is present in source but missing in destination the script now logs:

	Missing in destination: ID = X

Quick test (example):

```bash
# run a small one-off check that demonstrates a missing destination record
python -c "from sync_validator import validate_sync; m, miss = validate_sync({'A':1,'B':2,'C':3,'D':4},{'A':1,'B':2,'C':3});\
print('mismatches =', m);\
print('missing =', miss)"
```

Sample logger output when a source-only ID exists (script run):

```
WARNING Missing in destination: ID = D
WARNING ⚠️ Mismatched Records Found:
ID: B | Source: 20 | Destination: 25
```

If you want, I can add a tiny unit test that asserts the missing/mismatch behavior and run it as part of CI.

