#!/usr/bin/python3
"""
Module to recursively count occurrences of keywords in hot post titles.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively parses titles of all hot articles and prints a sorted count
    of specified keywords.
    """
    if counts is None:
        counts = {}
        for word in word_list:
            w = word.lower()
            counts[w] = counts.get(w, 0)

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
            return

        data = response.json().get("data", {})
        children = data.get("children", [])

        for post in children:
            title = post.get("data", {}).get("title", "").lower()
            words = title.split()
            for word in words:
                clean_word = word.strip(".,!?_")
                if clean_word in counts:
                    counts[clean_word] += 1

        next_after = data.get("after")
        if next_after is not None:
            return count_words(subreddit, word_list, next_after, counts)

        # Print sorted results upon reaching the end of recursion
        filtered_counts = {k: v for k, v in counts.items() if v > 0}
        if not filtered_counts:
            return

        # Sort primarily by count (descending), secondarily by key (ascending)
        sorted_counts = sorted(
            filtered_counts.items(),
            key=lambda item: (-item[1], item[0])
        )

        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

    except Exception:
        return
