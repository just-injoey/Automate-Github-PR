import json
import requests

def create_pull_request(project_name, repo_name, title, description, head_branch, base_branch, git_token):
    """Creates the pull request for the head_branch against the base_branch"""
    git_pulls_api = "https://github.com/api/v3/repos/{0}/{1}/pulls".format(
        project_name,
        repo_name)
    headers = {
        "Authorization": "token {0}".format(git_token),
        "Content-Type": "application/json"}

    payload = {
        "title": title,
        "body": description,
        "head": head_branch,
        "base": base_branch,
    }

    r = requests.post(
        git_pulls_api,
        headers=headers,
        data=json.dumps(payload))

    if not r.ok:
        print("Request Failed: {0}".format(r.text))

create_pull_request(
    "Automate-Github-PR-Project", # project_name
    "Automate-Github-PR", # repo_name
    "Dekhte hai", # title
    "Mdescription kya likhna hai", # description
    "main", # head_branch
    "main", # base_branch
    "<github access token here>", # git_token
)