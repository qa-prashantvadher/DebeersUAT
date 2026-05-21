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


# PERSISTENT CONTEXT FIXTURE
@pytest.fixture(scope="session")
def context(playwright_instance):

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
        base_path,
        env_map[ENV],
        COUNTRY,
        date_folder
    )

    os.makedirs(video_full_path, exist_ok=True)

    # LOCALE MAP
    locale_map = {
        "UK": "en-GB",
        "US": "en-US",
        "FR": "fr-FR",
        "HK": "zh-HK",
        "TW": "zh-TW",
        "MO": "zh-MO"
    }

    browser_locale = locale_map.get(COUNTRY, "en-US")

    # PERSISTENT PROFILE DIRECTORY
    user_data_dir = r"D:\PlaywrightProfile"

    context_args = {

        # PERSISTENT PROFILE
        "user_data_dir": user_data_dir,

        # EDGE
        "channel": "msedge",

        # VIDEO
        "record_video_dir": video_full_path,

        # BROWSER
        "headless": False,

        # GEOLOCATION
        "permissions": ["geolocation"],

        "geolocation": {
            "latitude": 51.508099,
            "longitude": -0.140295
        },

        # LOCALE
        "locale": browser_locale,

        # TIMEZONE
        "timezone_id": "Europe/London",

        # USER AGENT
        "user_agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/136.0.0.0 Safari/537.36"
        ),

        # COLOR SCHEME
        "color_scheme": "light",

        # HTTPS HEADERS
        "extra_http_headers": {
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        },

        # EDGE ARGS
        "args": [
            "--start-maximized",
            "--lang=en-US",
            "--disable-features=Translate"
        ]
    }

    # DEVICE LOGIC
    if DEVICE == "MOBILE":

        device = playwright_instance.devices["iPhone 15 Pro Max"]

        context_args.update({
            **device,
            "record_video_size": {
                "width": 430,
                "height": 932
            }
        })

        print("[DEVICE] RUNNING IN MOBILE MODE..")

    elif DEVICE == "TABLET":

        device = playwright_instance.devices["iPad Pro 11"]

        context_args.update({
            **device,
            "record_video_size": {
                "width": 1024,
                "height": 1366
            }
        })

        print("[DEVICE] RUNNING IN TABLET MODE..")

    elif DEVICE == "DESKTOP":

        context_args.update({
            "no_viewport": True,
            "record_video_size": {
                "width": 1920,
                "height": 1080
            }
        })

        print("[DEVICE] RUNNING IN DESKTOP MODE..")

    # BASIC AUTH
    if ENV in ["UAT", "STAGING"]:
        context_args["http_credentials"] = creds

    # LAUNCH PERSISTENT CONTEXT
    context = playwright_instance.chromium.launch_persistent_context(
        **context_args
    )

    # STEALTH SCRIPT
    context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
    """)

    yield context

    context.close()


# PAGE FIXTURE
@pytest.fixture(scope="session")
def page(context):

    pages = context.pages

    if len(pages) > 0:
        page = pages[0]
    else:
        page = context.new_page()
        # FAST DEFAULT TIMEOUTS
        page.set_default_timeout(30000)
        page.set_default_navigation_timeout(60000)

    yield page

    page.close()