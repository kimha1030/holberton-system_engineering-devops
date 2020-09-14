#!/usr/bin/python3
"""Task 0. Gather data from an API"""
import requests
import sys


def GetUser():
    """According to user_id, show information"""
    UrlTodos = "https://jsonplaceholder.typicode.com/todos/?userId={:}".format(
        sys.argv[1])
    DataTask = requests.get(UrlTodos).json()

    UrlInfo = "https://jsonplaceholder.typicode.com/users/{:}".format(
        sys.argv[1])
    DataInfo = requests.get(UrlInfo).json()

    params = "userId={:}&completed=true".format(sys.argv[1])
    UrlCompleted = "https://jsonplaceholder.typicode.com/todos/?" + params
    DataCompleted = requests.get(UrlCompleted).json()

    EMPLOYEE_NAME = DataInfo.get("name")
    NUMBER_OF_TASKS = len(DataCompleted)
    TOTAL_NUMBER = len(DataTask)
    print("Employee {:} is done with tasks({:}/{:}):".format(EMPLOYEE_NAME,
                                                             NUMBER_OF_TASKS,
                                                             TOTAL_NUMBER
                                                             ))
    for i in DataCompleted:
        TASK_TITLE = i.get("title")
        print("  {}".format(TASK_TITLE))


if __name__ == "__main__":
    GetUser()
