#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    Returns 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom user agent'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            return data['data']['subscribers']
        except (KeyError, ValueError):
            # In case the JSON is not in the expected format or does not contain the subscribers count
            return 0
    else:
        # If the status code is not 200, the subreddit is probably invalid
        return 0

