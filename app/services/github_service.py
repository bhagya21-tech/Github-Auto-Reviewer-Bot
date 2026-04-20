from github import Github 
from app.core.config import settings 

g = Github(settings.GITHUB_TOKEN)

def get_repo(repo_name):
    return g.get_repo(repo_name)

def get_pr_files(repo_name, pr_number):
    repo = get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    return pr.get_files()

def post_comment(repo_name, pr_number, comment, filename, patch):
    repo = get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    
    pr.create_issue_comment(
        f"📌 **Auto Review for `{filename}`**\n\n{comment}"
    )