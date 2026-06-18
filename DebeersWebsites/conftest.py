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

# START PLAYWRIGHT ONCE
@pytest.fixture(scope="session")
def playwright_instance():
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()


# BROWSER USES SAME PLAYWRIGHT INSTANCE
@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(
        channel="msedge",
        headless=False,
        args=[
            "--start-maximized",
            "--disable-features=Translate,msEdgeTranslate,EdgeTranslate,TranslateUI",
            "--disable-translate",
            "--lang=en-US"
        ]
    )
    yield browser
    browser.close()


# MOBILE OR DESKTOP SWITCH
@pytest.fixture(scope="session")
def context(browser, playwright_instance):
    ENV = os.getenv("ENVIRONMENT").upper()
    COUNTRY = os.getenv("LOCALE").upper()
    DEVICE = os.getenv("DEVICE").upper()

    date_folder = time.strftime('%d%m%Y')
    base_path = r"D:\Debeers Videos and Screenshots\Videos"

    env_map = {
        "UAT": "DB-UAT",
        "PROD": "DB-PROD",
        "QA": "DB-QA"
    }

    if ENV not in env_map:
        raise ValueError(f"Invalid Environment: {ENV}")
    if COUNTRY not in ["UK", "US", "FR", "HK", "TW", "MO", "CA"]:
        raise ValueError(f"Invalid Country: {COUNTRY}")

    video_full_path = os.path.join(
        base_path, env_map[ENV], COUNTRY, date_folder
    )
    os.makedirs(video_full_path, exist_ok=True)

    # CONTEXT LANGUAGE MAP
    locale_map = {
        "UK": "en-GB",
        "US": "en-US",
        "FR": "fr-FR",
        "HK": "zh-HK",
        "TW": "zh-TW",
        "MO": "zh-MO"
    }

    browser_locale = locale_map.get(COUNTRY, "en-US")

    geo_map = {
        "UK": {"latitude": 51.508099, "longitude": -0.140295},
        "US": {"latitude": 40.7128, "longitude": -74.0060},
        "FR": {"latitude": 48.8566, "longitude": 2.3522},
        "HK": {"latitude": 22.3193, "longitude": 114.1694},
        "TW": {"latitude": 25.0330, "longitude": 121.5654},
        "MO": {"latitude": 22.1987, "longitude": 113.5439}
    }

    context_args = {
        "record_video_dir": video_full_path,
        "permissions": ["geolocation"],
        "locale": browser_locale,
        "geolocation": geo_map[COUNTRY]
    }

    # DEVICE LOGIC (FIXED)
    if DEVICE == "MOBILE":
        device = playwright_instance.devices["iPhone 15 Pro Max"]

        context_args.update({
            **device,
            "record_video_size": {"width": 430, "height": 932}
        })
        print("[DEVICE] RUNNING IN MOBILE MODE..")

    elif DEVICE == "TABLET":
        device = playwright_instance.devices["iPad Pro 11"]

        context_args.update({
            **device,
            "record_video_size": {"width": 1024, "height": 1366}
        })
        print("[DEVICE] RUNNING IN TABLET MODE..")

    elif DEVICE == "DESKTOP":
        context_args.update({
            "no_viewport": True,
            "record_video_size": {"width": 1920, "height": 1080}
        })
        print("[DEVICE] RUNNING IN DESKTOP MODE..")

    # AUTH FOR UAT AND STAGING WEBSITE
    if ENV == "UAT" or ENV == "STAGING":
        context_args["http_credentials"] = creds

    context = browser.new_context(**context_args)

    yield context
    context.close()


# Page fixture
@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page
    page.close()