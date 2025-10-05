import scraper
import json
import time
import os

def load_config(products: str) -> dict:
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, products)
    with open(path, 'r') as file:
        data = json.load(file)
    return data

def main():
    
    config = load_config('config/config.json')

    print("🚬 Running smoke test...")
    results = scraper.run_scraper(config)

    print(f"✅ Pulled {len(results)} products")
    for product in results[:5]:  # only show first 5
        print(json.dumps(product, indent=2))

if __name__ == "__main__":
    main()
