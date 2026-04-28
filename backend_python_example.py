from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

class LeadProfile(BaseModel):
    name: str
    company: str
    notes: str

@app.post("/api/generate-followup")
async def generate_followup(lead: LeadProfile):
    prompt = f"""
    Generate a professional and concise follow-up email for a lead.
    Lead Name: {lead.name}
    Company: {lead.company}
    Interest/Notes: {lead.notes}
    
    The tone should be helpful, visionary, and forward-thinking.
    """
    
    try:
        response = model.generate_content(prompt)
        return {"draft": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/dashboard-stats")
async def get_stats():
    # Example stats that match your dashboard
    return {
        "mrr": "$24,200",
        "active_leads": 42,
        "compute_cost": "$840.12",
        "growth": "+14.2%"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
