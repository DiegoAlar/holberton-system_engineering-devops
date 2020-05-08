#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
from re import search
import requests


def count_words(subreddit, word_list, after='', a_dict=None):
    """  Recurse it!  """
    if a_dict is None:
        a_dict = {}
        for item in word_list:
            if search('_', item):
                pass
            else:
                a_dict[item] = 0
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
            for word in word_list:
                if search(r'\b{}\b'.format(word), title):
                    a_dict[word] += 1
        count_words(subreddit, word_list, next_after, a_dict)
    else:
        sorted_dict = sorted(a_dict.items(), key=lambda x: x[1], reverse=True)
        for item in sorted_dict:
            print('{}: {}'.format(item[0], item[1]))
