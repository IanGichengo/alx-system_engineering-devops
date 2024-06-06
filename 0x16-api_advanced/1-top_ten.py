#!/usr/bin/python3
''' the top ten '''
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My Reddit Hot Posts Viewer"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        posts = data["data"]["children"][:10]  # Get the first 10 posts
        for post in posts:
            print(post["data"]["title"])
    except (requests.RequestException, KeyError):
        print("None")
