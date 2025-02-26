#!/usr/bin/python3
"""Defines top_ten function"""
import json
import requests


def top_ten(subreddit):
    """Return the top 10 titles of a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {"User-Agent": "ALX"}

    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            posts = resp.json()
            for post in posts['data']['children']:
                print(post['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(None)
