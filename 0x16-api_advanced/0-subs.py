#!/usr/bin/python3
''' returns the number of subscribers '''
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subs = data.get('data').get('subscribers')
        return subs
    else:
        return 0
