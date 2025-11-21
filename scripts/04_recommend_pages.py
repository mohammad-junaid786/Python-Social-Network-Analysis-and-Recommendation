"""
===============================================================================
Posts You Might Like - Recommendation
===============================================================================
Purpose:
    - Recommend pages/posts a user might like
    - Use liked pages of other users with similar interests
    - Score pages based on how many common pages exist between users

File Used:
    - big_data.json

Main Functions:
    - load_data(filename): Loads JSON data from a file
    - find_post_you_might_liked(my_id, data):
        * Builds a mapping of user → liked pages
        * Finds common liked pages between users
        * Scores and ranks pages not yet liked by the user
===============================================================================
"""

import json

def load_data(filename):
    with open(filename, "r") as f:
        return json.load(f)

def find_post_you_might_liked(my_id, data):
    pages_dict = {}

    for user in data['users']:
        pages_dict[user['id']] = set(user['liked_pages'])

    if my_id not in pages_dict:
        return []

    my_pages = pages_dict[my_id]

    scores = {}

    for other_id, their_pages in pages_dict.items():
        if other_id != my_id:
            common_pages = my_pages.intersection(their_pages)

            for page in their_pages:
                if page not in my_pages:
                    scores[page] = scores.get(page, 0) + len(common_pages)

    sorted_list = sorted(scores.items(), key=lambda x:x[1], reverse=True)
    return [page_id for page_id, _ in sorted_list]

data = load_data("big_data.json")
my_id = 1
recc = find_post_you_might_liked(my_id, data)
print(recc)
