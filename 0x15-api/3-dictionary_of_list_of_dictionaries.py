#!/usr/bin/python3
"""
    Python script that, using this REST API
    (https://jsonplaceholder.typicode.com/), extend your Python
    script to export data in the JSON format.
"""
if __name__ == "__main__":
    import json
    import requests
    import sys
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    r_users = requests.get(url_users)
    r_todos = requests.get(url_todos)
    users_dict = {}
    list_users = r_users.json()
    list_todos = r_todos.json()
    for user in list_users:
        list_of_todos = []
        users_dict[user.get('id')] = list_of_todos
        for todo in list_todos:
            if users_dict[user.get('id')] == todo.get('userId'):
                todo_dict = {}
                todo_dict["username"] = user.get('username')
                todo_dict["task"] = todo.get('title')
                todo_dict["completed"] = todo.get('completed')
                list_of_todos.append(todo_dict)
    with open('todo_all_employees.json', 'w') as outfile:
        json.dump(users_dict, outfile)
