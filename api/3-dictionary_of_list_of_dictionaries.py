#!/usr/bin/python3
''' Dictionary_of_list_of_dictionaries that export data to a json file '''
import json
import requests
import sys


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com'

    ''' Get the employees list '''
    employee = requests.get(f'{url}/users').json()

    ''' Create the dictionary '''
    data_employees = {}

    for users in employee:
        user_id = users['id']
        username = users['username']

        to_do = requests.get(f'{url}/todos?userId={user_id}').json()
        employ_task = [
                {
                    'username': username,
                    'task': task['title'],
                    'completed': task['completed']
                }
                for task in to_do
            ]
        data_employees[user_id] = employ_task

    ''' Export to json file '''
    json_file = 'todo_all_employees.json'
    with open(json_file, mode='w') as file:
        json.dump(data_employees, file)
