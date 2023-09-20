#!/usr/bin/python3
''' Module 0-gather_data_from_an_API that manipulate an API '''
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

    for i in to_do:
        if i['userId'] == emp_id:
            t_count += 1
        if (i['completed'] and i['userId'] == emp_id):
            t_done += 1

    name = None
    for i in employee:
        if i['id'] == emp_id:
            name = i['name']

    print(
            'Employee {} is done with tasks({}/{}):'
            .format(name, t_done, t_count)
            )

    for task in to_do:
        if task['completed'] is True and task['userId'] == emp_id:
            print(f"\t {task['title']}")
