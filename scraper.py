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


def fetch_page(url: str) -> str:

    headers = {}
    response = requests.get(url, headers=headers)
    raw_html = response.text
    return raw_html


class Scraper:
    def __init__(self, site, selectors, stock_indicators, scraper_settings):
        self.site = site
        self.selectors = selectors
        self.stock_indicators = stock_indicators
        self.scraper_settings = scraper_settings