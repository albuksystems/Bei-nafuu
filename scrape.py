
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import re

# Configuration for hyper-local products in Mlolongo/Syokimau/Athi River
PRODUCTS = [
    {"name": "gas cooker", "keywords": ["2 burner gas cooker", "table top gas cooker", "gas stove"]},
    {"name": "water tank", "keywords": ["1000L water tank", "2000L water tank", "cylindrical water tank"]},
    {"name": "tv", "keywords": ["32 inch smart tv", "digital tv 32 inch", "android tv"]},
    {"name": "mattress", "keywords": ["5x6 mattress", "4x6 mattress", "moko mattress", "superfoam mattress"]},
    {"name": "solar", "keywords": ["solar lighting kit", "solar panel 100w", "solar home system"]},
    {"name": "sound system", "keywords": ["subwoofer system", "home theater system", "bluetooth speaker"]},
    {"name": "furniture", "keywords": ["sofa set", "wooden bed 5x6", "plastic chairs set"]},
]

# Major retailers for price reference
RETAILERS = {
    "Jumia": {"base_url": "https://www.jumia.co.ke/", "search_path": "catalog/?q="},
    "Naivas": {"base_url": "https://naivas.online/", "search_path": "search?q="},
    "Carrefour": {"base_url": "https://www.carrefour.ke/mafken/en/search?q="},
    "Hotpoint": {"base_url": "https://hotpoint.co.ke/search?q="},
}

def scrape_jumia(product_keyword):
    url = f"{RETAILERS['Jumia']['base_url']}{RETAILERS['Jumia']['search_path']}{product_keyword}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        products = []
        for item in soup.find_all("article", class_="prd _fb col c-prd"):
            name_tag = item.find("h3", class_="name")
            price_tag = item.find("div", class_="prc")
            link_tag = item.find("a", class_="core")
            if name_tag and price_tag and link_tag:
                name = name_tag.text.strip()
                price_str = price_tag.text.strip().replace("KSh", "").replace(",", "")
                try:
                    price = float(price_str)
                except ValueError:
                    price = None
                product_url = RETAILERS["Jumia"]["base_url"] + link_tag["href"].lstrip("/")
                products.append({"name": name, "price": price, "url": product_url})
        return products
    except Exception as e:
        print(f"Error Jumia {product_keyword}: {e}")
        return []

def scrape_naivas(product_keyword):
    url = f"{RETAILERS['Naivas']['base_url']}{RETAILERS['Naivas']['search_path']}{product_keyword}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        products = []
        # Basic parsing logic for Naivas
        for item in soup.find_all("div", class_="product-item"):
            name_tag = item.find("a", class_="product-item-link")
            price_tag = item.find("span", class_="price")
            if name_tag and price_tag:
                name = name_tag.text.strip()
                price_str = price_tag.text.strip().replace("KES", "").replace(",", "")
                try:
                    price = float(price_str)
                except ValueError:
                    price = None
                products.append({"name": name, "price": price, "url": name_tag["href"]})
        return products
    except Exception as e:
        print(f"Error Naivas {product_keyword}: {e}")
        return []

def main():
    all_prices = {"last_updated": datetime.now().isoformat(), "products": {}}
    for product_info in PRODUCTS:
        p_name = product_info["name"]
        all_prices["products"][p_name] = []
        for kw in product_info["keywords"]:
            # Jumia
            res = scrape_jumia(kw)
            for r in res:
                r["retailer"] = "Jumia"
                all_prices["products"][p_name].append(r)
            # Naivas
            res = scrape_naivas(kw)
            for r in res:
                r["retailer"] = "Naivas"
                all_prices["products"][p_name].append(r)
    
    # Sort and Deduplicate
    for p_type, items in all_prices["products"].items():
        unique = {}
        for it in items:
            k = (it["name"].lower(), it["retailer"])
            if k not in unique and it["price"]:
                unique[k] = it
        all_prices["products"][p_type] = sorted(unique.values(), key=lambda x: x["price"])[:10] # Top 10 for depth

    with open("/home/ubuntu/patahapa-prices/data/prices.json", "w") as f:
        json.dump(all_prices, f, indent=4)
    print("Scrape complete.")

if __name__ == "__main__":
    main()
