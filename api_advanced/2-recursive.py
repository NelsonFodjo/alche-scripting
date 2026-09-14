#!/usr/bin/python3
"""
Module to recursively fetch all hot post titles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing titles
    of all hot articles for a given subreddit. Returns None if invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyCustomUserAgent/1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])

        for post in children:
            hot_list.append(post.get("data", {}).get("title"))

        next_after = data.get("after")
        if next_after is not None:
            return recurse(subreddit, hot_list, after=next_after)

        return hot_list
    except Exception:
        return None
