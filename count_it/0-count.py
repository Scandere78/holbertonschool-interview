#!/usr/bin/python3
"""Recursive function that queries the Reddit API and counts words in titles"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        # dictionnaire avec tous les mots en lowercase
        counts = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "holberton_count_script"}
    params = {"limit": 100, "after": after}

    try:
        res = requests.get(url, headers=headers,
                           params=params, allow_redirects=False)
        if res.status_code != 200:
            return
        data = res.json().get("data")
        if not data:
            return

        # Parcourir les titres
        for child in data.get("children", []):
            title = child.get("data", {}).get("title", "").lower().split()
            for word in counts:
                counts[word] += title.count(word)

        # Récursivité si after n’est pas None
        next_after = data.get("after")
        if next_after:
            return count_words(subreddit, word_list, next_after, counts)

        # Fin : affichage trié
        sorted_counts = sorted(
            [(word, cnt) for word, cnt in counts.items() if cnt > 0],
            key=lambda x: (-x[1], x[0])
        )
        for word, cnt in sorted_counts:
            print(f"{word}: {cnt}")

    except Exception:
        return
