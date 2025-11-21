"""
===============================================================================
Data Report - Social Network
===============================================================================
Purpose:
    - Load the social network data from JSON
    - Display all users, their friends, and liked pages
    - Display all pages available in the dataset

File Used:
    - data.json

Main Functions:
    - load_data(filename): Loads JSON data from a file
    - data_report(info): Prints users, their connections, and liked pages
===============================================================================
"""

import json

def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

info = load_data("data.json")

print(info)

# Write a function to display users and their connections
def data_report(info):
    print("User Information and their Connections")
    for user in info["users"]:
        print(f"ID.{user['id']} - {user['name']} is friend with: {user['friends']} and their Liked pages are {user['liked_pages']}")
    print("\nUsers Page Information")
    for page in info["pages"]:
        print(f"{page['id']}: {page['name']}")

print(data_report(info))
