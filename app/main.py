from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
SITES_FILE = os.path.join(DATA_DIR, "sites.json")

app = FastAPI(title="Lumen Station API")

# Serve static UI files
app.mount("/ui", StaticFiles(directory=os.path.join(BASE_DIR, "..", "ui")), name="ui")

def load_sites():
    with open(SITES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/search")
async def search(username: str = Query(..., description="Username to search for")):
    """
    Search for a username across configured sites.
    Returns a list of site entries with placeholder replaced.
    """
    sites = load_sites()
    results = []
    for site in sites:
        url = site["url"].replace("{}", username)
        results.append({"name": site["name"], "url": url})
    return {"username": username, "sites": results}

@app.get("/", response_class=HTMLResponse)
async def root():
    # Simple HTML page that redirects to UI
    return "<html><body><a href='/ui'>UI</a></body></html>"

