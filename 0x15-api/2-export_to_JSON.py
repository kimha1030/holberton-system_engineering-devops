#!/usr/bin/python3
"""Task 2. Export to json"""
import json
import requests
import sys


def ExportJSON():
    """According to user_id, export information in json"""
    UrlTodos = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(
        sys.argv[1])
    DataTask = requests.get(UrlTodos).json()

    UrlInfo = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])
    DataInfo = requests.get(UrlInfo).json()

    USER_ID = sys.argv[1]
    USERNAME = DataInfo.get("username")

    my_list = []
    for i in DataTask:
        my_dict = {}
        TASK_TITLE = i.get("title")
        my_dict["task"] = TASK_TITLE
        TASK_COMPLETED_STATUS = i.get("completed")
        my_dict["completed"] = TASK_COMPLETED_STATUS
        my_dict["username"] = USERNAME
        my_list.append(my_dict)

    new_dict = {}
    new_dict = {USER_ID: my_list}

    FileName = USER_ID+".json"
    with open(FileName, 'w') as f:
        json.dump(new_dict, f)


if __name__ == "__main__":
    ExportJSON()
