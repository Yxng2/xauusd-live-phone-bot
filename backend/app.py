import os,httpx
from fastapi import FastAPI
from fastapi.responses import FileResponse
app=FastAPI()
KEY=os.getenv("TWELVE_DATA_API_KEY","")
@app.get("/")
def root(): return FileResponse("frontend/index.html")
@app.get("/health")
def health(): return {"ok":True,"mode":"LIVE-DATA/DEMO"}
@app.get("/price")
async def price():
    if not KEY: return {"error":"TWELVE_DATA_API_KEY is not configured on Render"}
    async with httpx.AsyncClient(timeout=10) as c:
        r=await c.get("https://api.twelvedata.com/price",params={"symbol":"XAU/USD","apikey":KEY})
        d=r.json()
    if "price" not in d: return {"error":d.get("message","Price unavailable")}
    return {"symbol":"XAU/USD","price":float(d["price"])}
