#!/usr/bin/python3
"""Task 2. Export to json"""
import json
import requests


def ListDictionaries():
    """According to user_id, export information in json"""
    UrlTodos = "https://jsonplaceholder.typicode.com/todos"
    DataTask = requests.get(UrlTodos).json()

    UrlInfo = "https://jsonplaceholder.typicode.com/users"
    DataInfo = requests.get(UrlInfo).json()

    new_dict = {}
    for info in DataInfo:
        USER_ID = info.get("id")
        USERNAME = info.get("username")
        my_list = []
        for task in DataTask:
            my_dict = {}
            if task.get("userId") == USER_ID:
                my_dict["task"] = task.get("title")
                my_dict["completed"] = task.get("completed")
                my_dict["username"] = USERNAME
                my_list.append(my_dict)
                my_dict = {}
        new_dict[USER_ID] = my_list

    FileName = "todo_all_employees.json"
    with open(FileName, 'w') as f:
        json.dump(new_dict, f)


if __name__ == "__main__":
    ListDictionaries()
