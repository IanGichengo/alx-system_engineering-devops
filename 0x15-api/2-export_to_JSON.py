#!/usr/bin/python3
'''Extend Python script to export data in JSON format'''

import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_data = requests.get(url).json()
    username = user_data.get("username")
    todos = requests.get(f"{url}/todos").json()
    filename = f"{user_id}.json"
    user_tasks = []

    for task in todos:
        task_info = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
        }
        user_tasks.append(task_info)

    user_data = {user_id: user_tasks}

    with open(filename, 'w') as file:
        json.dump(user_data, file, indent=4)
