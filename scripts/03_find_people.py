"""
===============================================================================
People You May Know - Recommendation
===============================================================================
Purpose:
    - Suggest new people a user may know based on mutual friends
    - Use friend connections to calculate a score for each suggested user

File Used:
    - big_data.json

Main Functions:
    - load_data(filename): Loads JSON data from a file
    - find_people_you_may_know(my_id, data):
        * Builds a friends dictionary
        * Finds mutual friends
        * Ranks people by number of mutual friends
===============================================================================
"""

import json

def load_data(filename):
    with open(filename, "r") as f:
        return json.load(f)

def find_people_you_may_know(my_id, data):
    friends_dict = {}
    for user in data['users']:
        friends_dict[user['id']] = set(user['friends'])

    if my_id not in friends_dict:
        return []

    my_friends = friends_dict[my_id]

    score = {}
    for friend in my_friends:
        for mutual in friends_dict[friend]:
            if mutual != my_id and mutual not in my_friends:
                score[mutual] = score.get(mutual, 0)+1
    sorted_score = sorted(score.items(), key=lambda x:x[1], reverse=True)
    return[person_id for person_id, count in sorted_score]

data = load_data("big_data.json")
my_id = 1
recc = find_people_you_may_know(my_id, data)
print(recc)
