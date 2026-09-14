#!/usr/bin/python3
"""Module for printing the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    If the subreddit is invalid, print None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:top.ten:v1.0 (by /u/nelson)"}
    params = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        children = response.json()["data"]["children"]
    except (ValueError, KeyError):
        print(None)
        return

    if not children:
        print(None)
        return

    for post in children:
        print(post["data"]["title"])
