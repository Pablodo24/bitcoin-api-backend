from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/analysis")
async def analyze():
    url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    return {
        "current_price": data["lastPrice"],
        "price_change_percent": data["priceChangePercent"]
    }
