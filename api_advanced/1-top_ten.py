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

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    params = {
        "limit": 10,
        "raw_json": 1
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code == 200:
            res_json = response.json()
            posts = res_json.get("data", {}).get("children", [])

            if not posts or not isinstance(posts, list):
                print("None")
                return

            for post in posts[:10]:
                print(post.get("data", {}).get("title"))
        else:
            print("None")
    except Exception:
        print("None")
