#!/usr/bin/python3
"""Task 0. How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """This function allow generate the count of suscribers"""
    userAgent = {'User-agent': 'Sure_Student_8276'}
    urlReddit = "https://www.reddit.com/r/" + subreddit + "/about.json"
    req = requests.get(urlReddit, headers=userAgent)
    reqJson = req.json()
    if req.status_code == 404:
        return (0)
    else:
        return(reqJson["data"]["subscribers"])
