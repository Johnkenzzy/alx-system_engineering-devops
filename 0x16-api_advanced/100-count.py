#!/usr/bin/python3
"""Defines count_words function"""
import collections
import json
import re
import requests


def count_words(subreddit, word_list=[], word_counts=None, after=None):
    """Given word(s) counts in hot article titles of a given subreddit"""
    if word_counts is None:
        word_counts = collections.defaultdict(int)

    normal_words = {word.lower(): 0 for word in word_list}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?'
    if after:
        url += f'after={after}'

    headers = {"User-Agent": "ALX"}

    try:
        resp = requests.get(url, headers=headers, allow_redirects=False)
        if resp.status_code == 200:
            data = resp.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title'].lower()
                words = re.findall(r'\b\w+\b', title)

                for word in words:
                    if word in normal_words:
                        word_counts[word] += 1

            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, word_counts, after)

            sorted_counts = sorted(
                    word_counts.items(), key=lambda x: (-x[1], x[0]))

            for word, count in sorted_counts:
                if count > 0:
                    print(f'{word}: {count}')
        else:
            return None
    except Exception as e:
        return None
