
"""Simple Data Sync Validator

Compares two in-memory data sets (simulating source and destination)
and reports any mismatched records and missing destination records.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def validate_sync(source_data, destination_data):
    """
    Compare records from source and destination and detect mismatches.

    Returns:
        (mismatches, missing)
        - mismatches: list of tuples (record_id, source_value, dest_value)
        - missing: list of record_ids present in source but missing in destination
    """
    mismatches = []
    missing = []

    for record_id, source_value in source_data.items():
        # If the record id does not exist in destination, record it as missing
        if record_id not in destination_data:
            missing.append(record_id)
            continue

        dest_value = destination_data.get(record_id)
        if dest_value != source_value:
            mismatches.append((record_id, source_value, dest_value))

    return mismatches, missing


if __name__ == "__main__":
    # Example data simulation
    source = {"A": 10, "B": 20, "C": 30}
    destination = {"A": 10, "B": 25, "C": 30}

    logging.info("Starting sync validation...")

    mismatched, missing = validate_sync(source, destination)

    if not mismatched and not missing:
        logging.info("✅ All records are consistent!")
    else:
        if missing:
            for mid in missing:
                logging.warning("Missing in destination: ID = %s", mid)

        if mismatched:
            logging.warning("⚠️ Mismatched Records Found:")
            for rec in mismatched:
                logging.warning("ID: %s | Source: %s | Destination: %s", *rec)
