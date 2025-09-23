from bs4 import BeautifulSoup
import requests
import json
import re
import time
import logging

sza_url = "https://txdxe.com/collections/sza"
not_url = "https://www.notbeauty.com/"

#TAKE A GRAND TOUR GRAND TOUR DRAGON BALL GT!!!!!!!!
grand_tour_url = "https://shop.grandnationaltour.com/"


def load_config(products: str = "") -> dict:
    with open(products, 'r') as file:
        data = json.load(file)
    return data

config = load_config()

def fetch_page(url: str) -> str:
    headers = {}
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    raw_html = response.text
    return raw_html

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

def check_stock(product: dict, stock_indicator: dict) -> str:

    stock_text = product.get("stock", "").lower()

    for phrase in stock_indicator.get("in_stock", []):
        if phrase.lower() in stock_text:
            return "in_stock"

    for phrase in stock_indicator.get("sold_out", []):
        if phrase.lower() in stock_text:
            return "sold_out"
    return "unknown"


def run_scraper(config: dict) -> None:

    for sites in config['sites']:
        selectors = sites['selectors']
        stock = sites['stock_indicators']
        delay = sites["scraper_settings"]['delay_seconds']

        for page in sites['pages']:
            html = fetch_page(page)
            products = parse_products(html, selectors)

            for product in products:
                if check_stock(product, stock):
                    x = 0
            
            time.sleep(delay)



