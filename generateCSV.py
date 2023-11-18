import csv
import json

# Function to convert JSON data to CSV
def generateCSV(paragraphs_evaluated):

    print(paragraphs_evaluated)
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
            print(item)
            writer.writerow([item["text"], item["category_ID"], item["paragraph_number"], item["relevancy_score"]])


# test = """
# [
#     {
#         "text": "Recommendations People have the right to be involved in discussions and make informed decisions about their care, as described in your care. Making decisions using NICE guidelines explains how we use words to show the strength (or certainty) of our recommendations, and has information about professional guidelines, standards and laws (including on consent and mental capacity), and safeguarding. NICE has also produced a patient decision aid to support discussions about statin therapy to reduce the risk of coronary heart disease and stroke.",
#         "category_ID": 6,
#         "paragraph_number": "1"
#     },
#     {
#         "text": "Identifying and assessing cardiovascular disease risk Identifying people for full formal risk assessment",
#         "category_ID": 1,
#         "paragraph_number": "1.1"
#     },
#     {
#         "text": "For the primary prevention of CVD in primary care, use a systematic strategy to identify people who are likely to be at high risk. [2008, amended 2014]",
#         "category_ID": 1,
#         "paragraph_number": "1.1.1"
#     },
#     {
#         "text": "Prioritise people on the basis of an estimate of their CVD risk before a full formal risk assessment. Estimate their CVD risk using CVD risk factors already recorded in primary care electronic medical records. [2008]",
#         "category_ID": 1,
#         "paragraph_number": "1.1.2"
#     },
#     {
#         "text": "People older than 40 should have their estimate of CVD risk reviewed on an ongoing basis. [2008]",
#         "category_ID": 3,
#         "paragraph_number": "1.1.3"
#     },
#     {
#         "text": "Prioritise people for a full formal risk assessment if their estimated 10-year risk of CVD is 10% or more. [2008, amended 2014]",
#         "category_ID": 1,
#         "paragraph_number": "1.1.4"
#     },
#     {
#         "text": "Discuss the process of risk assessment with the person identiNed as being at risk, including the option of declining any formal risk assessment. [2008]",
#         "category_ID": 1,
#         "paragraph_number": "1.1.5"
#     },
#     {
#         "text": "Do not use opportunistic assessment as the main strategy in primary care to identify CVD risk in unselected people. [2008]",
#         "category_ID": 1,
#         "paragraph_number": "1.1.6"
#     }
# ]
# """

# generateCSV(json.loads(test))