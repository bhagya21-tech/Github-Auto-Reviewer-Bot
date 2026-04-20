from app.services.github_service import get_pr_files, post_comment 
from app.services.review_service import review_code 


def review_pr_task(repo_name, pr_number):
    files = get_pr_files(repo_name, pr_number)
    
    for file in files:
        filename = file.filename 
        patch = file.patch 
        
        if not patch:
            continue
        
        review = review_code(patch)
        
        if review:
            post_comment(
                repo_name,
                pr_number,
                review,
                filename,
                file.patch
            )