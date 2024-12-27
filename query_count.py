import pandas as pd

# Load the CSV file directly
file_path = r"C:\Users\admin\Desktop\Project CRV2\grouped_data_with_embeddings.csv"
data = pd.read_csv(file_path)

# Define query terms
location_query = "London"
contact_query = "Financial"

# Filter rows where both conditions are met
matches = data[
    (data["town"].str.contains(location_query, case=False, na=False)) &
    (data["job_role_desc"].str.contains(contact_query, case=False, na=False))
]

# Output the results
print(f"Count of records where 'London' and 'Financial' appear in the same row: {len(matches)}")
print("\nMatching records:")
print(matches[["REFNUM", "town", "job_role_desc"]])
