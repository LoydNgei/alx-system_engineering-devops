#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    user_dict = {}
    for user in users:
        user_id = user.get('id')
        user_name = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        user_dict[user_id] = []
        for task in tasks:
            user_dict[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user_name
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_dict, file)
