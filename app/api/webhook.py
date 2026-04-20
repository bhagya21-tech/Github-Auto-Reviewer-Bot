from fastapi import APIRouter, Request, Header
from app.workers.tasks import review_pr_task 

router = APIRouter()

@router.post("/webhook")
async def github_webhook(request: Request, x_github_event: str = Header(None)):
    payload = await request.json()
    
    if x_github_event == "pull_request":
        action = payload.get("action")
        
        if action in ["opened", "synchronaize"]:
            pr_number = payload["pull_request"]["number"] 
            repo_name = payload["repository"]["full_name"]
            
            # send to background worker
            review_pr_task(repo_name, pr_number)
            
    return {"status": "received"}
