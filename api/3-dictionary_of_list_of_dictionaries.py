#!/usr/bin/python3
""" Module that return a dictionary in json format from an API """
import json
import requests


root = 'https://jsonplaceholder.typicode.com'


def all_data() -> dict:
    ''' Method that returns all data from the api '''

    ''' Get the data from 2 endpoint with only one requests '''
    users = requests.get(f"{root}/users?_embed=todos").json()

    ''' Create an empty dict'''
    all_tasks = {}

    ''' Add the data to the dict all_tasks'''
    for user in users:
        u_id = user['id']
        username = user['username']
        todo_data = user['todos']

        all_tasks[
            str(u_id)] = [{'username': username, 'task': task['title'],
                           'completed': task['completed']}
                          for task in todo_data]
    return all_tasks


def export_to_json():
    ''' Method that export the data from the api to a json file'''
    all_tasks = all_data()

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file, indent=None)


if __name__ == '__main__':
    export_to_json()
