#!/usr/bin/python3
''' Module that extract data from an API '''
import requests
from sys import argv


def get_progress(employee_id) -> None:
    """ Method that take 2 endpoints and extract data about the same user """

    url = 'https://jsonplaceholder.typicode.com'  # Principal root

    ''' Info to the endpoint users '''
    users = requests.get(f"{url}/users/{employee_id}")
    users_data = users.json()

    ''' Info to the endpoint to_do'''
    todos = requests.get(f"{url}/todos?userId={employee_id}")
    todos_data = todos.json()

    '''Tasks completed'''
    completed_task = [task for task in todos_data if task['completed']]

    ''' All tasks'''
    tasks = [task for task in todos_data]

    print("Employee {} is done with tasks ({}/{}):"
          .format(users_data['name'], len(completed_task), len(tasks)))

    for task in completed_task:
        print('\t {}'.format(task['title']))


if __name__ == '__main__':
    try:
        employee_id = int(argv[1])  # assign arg in position 2 to the variable
    except ValueError:
        print(ValueError)
    get_progress(employee_id)
