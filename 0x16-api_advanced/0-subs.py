#!/usr/bin/python3
"""Defines number_of_subscribers function"""
import json
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "ALX"}

    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            subreddit = resp.json()
            return subreddit['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0
