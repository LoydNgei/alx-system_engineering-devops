#!/usr/bin/python3

""" A script to get subscribers on a subreddit"""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": 'Loyd'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        the_subs = data.get("data").get("subscribers")
        return the_subs
    else:
        return 0
