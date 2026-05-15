from pages.base_page import BasePage
from dotenv import load_dotenv
import os
import logging

load_dotenv(override=True) #If .env file name is environment.env then must use load_dotenv("environment.env")
logger = logging.getLogger(__name__)


class OpenHomePage(BasePage):
    URL = os.getenv("BASE_URL")
    ENV = os.getenv("ENVIRONMENT")
    COUNTRY = os.getenv("LOCALE")

    approve_cookie_button = "//*[@id='onetrust-accept-btn-handler']"
    country_selector_continue_button = "//*[@id='js-custom-country-continue-btn']"
    email_subscription_popup_close_icon = "button[class='js-modal-close-btn btn close'] i[class='close-icon dbicon-close']"

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def test_navigate_to_url(self):
       try:
            self.navigate(self.URL)
            self.timeout(5000)
            logger.info(f"[{self.COUNTRY}-{self.ENV}] [HOME PAGE] NAVIGATED TO: {self.URL.upper()}")
       except:
            logger.error(f"*****[{self.COUNTRY}-{self.ENV}] [HOME PAGE] PAGE IS NOT AVAILABLE. LAUNCH BROWSER FIRST..*****")

    def test_cookie_consent(self):
         # Accept Consent Cookies if the popup appears
         try:
            self.timeout(5000)
            if self.is_visible(self.approve_cookie_button):
                  self.click(self.approve_cookie_button)
                  logger.info("[COOKIE] COOKIE CONSENT IS ACCEPTED..")
            else:
                  logger.warning("[COOKIE] COOKIE CONSENT IS ALREADY ACCEPTED..")
         except:
            logger.error("*****[COOKIE] COOKIE CONSENT POPUP ERROR..*****")

    def test_country_selector(self):
        # Accept Country selector if the popup appears
        try:
            self.timeout(3000)
            if self.is_visible(self.country_selector_continue_button):
                  self.page.click(self.country_selector_continue_button)
                  logger.info("[COUNTRY SELECTOR] CLICKED CONTINUE CTA ON THE COUNTRY SELECTOR POPUP..")
            else:
                  logger.warning("[COUNTRY SELECTOR] ALREADY CLICKED CONTINUE CTA ON THE COUNTRY SELECTOR POPUP..")
        except:
            logger.error("*****[COUNTRY SELECTOR] COUNTRY SELECTOR POPUP ERROR..*****")

    def test_email_subscription_popup(self):
        # Close the Newsletter popup if it appears
        try:
            self.page.click(self.email_subscription_popup_close_icon)
            logger.info("[EMAIL SUBSCRIPTION] CLOSED NEWSLETTER POPUP..")
        except:
            logger.error("*****[EMAIL SUBSCRIPTION] NEWSLETTER POPUP ERROR..*****")