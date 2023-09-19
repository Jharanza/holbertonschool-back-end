#!/usr/bin/python3
''' Module 0-gather_data_from_an_API that manipulate an API '''
import requests
import sys



if __name__ == '__main__':

    employee_id = sys.argv[1]
    
    url_base = 'https://jsonplaceholder.typicode.com/'

    ''' Get the employee information and transform it in json format '''
    response_employee = requests.get(f'{url_base}users/{employee_id}')
    employee_data = response_employee.json()

    ''' Get the todo list information and transform it in json format '''
    response_todo_list = requests.get(f'{url_base}todos/?userId={employee_id}')
    todo_list_data = response_todo_list.json()

    ''' Number of task finished and total tasks '''
    len_completed = len([task for task in todo_list_data if task['completed']])
    total_tasks = len(todo_list_data)

    ''' Display the progress '''
    print(f"Employee {employee_data['name']} is done with tasks\
            ({len_completed}/{total_tasks}):")
    for task in todo_list_data:
        print(f"\t {task['title']}")

    if response_employee.status_code == 200:
        content = response_employee.content
