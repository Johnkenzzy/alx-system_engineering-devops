#!/usr/bin/python3
"""Defines recurse function"""
import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list all hot article titles of a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after:
        url += f'?after={after}'

    headers = {"User-Agent": "ALX"}

    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            data = resp.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])

            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except Exception as e:
        return None
