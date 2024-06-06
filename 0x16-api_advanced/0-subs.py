#!/usr/bin/python3
''' outputs the number of subs '''
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API, returns number of subscribers for a subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My Reddit Subscribers Checker"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data["data"]["subscribers"]
    except (requests.RequestException, KeyError):
        return 0
