#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import re
import requests


def count_words(subreddit, word_list, after='', a_dict=None):
    """  Recurse it!  """
    if a_dict is None:
        a_dict = {}
        a_list = []
        for item in word_list:
            if re.search('_', item):
                pass
            elif item.lower() in a_dict:
                a_dict[item] += 1
            else:
                a_dict[item.lower()] = 0
                a_list.append(item.lower())
                word_list = a_list
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = {'user-agent': 'X-Modhash'}
    req = requests.get(url, headers=headers)
    if req.history or req.status_code == 404:
        print()
    else:
        data = req.json()
        next_after = data.get('data').get('after')
        if next_after:
            req = data.get('data').get('children')
            for title in req:
                title = title.get('data').get('title')
                for word in word_list:
                    if re.search(
                            r'\b{}\b'.format(
                                word.lower()), title, re.IGNORECASE):
                        a_dict[word] += 1
            count_words(subreddit, word_list, next_after, a_dict)
        else:
            sorted_dict = sorted(
                a_dict.items(), key=lambda x: x[1], reverse=True)
            for item in sorted_dict:
                if item[1] != 0:
                    print('{}: {}'.format(item[0], item[1]))
