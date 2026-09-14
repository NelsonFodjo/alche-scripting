#!/usr/bin/python3
"""
Module to print the top 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    Prints None if the subreddit is invalid or redirects.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:v1.0.0 (by /u/NelsonFodjo)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code == 200:
            posts = response.json().get("data", {}).get("children", [])
            if not posts:
                print("None")
                return

            for post in posts[:10]:
                print(post.get("data", {}).get("title"))
        else:
            print("None")
    except Exception:
        print("None")
