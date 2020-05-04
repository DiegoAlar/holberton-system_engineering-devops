#!/usr/bin/python3
"""
    Python script that, using this REST API
    (https://jsonplaceholder.typicode.com/), for a given employee ID,
    returns information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import csv
    import requests
    import sys
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    if len(sys.argv) == 2:
        r_users = requests.get(url_users)
        r_todos = requests.get(url_todos)
        list_of_todos = []
        try:
            list_users = r_users.json()
            list_todos = r_todos.json()
            for user in list_users:
                if user.get('id') == int(sys.argv[1]):
                    username = user.get('username')
                    with open(sys.argv[1] + ".csv", mode="w") as csvfile:
                        f = csv.writer(
                            csvfile,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
                        # f.writerow(["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"])
                        for todo in list_todos:
                            if todo.get('userId') == int(sys.argv[1]):
                                f.writerow(
                                    [
                                        todo.get("userId"),
                                        username,
                                        todo.get("completed"),
                                        todo.get("title")
                                    ])
        except ValueError:
            print("Not a valid JSON")
