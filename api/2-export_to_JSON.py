#!/usr/bin/python3
''' Module export_to_JSON that export the data to a JSON file '''
import json
import requests
import sys


if __name__ == '__main__':

    emp_id = int(sys.argv[1])

    url = 'https://jsonplaceholder.typicode.com'

    ''' Get the employees list '''
    employee = requests.get(f'{url}/users').json()

    ''' Get the to do list '''
    to_do = requests.get(f'{url}/todos').json()

    t_count = 0
    t_done = 0

    ''' Get the data of the to do list '''
    for i in to_do:
        if i['userId'] == emp_id:
            t_count += 1
        if (i['completed'] and i['userId'] == emp_id):
            t_done += 1

    ''' Get the data of the employee list '''
    name = None
    for i in employee:
        if i['id'] == emp_id:
            name = i['name']

    ''' Format JSON'''
    user_data = {
        f'{emp_id}': [
            {
                "task": f"{task['title']}",
                "completed": f"{task['completed']}",
                "username": f"{employ['username']}"
            }
            for task in to_do if task['userId'] == emp_id
            for employ in employee if employ['id'] == emp_id
        ]
    }

    ''' Export the data to a json file '''
    json_file = f'{emp_id}.json'
    with open(json_file, mode='w') as file:
        json.dump(user_data, file)

