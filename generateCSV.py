import csv
import json

CATEGORIES = {
    1: "Diagnostic recommendation",
    2: "Medication and other therapeutic recommendation",
    3: "Monitoring and follow-up recommendation",
    4: "Possible interactions with other guidelines, including comorbidities",
    5: "Early warning signs, estimation of risk and poor evolution",
    6: "No Category"
}

# Function to convert JSON data to CSV
def generateCSV(paragraphs_evaluated):
    """
    Function to convert JSON data to CSV. Writes the CSV file to the current directory.

    :param paragraphs_evaluated: JSON data
    :return: None
    """

    print(paragraphs_evaluated)
    # Specify the CSV file name
    csv_file_name = "categorized_clinical_guideline.csv"
    # Open the CSV file for writing
    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
        # Create a CSV writer
        writer = csv.writer(file)

        # Write the header
        writer.writerow(["Paragraph", "Category", "Paragraph Number", "Relevancy Score"])

        # Write the data
        for item in paragraphs_evaluated:
            print(item)
            category = CATEGORIES[item["category_ID"]]
            writer.writerow([item["text"], category, item["paragraph_number"], item["relevancy_score"]])
