#!/usr/bin/python3
"""Task 1. Top Ten"""
import requests


def top_ten(subreddit):
    """This function allow us generate the hot titles"""
    userAgent = {'User-agent': 'Sure_Student_8276'}
    urlReddit = "https://www.reddit.com/r/{}/hot.json?limit=10".format(
        subreddit)
    req = requests.get(urlReddit, headers=userAgent)
    response_data = req.json()
    if req.status_code == 404:
        return (0)
    else:
        new_Dict = response_data['data']['children']
        for i in range(len(new_Dict)):
            print("{:}".format(
                new_Dict[i]['data']['title']))
