#!/usr/bin/python3
# For a given employee ID, returns information about his/her TO-DO list progress

import requests
import sys

def fetch_employee_data(employee_id):
    """Fetch employee data and TODO list from the API."""
    try:
        # Fetch user data
        user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
        user_response.raise_for_status()
        user_data = user_response.json()

        # Fetch TODO list data
        todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        return user_data, todos_data
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        sys.exit(1)

def display_todo_progress(employee_id):
    """Display the TODO list progress for the given employee."""
    user_data, todos_data = fetch_employee_data(employee_id)

    # Get employee name
    employee_name = user_data.get('name')

    # Calculate the number of completed tasks and total tasks
    completed_tasks = [task for task in todos_data if task['completed']]
    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    # Display the TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
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
