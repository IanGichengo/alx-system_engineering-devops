#!/usr/bin/python3
'''For a given employee ID, information about his/her TO-DO list progress'''

import requests
import sys


def fetch_employee_data(employee_id):
    """Fetch employee data and TODO list from the API."""
    try:
        user_url = (f'https://jsonplaceholder.typicode.com'
                    f'/users/{employee_id}')
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        todos_url = (f'https://jsonplaceholder.typicode.com'
                     f'/todos?userId={employee_id}')
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        return user_data, todos_data
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        sys.exit(1)


def display_todo_progress(employee_id):
    """Display the TODO list progress for the given employee."""
    user_data, todos_data = fetch_employee_data(employee_id)

    employee_name = user_data.get('name')

    completed_tasks = [task for task in todos_data if task['completed']]
    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks("
          f"{number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        display_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
