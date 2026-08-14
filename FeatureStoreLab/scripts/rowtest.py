import csv
 
 
def compare_row_counts(file1_path, file2_path):
    """Compares the total number of data rows between two CSV files."""
 
    def count_rows(file_path):
        with open(file_path, mode="r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            # Skip header row. Remove next() if your files have no headers.
            next(reader, None)
            # Sum 1 for every remaining row efficiently
            return sum(1 for _ in reader)
 
    try:
        count1 = count_rows(file1_path)
        count2 = count_rows(file2_path)
    except FileNotFoundError as e:
        print(f"❌ Error: {e.filename} could not be found.")
        return
 
    print("📊 Row Count Summary:")
    print(f"  • {file1_path}: {count1} rows")
    print(f"  • {file2_path}: {count2} rows")
 
    if count1 == count2:
        print("✅ Success: Both files have the exact same number of rows!")
    else:
        diff = abs(count1 - count2)
        print(f"❌ Mismatch: Files differ by {diff} row(s).")
 
 
# --- Working Execution ---
# Pass your specific file paths here as quoted strings:
compare_row_counts("../data/billing_data.csv", "../data/customer_features.csv")