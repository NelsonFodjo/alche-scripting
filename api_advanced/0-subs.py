#!/usr/bin/python3
"""
Module to query total subscriber count for a subreddit from the Reddit API.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers for a given subreddit.
    Returns 0 if the subreddit is invalid or redirects.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        return 0
    except Exception:
        return 0
