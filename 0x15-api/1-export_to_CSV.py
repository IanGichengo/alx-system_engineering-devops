#!/usr/bin/python3
''' records all tasks owned by the employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"'''

import csv
import requests
import sys


def fetch_employee_data(employee_id):
    """Fetch employee data and TODO list from the API."""
    try:
        user_url = (f'https://jsonplaceholder.typicode.com/users/'
                    f'{employee_id}')
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        todos_url = (f'https://jsonplaceholder.typicode.com/todos?userId='
                     f'{employee_id}')
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        return user_data, todos_data
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        sys.exit(1)


def export_to_csv(employee_id):
    """Export the TODO list for the given employee to a CSV file."""
    user_data, todos_data = fetch_employee_data(employee_id)

    employee_name = user_data.get('name')

    with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos_data:
            writer.writerow({'USER_ID': employee_id,
                             'USERNAME': employee_name,
                             'TASK_COMPLETED_STATUS': task['completed'],
                             'TASK_TITLE': task['title']})


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
