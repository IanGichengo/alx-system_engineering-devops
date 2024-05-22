#!/usr/bin/python3
'''Export data in JSON format for all employees'''

import json
import requests

if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/users/"
    employees = requests.get(base_url).json()
    filename = 'todo_all_employees.json'
    all_tasks = {}

    for employee in employees:
        username = employee.get('username')
        user_id = str(employee.get('id'))
        user_tasks = requests.get(f"{base_url}{user_id}/todos").json()
        all_tasks[user_id] = []
        for task in user_tasks:
            all_tasks[user_id].append({
                'username': username,
                'task': task.get('title'),
                'completed': task.get('completed')
            })

    with open(filename, 'w') as f:
        json.dump(all_tasks, f)
