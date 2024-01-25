#!/usr/bin/python3
''' Module that extract data from an API and store it in a CSV file '''
import csv
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

    ''' All tasks'''
    tasks = [task for task in todos_data]

    ''' Export the data to the export_to_csv function '''
    export_to_csv(employee_id, users_data["username"], tasks)


def export_to_csv(user_id, username, tasks):
    ''' Method that export the data from the api to the csv file '''
    filename = f'{user_id}.csv'

    ''' Write the csv with the data '''
    with open(filename, mode='wt', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([str(user_id), username,
                             task['completed'], task['title']])

    print(f'Data exported to {filename}')


if __name__ == '__main__':
    try:
        employee_id = int(argv[1])  # assign arg in position 1 to the variable
    except ValueError:
        print(ValueError)
    get_progress(employee_id)
