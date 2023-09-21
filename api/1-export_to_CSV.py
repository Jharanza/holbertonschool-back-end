#!/usr/bin/python3
''' Module that manipulate an API and export it to a CSV file '''
import csv
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

    ''' Get the ttotal tasks and the completed tasks '''
    for i in to_do:
        if i['userId'] == emp_id:
            t_count += 1
        if (i['completed'] and i['userId'] == emp_id):
            t_done += 1

    ''' Get the name of the emploee '''
    name = None
    for i in employee:
        if i['id'] == emp_id:
            name = i['name']

    ''' Export data to CVS file '''
    csv_name = f'{emp_id}.csv'
    with open(csv_name, mode='w', newline='') as file:
        csv_writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)

        ''' Get the username and the list to do and save it in the file '''
        username = None
        for employ in employee:
            if employ['id'] == emp_id:
                username = employ['username']
        for task in to_do:
            if task['userId'] == emp_id:
                csv_writer.writerow(
                        [emp_id, username, task['completed'], task['title']]
                     )

    ''' Output '''
    print(
            'Employee {} is done with tasks({}/{}):'
            .format(name, t_done, t_count)
            )

    for task in to_do:
        if task['completed'] is True and task['userId'] == emp_id:
            print(f"\t {task['title']}")
