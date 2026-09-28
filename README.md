# XAUUSD live-price bot
Render Build: `pip install -r backend/requirements.txt`
Render Start: `uvicorn backend.app:app --host 0.0.0.0 --port $PORT`
Add Environment Variable `TWELVE_DATA_API_KEY` with your Twelve Data API key.
Do not put the key in GitHub.
This provides live XAU/USD data only; it does not place Headway orders.
