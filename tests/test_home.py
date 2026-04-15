'''from playwright.sync_api import sync_playwright

def test_homepage_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.matchmyflight.com/")

        assert "flight" in page.title().lower()

        browser.close()'''

from playwright.sync_api import sync_playwright

def test_homepage_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://www.matchmyflight.com/")

        # Check main UI elements exist
        assert page.locator("text=Flight").count() > 0

        browser.close()