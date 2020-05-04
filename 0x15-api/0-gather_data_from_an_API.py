#!/usr/bin/python3
"""
    Python script that, using this REST API
    (https://jsonplaceholder.typicode.com/), for a given employee ID,
    returns information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import requests
    import sys
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    if len(sys.argv) == 2:
        list_of_todos = []
        total_tasks = 0
        completed = 0
        mge = 'Employee {} is done with tasks({}/{}):'
        r_users = requests.get(url_users)
        r_todos = requests.get(url_todos)

        try:
            list_users = r_users.json()
            list_todos = r_todos.json()
            for obj in list_todos:
                if obj.get('userId') == int(sys.argv[1]):
                    if obj.get('completed') is True:
                        list_of_todos.append(obj.get('title'))
                        completed += 1
                    total_tasks += 1
            for obj in list_users:
                if obj.get('id') == int(sys.argv[1]):
                    print(mge.format(obj.get('name'), completed, total_tasks))
            for task in list_of_todos:
                print('\t {}'.format(task))
        except ValueError:
            print("Not a valid JSON")
