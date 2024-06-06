#!/usr/bin/python3
''' returns the number of subscribers '''
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My Reddit Subscribers Checker"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data["data"]["subscribers"]
    except (requests.RequestException, KeyError):
        return 0
