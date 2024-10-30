DATASET_ID = "d_8b84c4ee58e3cfc0ece0d773c8ca6abc"

import json
import requests
import time
import pandas as pd

base_url = "https://api-production.data.gov.sg"
url = base_url + f"/v2/public/api/datasets/{DATASET_ID}/metadata"
print(url)
response = requests.get(url)
data = response.json()['data']
columnMetadata = data.pop('columnMetadata', None)

print("Dataset Metadata:")
print(json.dumps(data, indent=2))

print("\nColumns:\n", list(columnMetadata['map'].values()))

# Initiate download
initiate_download_response = requests.get(
    f"https://api-open.data.gov.sg/v1/public/api/datasets/{DATASET_ID}/initiate-download",
    headers={"Content-Type": "application/json"},
    json={}
)

print(initiate_download_response.json())

MAX_POLLS = 5
DOWNLOAD_URL = None

for i in range(MAX_POLLS):
    poll_download_response = requests.get(
        f"https://api-open.data.gov.sg/v1/public/api/datasets/{DATASET_ID}/poll-download",
        headers={"Content-Type": "application/json"},
        json={}
    )
    print(poll_download_response.json())
    
    if "url" in poll_download_response.json()['data']:
        DOWNLOAD_URL = poll_download_response.json()['data']['url']
        print("Download URL:", DOWNLOAD_URL)
        
        # Load the dataset into a DataFrame
        df = pd.read_csv(DOWNLOAD_URL)
        
        # Save the DataFrame as a CSV file locally
        df.to_csv("data/downloaded_data.csv", index=False)
        print("Data saved to 'downloaded_data.csv'")
        break
    
    if i == MAX_POLLS - 1:
        print(f"{i + 1}/{MAX_POLLS}: No result found, possible error with dataset, please try again or let us know at https://go.gov.sg/datagov-supportform\n")
    else:
        print(f"{i + 1}/{MAX_POLLS}: No result yet, continuing to poll\n")
    
    time.sleep(3)
