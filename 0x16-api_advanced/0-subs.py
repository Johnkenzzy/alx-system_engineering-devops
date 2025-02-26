#!/usr/bin/python3
"""Defines number_of_subscribers function"""
import json
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers (not active and total subscribers)"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "ALX"}

    try:
        subreddit = requests.get(url, headers=headers)
        if subreddit.status_code == 200:
            subreddit = subreddit.json()
            return subreddit['data']['subscribers']
    except Exception as e:
        return 0
