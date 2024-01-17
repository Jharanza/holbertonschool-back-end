#!/usr/bin/python3
''' Module that extract data from an API and write it in an json file'''
import json
import requests
from sys import argv


url = 'https://jsonplaceholder.typicode.com'  # Principal root


def get_progress(employee_id) -> None:
    """ Method that take 2 endpoints and extract data about the same user """

    ''' Info to the endpoint users '''
    users = requests.get(f"{url}/users/{employee_id}")
    users_data = users.json()

    ''' Info to the endpoint to_do'''
    todos = requests.get(f"{url}/todos?userId={employee_id}")
    todos_data = todos.json()

    ''' export data to the export_to_json function '''
    export_to_json(employee_id, users_data, todos_data)


def export_to_json(user_id, users_data, todos_data) -> None:
    ''' Method that export the data to a file json'''

    ''' Assign the name of the file '''
    filename = f'{user_id}.json'

    ''' iterate over the values '''
    new_user = {user: value for user, value in users_data.items()}
    print(isinstance(new_user, dict))  # Check type of the iterable

    ''' Create the model of the response '''
    result_dict = {str(user_id): [
        {
            'task': task['title'],
            'completed': task['completed'],
            'username': new_user['username']
        }
        for task in todos_data if task['userId'] == user_id
    ]}

    ''' Write result_dict to a json file '''
    with open(filename, 'w') as file:
        json.dump(result_dict, file, indent=2)

    ''' Check result '''
    print(f'Data exported to {filename}')


if __name__ == '__main__':
    try:
        employee_id = int(argv[1])  # assign arg in position 1 to the variable
    except ValueError:
        print(ValueError)
    get_progress(employee_id)
