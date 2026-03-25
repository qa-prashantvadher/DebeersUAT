import pytest
from playwright.sync_api import sync_playwright

creds = {
    "username": "storefront",
    "password": "storefront"
}

# Start browser once per session
@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        #headless=True,
        headless=False,
        args=["--start-maximized"]

    )
    yield browser
    browser.close()
    playwright.stop()


# Create ONE context for all tests
@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context(
        no_viewport=True,
        #Disable following line in case of Production
        #http_credentials=creds,

        #Grant geolocation permission
        permissions = ["geolocation"],
        #Mock browser location (London example)
        geolocation = {
        "latitude": 51.508099,
        "longitude": -0.140295
        }
    )
    yield context
    context.close()


# Reuse SAME page across all tests
@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page

