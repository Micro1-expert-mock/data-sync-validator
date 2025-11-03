
---

### 🧠 **sync_validator.py**
```python
"""
Simple Data Sync Validator

Compares two in-memory data sets (simulating source and destination)
and reports any mismatched records.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def validate_sync(source_data, destination_data):
    """
    Compare records from source and destination and detect mismatches.
    """
    mismatches = []

    for record_id, source_value in source_data.items():
        dest_value = destination_data.get(record_id)
        if dest_value != source_value:
            mismatches.append((record_id, source_value, dest_value))

    return mismatches


if __name__ == "__main__":
    # Example data simulation
    source = {"A": 10, "B": 20, "C": 30}
    destination = {"A": 10, "B": 25, "C": 30}

    logging.info("Starting sync validation...")

    mismatched = validate_sync(source, destination)

    if not mismatched:
        logging.info("✅ All records are consistent!")
    else:
        logging.warning("⚠️ Mismatched Records Found:")
        for rec in mismatched:
            logging.warning("ID: %s | Source: %s | Destination: %s", *rec)
