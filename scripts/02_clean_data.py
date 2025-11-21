"""
===============================================================================
Data Cleaning - Social Network
===============================================================================
Purpose:
    - Clean the raw social network data
    - Remove users with missing names
    - Remove duplicate friends
    - Remove inactive users (no friends and no liked pages)
    - Remove duplicate pages based on page ID

File Used:
    - Input : data2.json
    - Output: cleaned_data_2.json

Main Functions:
    - clean_data(data): Cleans the users and pages data
===============================================================================
"""

import json

def clean_data(data):
    # Remove users with missing names
    data["users"] = [user for user in data["users"] if user["name"].strip()]
    
    # Remove duplicate friends
    for user in data["users"]:
        user["friends"] = list(set(user['friends']))
        
    # Remove the inactive users
    data['users'] = [user for user in data['users'] if user['friends'] or user['liked_pages']]

    # Remove duplicate pages
    unique_pages = {}
    for page in data["pages"]:
        unique_pages[page["id"]] = page
    data["pages"] = list(unique_pages.values())
    return data


#Load the Data
with open("data2.json", "r") as f:
    raw_data = json.load(f)

cleaned_data = clean_data(raw_data)

with open("cleaned_data_2.json", "w") as f:
    json.dump(cleaned_data, f, indent=4)
print("Data has been cleaned successfully")
