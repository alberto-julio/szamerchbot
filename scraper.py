from bs4 import BeautifulSoup
import requests
import json
import re

sza_url = "https://txdxe.com/collections/sza"
not_url = "https://www.notbeauty.com/"
grand_tour_url = "https://shop.grandnationaltour.com/"

class Scraper:
    def __init__(self, site, selectors, stock_indicators, scraper_settings):
        self.site = site
        self.selectors = selectors
        self.stock_indicators = stock_indicators
        self.scraper_settings = scraper_settings