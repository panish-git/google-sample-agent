from fastapi import FastAPI
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCRklqwcLUoEQ4CqAlz3mCK_j8SJ-oqVWo")

app = FastAPI()

for m in genai.list_models():
    print(m.name, m.supported_generation_methods)

model = genai.GenerativeModel("models/gemini-2.5-flash")

@app.post("/market-price")
async def get_market_price(data: dict):
    item = data.get("item")
    supplier = data.get("supplier")

    prompt = f"""
    Provide current estimated market price for:
    Item: {item}
    Supplier: {supplier}

    Respond only in JSON:
    {{
      "item": "...",
      "supplier": "...",
      "estimated_price": "...",
      "currency": "..."
    }}
    """

    response = model.generate_content(prompt)

    return response.text
