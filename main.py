import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Initialize FastAPI instance
app = FastAPI()

# 1. Setup paths correctly for Windows
BASE_DIR = Path(__file__).resolve().parent
static_dir = BASE_DIR / "static"

# DEBUG: Verification
print(f"DEBUG: Looking for static files in: {static_dir}")
print(f"DEBUG: Does folder exist? {static_dir.exists()}")

# 2. The standard way to mount static files (which we verified works in isolation)
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# 3. Setup templates engine
templates = Jinja2Templates(directory="templates")

# 4. Define your routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/blog", response_class=HTMLResponse)
async def blog(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request})
