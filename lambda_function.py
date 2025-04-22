import csv
import io
from datetime import datetime, timedelta

def process_orders(input_file, output_file):
    print("Processing orders from the provided CSV file.")
    
    # Read the input CSV file
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as f:
            raw_csv = f.read().splitlines()
        print(f"Successfully read file: {input_file}")
    except Exception as e:
        print(f"Error reading file: {e}")
        raise e

    reader = csv.DictReader(raw_csv)
    filtered_rows = []
    original_count = 0
    filtered_out_count = 0
    cutoff_date = datetime.now() - timedelta(days=30)

    print("Processing records...")
    for row in reader:
        original_count += 1
        order_status = row['Status'].strip().lower()
        order_date = datetime.strptime(row['OrderDate'], "%Y-%m-%d")

        # Check if the order should be kept
        if order_status not in ['pending', 'cancelled'] or order_date > cutoff_date:
            filtered_rows.append(row)
        else:
            filtered_out_count += 1

    print(f"Total records processed: {original_count}")
    print(f"Records filtered out: {filtered_out_count}")
    print(f"Records kept: {len(filtered_rows)}")

    # Write the filtered rows to an output CSV file
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(filtered_rows)
        print(f"Filtered file successfully saved to: {output_file}")
    except Exception as e:
        print(f"Error writing filtered file: {e}")
        raise e

# Example usage:
input_file = 'orders.csv'  # Replace with your input CSV file path
output_file = 'filtered_orders.csv'  # Output file name
process_orders(input_file, output_file)
