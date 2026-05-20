import requests
import pandas as pd
from datetime import datetime

URL = "https://www.zeroharm.in/products.json"

def fetch_products():
    all_products = []
    page = 1
    
    while True:
        r = requests.get(f"{URL}?page={page}")
        data = r.json()
        
        if not data["products"]:
            break
        
        for product in data["products"]:
            for variant in product["variants"]:
                all_products.append({
                    "date": datetime.today().strftime("%Y-%m-%d"),
                    "product": product["title"],
                    "variant": variant["title"],
                    "price": variant["price"],
                    "mrp": variant["compare_at_price"],
                    "sku": variant["sku"]
                })
        
        page += 1
        
    return pd.DataFrame(all_products)

df = fetch_products()
df.to_csv("prices.csv", index=False)
