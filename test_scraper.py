import unittest
import scraper
from unittest.mock import patch, MagicMock

class Testing(unittest.TestCase):
    @patch("scraper.requests.get")
    def test_fetch_page(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><body><h1>Fake Page</h1></body></html>"
        mock_get.return_value = mock_response

        html = scraper.fetch_page("http://fakeurl.com")
        self.assertIn("<h1>Fake Page</h1>", html)
        mock_get.assert_called_once_with("http://fakeurl.com", timeout=10)

    def test_parse_products(self):
        html = """
        <div id="product-grid">
            <div class="grid__item">
                <a class="full-unstyled-link" href="/p1">Test Product</a>
                <span class="price-item">$19.99</span>
                <span class="badge">In Stock</span>
            </div>
        </div>
        """
        selectors = {
            "item": "#product-grid .grid__item",
            "title": ".full-unstyled-link",
            "price": ".price-item",
            "stock": ".badge",
            "link": ".full-unstyled-link"
        }

        products = scraper.parse_products(html, selectors)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0]["title"], "Test Product")
        self.assertEqual(products[0]["price"], "$19.99")
        self.assertEqual(products[0]["stock"], "In Stock")
        self.assertEqual(products[0]["link"], "/p1")

    def test_check_stock(self):
        indicators = {
            "in_stock": ["In Stock", "Available"],
            "sold_out": ["Sold Out"]
        }

        product_in = {"stock": "In Stock"}
        product_out = {"stock": "Sold Out"}
        product_unknown = {"stock": "Coming Soon"}

        self.assertEqual(scraper.check_stock(product_in, indicators), "in_stock")
        self.assertEqual(scraper.check_stock(product_out, indicators), "sold_out")
        self.assertEqual(scraper.check_stock(product_unknown, indicators), "unknown")


    @patch("scraper.fetch_page")
    def test_run_scraper(self, mock_fetch):
        html = """
        <div id="product-grid">
            <div class="grid__item">
                <a class="full-unstyled-link" href="/p1">Demo Product</a>
                <span class="price-item">$49.99</span>
                <span class="badge">Add to Cart</span>
            </div>
        </div>
        """
        mock_fetch.return_value = html

        fake_config = {
            "sites": [
                {
                    "name": "DemoSite",
                    "base_url": "https://demosite.com",
                    "pages": ["https://demosite.com/products"],
                    "selectors": {
                        "item": "#product-grid .grid__item",
                        "title": ".full-unstyled-link",
                        "price": ".price-item",
                        "stock": ".badge",
                        "link": ".full-unstyled-link"
                    },
                    "stock_indicators": {
                        "in_stock": ["Add to Cart"],
                        "sold_out": ["Sold Out"]
                    },
                    "scraper_settings": {"delay_seconds": 3, "max_retries": 1}
                }
            ]
        }

        results = scraper.run_scraper(fake_config)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["status"], "in_stock")
        self.assertEqual(results[0]["site"], "DemoSite")
        self.assertIn("https://demosite.com/p1", results[0]["link"])

    @patch("scraper.requests.get")
    def test_parse_product_mock(self, mock_get):
        """Unit test with mocked HTML response"""
        # Fake HTML snippet that matches your selectors
        fake_html = """
        <html>
            <body>
                <div class="product">
                    <h2 class="title">Test Item</h2>
                    <span class="price">$19.99</span>
                    <span class="status">In Stock</span>
                    <a href="https://example.com/item">Link</a>
                </div>
            </body>
        </html>
        """
        mock_response = MagicMock()
        mock_response.text = fake_html
        mock_get.return_value = mock_response

        config = {
            "sites": [
                {
                    "name": "TestShop",
                    "base_url": "https://example.com",
                    "pages": ["https://example.com/test"],
                    "selectors": {
                        "item": ".product",
                        "title": ".title",
                        "price": ".price",
                        "status": ".status",
                        "link": "a"
                    }
                }
            ]
        }

        results = scraper.run_scraper(config)
        self.assertEqual(len(results), 1)
        product = results[0]
        self.assertEqual(product["title"], "Test Item")
        self.assertEqual(product["price"], "$19.99")
        self.assertEqual(product["status"], "In Stock")
        self.assertTrue(product["link"].startswith("https://"))

if __name__ == '__main__':
    unittest.main()