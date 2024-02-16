import csv
import json


def json_to_csv(json_file, csv_file):
    # Read JSON file and convert it to CSV
    with open(json_file, 'r') as jsonfile:
        data = json.load(jsonfile)

    # Get field names from the first record
    field_names = list(data[0].keys())

    # Write data to CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    json_file = input("Enter the JSON file name: ")
    csv_file = input("Enter the CSV file name (output): ")

    json_to_csv(json_file, csv_file)
    print(f"Conversion from {json_file} to {csv_file} is complete.")
