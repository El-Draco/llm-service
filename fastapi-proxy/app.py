import os
import secrets
from fastapi import FastAPI, Depends, HTTPException, status, Request, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from httpx import AsyncClient

app = FastAPI()
security = HTTPBasic()

# Get credentials from environment variables
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

async def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, USERNAME)
    correct_password = secrets.compare_digest(credentials.password, PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy(
    path: str,
    request: Request,
    credentials: HTTPBasicCredentials = Depends(get_current_user)
):
    url = f"http://ollama:11434/{path}"
    async with AsyncClient() as client:
        if request.method == "GET":
            response = await client.get(url, params=request.query_params)
        elif request.method == "POST":
            response = await client.post(url, data=await request.body())
        else:
            raise HTTPException(status_code=405, detail="Method Not Allowed")
    return Response(content=response.content, status_code=response.status_code)
