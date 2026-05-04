from pages.open_website import OpenHomePage
from dotenv import load_dotenv
import os

load_dotenv(override=True)
ENV = os.getenv("ENVIRONMENT").upper()
COUNTRY = os.getenv("LOCALE").upper()

def test_menu_and_header_option_pages(page):

    home_page = OpenHomePage(page)

    # OPEN DEBEERS WEBSITE
    home_page.test_navigate_to_url()
    if ENV != "QA":
        home_page.test_cookie_consent()
        home_page.test_country_selector()
        home_page.test_email_subscription_popup()

