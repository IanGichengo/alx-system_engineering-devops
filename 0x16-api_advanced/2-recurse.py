#!/usr/bin/python3
"""
Module to recursively query the Reddit API and return a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Recursively queries the Reddit API and returns a list of titles of all hot articles."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return None
    
    data = response.json().get('data', {})
    hot_list.extend([post.get('data', {}).get('title') for post in data.get('children', [])])
    
    after = data.get('after', None)
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)

