from playwright.sync_api import sync_playwright
from pages.home_page import HomePage

def test_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        home = HomePage(page)
        home.open()

        assert "flight" in home.get_title().lower()

        browser.close()