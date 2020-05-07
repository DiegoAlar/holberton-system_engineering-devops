#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests
import sys


def top_ten(subreddit):
    """
        function that queries the Reddit API and prints the titles of the first
        10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'user-agent': 'X-Modhash'}
    r = requests.get(url, headers=headers)
    if r.json() is not None:
        try:
            a_dict = r.json()
        except ValueError:
            print("Not a valid JSON")
    if r.history or r.status_code == 404:
        return 0
    else:
        dict_list = a_dict.get('data').get('children')
        for dict_post in dict_list:
            print(dict_post.get('data').get('title'))
