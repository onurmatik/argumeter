from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
import json
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables (for OPENAI_API_KEY)
load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# FastAPI app
app = FastAPI()

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Pydantic  schema
class Argument(BaseModel):
    argument: str
    evaluation: str
    facts: List[str]
    fallacies: List[str]

class Users(BaseModel):
    user: str
    arguments: List[Argument]
    score: int

class Discussion(BaseModel):
    topic: str
    users: List[Users]

# FastAPI input model to accept the thread from the user
class ThreadInput(BaseModel):
    thread: str

@app.post("/evaluate_discussion/")
async def evaluate_discussion(request: Request, thread: str = Form(...)):
    try:
        # Call OpenAI with the thread data
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Analyze the users’ arguments in the provided discussion thread. "
                               "Identify and evaluate each individual argument by identifying supporting "
                               "facts and highlighting any logical fallacies present. "
                               "For each user, assign an overall score (1-10) based on the collective strength, "
                               "logical soundness, and factual accuracy of their arguments. "
                },
                {
                    "role": "user",
                    "content": thread,
                }
            ],
            response_format=Discussion,
        )

        # Parse the OpenAI completion response
        result = completion.choices[0].message.content

        # Return the evaluation results
        return templates.TemplateResponse("result.html", {
            "request": request,
            "result": json.loads(result)
        })

    except Exception as e:
        # Handle exceptions and return HTTP 500 error if anything goes wrong
        raise HTTPException(status_code=500, detail=str(e))

# Form endpoint to accept discussion thread via HTML
@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("form.html", {
        "request": request
    })
