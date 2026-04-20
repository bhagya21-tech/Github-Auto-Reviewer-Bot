from groq import Groq 
from app.core.config import settings 

client = Groq(api_key=settings.GROQ_API_KEY)

def review_code(code_diff):
    prompt = f""" 
You are a senior Python code reviewer. 
    
Review this code diff:
{code_diff} 

Give: 
- Bugs 
- Improvements
- Naming suggestions 
- Code quality issues 
""" 
    
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    
    return response.choices[0].message.content 
