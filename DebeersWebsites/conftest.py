import pytest
from playwright.sync_api import sync_playwright

from dotenv import load_dotenv
import os

load_dotenv(override=True)


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
        channel="msedge", #To execute script in the MS Edge Browser
        headless=False,
        args=["--start-maximized"]

    )
    yield browser
    browser.close()
    playwright.stop()


# Create ONE context for all tests
@pytest.fixture(scope="session")
def context(browser):
    ENV = os.getenv("ENVIRONMENT")

    context_args = {
        "no_viewport": True,
        "permissions": ["geolocation"],
        "geolocation": {
            "latitude": 51.508099,
            "longitude": -0.140295
        }
    }

    # Apply condition based on environment
    if ENV == "UAT":
        context_args["http_credentials"] = creds

    context = browser.new_context(**context_args)

    yield context
    context.close()


# Reuse SAME page across all tests
@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page

