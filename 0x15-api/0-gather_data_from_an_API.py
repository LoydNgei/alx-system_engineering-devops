#!/usr/bin/python3
"""Fetching json data from an api"""

import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1].strip()
    user_url = "https://jsonplaceholder.typicode.com/users" + user_id
    user_dictionary = requests.get(user_url).json()
    user_name = user_dictionary.get("name")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()
    total = 0
    titles = []
    number = 0

    for item in todos:
        if item.get("userId") == int(user_id):
            total += 1
            if item.get("completed") is True:
                number += 1
                titles.append(item.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user_name, number, total))
    for title in titles:
        print("\t {}".format(title))
