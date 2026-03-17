"""Fetch and display public GitHub user information."""

import requests


def fetch_github_user(username: str) -> None:
    """Fetch and display public info for a GitHub user."""
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data for '{username}'")
        return

    data = response.json()
    print(f"GitHub user: {data['login']}")
    print(f"Public Repos: {data['public_repos']}")


if __name__ == "__main__":
    fetch_github_user("gerardinhoo")
    fetch_github_user("octocat")
