#!/usr/bin/python3
"""
Module to recursively query the Reddit API, parse the titles of all hot articles, and print a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, counts={}, after=""):
    """Recursively queries the Reddit API, parses titles of hot articles, and prints a sorted count of given keywords."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return
    
    data = response.json().get('data', {})
    titles = [post.get('data', {}).get('title').lower() for post in data.get('children', [])]
    
    for title in titles:
        for word in word_list:
            word_lower = word.lower()
            if word_lower in title.split():
                counts[word_lower] = counts.get(word_lower, 0) + 1
    
    after = data.get('after', None)
    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
    else:
        count_words(subreddit, word_list, counts, after)
