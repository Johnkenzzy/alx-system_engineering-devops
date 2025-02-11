#!/usr/bin/python3
"""
Returns information about an employee's TODO list progress.
"""
import csv
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
        usrn = user['username']
        csv_filename = f'{ID}.csv'

        with open(csv_filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for todo in todos:
                writer.writerow([ID, usrn, todo['completed'], todo['title']])
    except Exception as e:
        print(f'Error: {e}')
