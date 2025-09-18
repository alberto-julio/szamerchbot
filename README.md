# 🛒 Twitter Stock Alert Bot  

A Python-based Twitter bot that automatically checks online stores for stock availability, price changes, and new product listings, then posts updates on Twitter (X).  

Currently configured to monitor:  
- [Grand National Tour Shop](https://shop.grandnationaltour.com/)  
- [Not Beauty](http://notbeauty.com)  
- [TXDXE (SZA Collection)](https://txdxe.com/collections/sza)  

---

## 📌 Features
- Scrapes product pages at defined intervals.  
- Detects:  
  - **In Stock / Out of Stock** changes  
  - **Price updates**  
  - (Optional) **New products** in a collection/category  
- Posts automated updates to Twitter (X).  
- Tracks multiple products from multiple stores.  
- Simple configuration via JSON file.  

---

## 🛠️ Tech Stack
- **Python 3.10+**  
- **Libraries**:  
  - [`requests`](https://pypi.org/project/requests/) – fetch web pages  
  - [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) – HTML parsing  
  - [`tweepy`](https://pypi.org/project/tweepy/) – Twitter API client  
  - [`sqlite3`](https://docs.python.org/3/library/sqlite3.html) – local database for state tracking  
  - [`schedule`](https://pypi.org/project/schedule/) – job scheduling  

---

## ⚙️ Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/twitter-stock-bot.git
cd twitter-stock-bot
