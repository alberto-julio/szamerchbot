from bs4 import BeautifulSoup
import requests
import json
import time
import logging
import os

sza_url = "https://txdxe.com/collections/sza"
not_url = "https://www.notbeauty.com/"

#TAKE A GRAND TOUR GRAND TOUR DRAGON BALL GT!!!!!!!!
grand_tour_url = "https://shop.grandnationaltour.com/"


#loads up our config file that you wrote so that we can use all that data within python
#also lets the bot know what we are looking for
def load_config(products: str) -> dict:
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, products)
    with open(path, 'r') as file:
        data = json.load(file)
    return data

config = load_config('config/config.json')

#turns the webpages into raw html so that the bot can follow the structure and know where to look for the data
def fetch_page(url: str) -> str:
    headers = {}
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    raw_html = response.text
    return raw_html


#this is where the bot actually goes through the website and yanks everything out and returns the data we want
#but this only returns the products, used to help fill out our config
def parse_products(html: str, selectors: dict) -> list[dict[str, str]]:
    
    soup = BeautifulSoup(html, "html.parser")
    product_list = []
    items = soup.select(selectors['item'])

    for item in items:
        title_elem = item.select_one(selectors.get("title", ""))
        price_elem = item.select_one(selectors.get("price", ""))
        stock_elem = item.select_one(selectors.get("stock", ""))
        link_elem = item.select_one(selectors.get("link", ""))

        product = {
            "title": title_elem.get_text(strip=True) if title_elem else "",
            "price": price_elem.get_text(strip=True) if price_elem else "",
            "stock": stock_elem.get_text(strip=True) if stock_elem else "",
            "link": link_elem["href"] if link_elem and link_elem.has_attr("href") else "",
        }

        product_list.append(product)
    return product_list

#individual function used to check our stock, usually the last step
def check_stock(product: dict, stock_indicator: dict) -> str:

    stock_text = product.get("stock", "").lower()
    for phrase in stock_indicator.get("in_stock", []):
        if phrase.lower() in stock_text:
            return "in_stock"
    for phrase in stock_indicator.get("sold_out", []):
        if phrase.lower() in stock_text:
            return "sold_out"
    return "unknown"


#main bread and butter for our bot, where it goes into each individual sit, webpages and calls our other functions
def run_scraper(config: dict) -> list[dict[str, str]]:

    all_results = []

    for site in config["sites"]:
        selectors = site["selectors"]
        stock_indicators = site["stock_indicators"]
        delay = site["scraper_settings"]["delay_seconds"]
        base_url = site["base_url"]

        for page in site["pages"]:
            try:
                html = fetch_page(page)
                products = parse_products(html, selectors)

                for product in products:
                    status = check_stock(product, stock_indicators)
                    product["status"] = status

                    if product["link"].startswith("/"):
                        product["link"] = base_url.rstrip("/") + product["link"]

                    
                    product["site"] = site["name"]

                    all_results.append(product)

                time.sleep(delay)

            except Exception as e:
                logging.error(f"Error scraping {page}: {e}")

    return all_results


