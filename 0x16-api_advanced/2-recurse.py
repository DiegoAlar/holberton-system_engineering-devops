#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """  Recurse it!  """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = {'user-agent': 'X-Modhash'}
    req = requests.get(url, headers=headers)
    if req.history or req.status_code == 404:
        return None
    data = req.json()
    next_after = data.get('data').get('after')
    if next_after:
        req = data.get('data').get('children')
        for title in req:
            title = title.get('data').get('title')
            hot_list.append(title)
        return recurse(subreddit, hot_list, next_after)
    else:
        return hot_list
