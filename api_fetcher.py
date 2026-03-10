import requests

def fetch_github_user(username):

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch data")
        return
    
    data = response.json()

    print(f"Github user: {data['login']}")
    print(f"Public Repos: {data['public_repos']}")


fetch_github_user("gerardinhoo")
fetch_github_user("octocat")

