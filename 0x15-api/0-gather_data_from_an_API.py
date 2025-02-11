#!/usr/bin/python3
"""
Returns information about an employee's TODO list progress.
"""
import requests
import sys


if __name__ == '__main__':
    ID = int(sys.argv[1])
    user_url = f'https://jsonplaceholder.typicode.com/users/{ID}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={ID}'

    try:
        user_resp = requests.get(user_url)
        todos_resp = requests.get(todos_url)
        user = user_resp.json()
        todos = todos_resp.json()
        name = user['name']
        total = len(todos)
        completed = 0
        for todo in todos:
            if todo['completed']:
                completed += 1
        print(f'Employee {name} is done with tasks({completed}/{total}):')

        for todo in todos:
            print(f"     {todo['title']}")
    except Exception as e:
        print(f'Error: {e}')
