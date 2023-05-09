#!/usr/bin/python3

"""Queries the reddit API to print titles of the 1st 10 hot posts"""
import requests


def top_ten(subreddit):

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": 'Loyd'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        results = response.json()

        for post in results['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
