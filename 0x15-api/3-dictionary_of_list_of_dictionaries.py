#!/usr/bin/python3
"""
Returns information about an employee's TODO list progress.
And exports data to JSON format
"""
import json
import requests
import sys


if __name__ == '__main__':
    user_url = f'https://jsonplaceholder.typicode.com/users'
    todos_url = f'https://jsonplaceholder.typicode.com/todos'

    try:
        user_resp = requests.get(user_url)
        todos_resp = requests.get(todos_url)
        users = user_resp.json()
        todos = todos_resp.json()
        json_filename = 'todo_all_employees.json'

        json_data = {
            user['id']: [
                {
                    "username": user['username'],
                    "task": todo["title"],
                    "completed": todo["completed"]
                }
                for todo in todos if todo['userId'] == user['id']
            ]
            for user in users
        }

        with open(json_filename, mode='w') as json_file:
            json.dump(json_data, json_file)
    except Exception as e:
        print(f'Error: {e}')
