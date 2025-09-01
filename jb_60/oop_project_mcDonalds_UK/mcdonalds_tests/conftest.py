import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture

def setup_mcdonalds():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        page = browser.new_page()
        page.goto("https://www.mcdonalds.com/gb/en-gb.html")

        if (page.locator("[id='onetrust-accept-btn-handler']").is_visible()):
            cookies_button = page.locator("[id='onetrust-accept-btn-handler']")
            cookies_button.click()

        yield page
        page.close()
        browser.close()
        print("test end")

