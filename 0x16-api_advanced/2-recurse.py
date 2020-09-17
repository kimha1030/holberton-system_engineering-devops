#!/usr/bin/python3
"""Task 1. Top Ten"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """This function allow us generate a list with the titles"""
    userAgent = {'User-agent': 'Sure_Student_8276'}
    if after == "":
        urlReddit = "https://www.reddit.com/r/{}/hot.json?after=".format(
            subreddit)
    else:
        urlReddit = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
    req = requests.get(urlReddit, headers=userAgent)
    response_data = req.json()
    if req.status_code == 404:
        return None
    else:
        new_Dict = response_data['data']['children']
        for i in range(len(new_Dict)):
            hot_list.append(new_Dict[i]['data']['title'])
        after = response_data['data']['after']
        if after is None:
            return hot_list
        recurse(subreddit, hot_list, after)
        return hot_list
