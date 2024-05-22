#!/usr/bin/python3
'''Export data in CSV format'''

import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_data = requests.get(url).json()
    username = user_data.get("username")
    todos = requests.get(f"{url}/todos").json()
    filename = f"{user_id}.csv"

    with open(filename, 'w') as csvfile:
        for task in todos:
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                task.get("userId"), username, task.get("completed"),
                task.get("title")
            ))
