#!/usr/bin/python3
"""Task 1. Export to CSV"""
import csv
import requests
import sys


def ExportUser():
    """According to user_id, export information in CSV"""
    UrlTodos = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(
        sys.argv[1])
    DataTask = requests.get(UrlTodos).json()

    UrlInfo = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])
    DataInfo = requests.get(UrlInfo).json()

    USER_ID = sys.argv[1]
    USERNAME = DataInfo.get("username")
    FileName = USER_ID+".csv"
    with open(FileName, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in DataTask:
            writer.writerow([USER_ID, USERNAME, i.get("completed"),
                             i.get("title")])

if __name__ == "__main__":
    ExportUser()
