import time
import pytest
import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

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
    COUNTRY = os.getenv("LOCALE")


    date_folder = time.strftime('%d%m%Y')
    base_path = r"D:\Debeers Videos and Screenshots\Videos"
    env_map = {
        "UAT": "DB-UAT",
        "PROD": "DB-PROD",
        "QA": "DB-QA"
    }

    if ENV not in env_map:
        raise ValueError(f"Invalid Environment: {ENV}")
    if COUNTRY not in ["UK", "US", "FR","HK"]:
        raise ValueError(f"Invalid Country: {COUNTRY}")

    video_path = os.path.join(base_path, env_map[ENV], COUNTRY)
    video_full_path = os.path.join(video_path, date_folder)
    os.makedirs(video_full_path, exist_ok=True)

    context_args = {
        "no_viewport": True,
        "record_video_dir": video_full_path,  # Folder where videos will be saved
        "record_video_size": {"width": 1920, "height": 1080},
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
    page.close()