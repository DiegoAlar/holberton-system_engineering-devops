#!/usr/bin/python3
"""
    Python script that, using this REST API
    (https://jsonplaceholder.typicode.com/) for a given employee ID,
    returns information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import json
    import requests
    import sys
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    if len(sys.argv) == 2:
        r_users = requests.get(url_users)
        r_todos = requests.get(url_todos)
        list_of_todos = []
        user_dict = {
            sys.argv[1]: list_of_todos
        }
        try:
            list_users = r_users.json()
            list_todos = r_todos.json()
            for user in list_users:
                if user.get('id') == int(sys.argv[1]):
                    username = user.get('username')
                    for todo in list_todos:
                        if todo.get('userId') == int(sys.argv[1]):
                            todo_dict = {}
                            todo_dict["task"] = todo.get('title')
                            todo_dict["completed"] = todo.get('completed')
                            todo_dict["username"] = username
                            list_of_todos.append(todo_dict)
                    with open(sys.argv[1] + '.json', 'w') as outfile:
                        json.dump(user_dict, outfile)
        except ValueError:
            print("Not a valid JSON")
