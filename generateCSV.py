import csv
import json

# Function to convert JSON data to CSV
def generateCSV(paragraphs_evaluated):
    # Specify the CSV file name
    csv_file_name = "categorized_file.csv"
    # Open the CSV file for writing
    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
        # Create a CSV writer
        writer = csv.writer(file)

        # Write the header
        writer.writerow(["text", "category_ID", "paragraph_number"])

        # Write the data
        for item in paragraphs_evaluated:
            writer.writerow([item["text"], item["category_ID"], item["paragraph_number"]])
			
    print(paragraphs_evaluated)
