#!/usr/bin/python3
"""
Returns information about an employee's TODO list progress.
And export data to JSON format
"""
import json
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
        username = user['username']
        json_filename = f'{ID}.json'

        json_data = {
            ID: [
                {
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": username
                }
                for todo in todos
            ]
        }

        with open(json_filename, mode='w') as json_file:
            json.dump(json_data, json_file)
    except Exception as e:
        print(f'Error: {e}')
