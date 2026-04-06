from pages.base_page import BasePage
from dotenv import load_dotenv
import os

load_dotenv(override=True)

#If .env file name is environment.env then must use load_dotenv("environment.env")

class OpenHomePage(BasePage):
    URL = os.getenv('BASE_URL')
    env = os.getenv('ENVIRONMENT')

    approve_cookie_button = "//*[@id='onetrust-accept-btn-handler']"
    country_selector_continue_button = "//*[@id='js-custom-country-continue-btn']"
    email_subscription_popup_close_icon = "button[class='js-modal-close-btn btn close'] i[class='close-icon dbicon-close']"

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def test_navigate_to_url(self):
       try:
            self.navigate(self.URL)
            print(f"NAVIGATED TO: {self.URL.upper()}")
       except:
            print("PAGE IS NOT AVAILABLE. LAUNCH BROWSER FIRST..")

    def test_cookie_consent(self):
         # Accept Consent Cookies if the popup appears
         try:
            if self.env in ("PROD", "QA"):
                pass  # do nothing, continue with next lines
            else:
                self.timeout(8000)
                if self.is_visible(self.approve_cookie_button):
                      self.click(self.approve_cookie_button)
                      print("COOKIE CONSENT IS ACCEPTED..")
                else:
                      print("COOKIE CONSENT IS ALREADY ACCEPTED..")
         except:
            print("*****COOKIE CONSENT POPUP ERROR..*****")

    def test_country_selector(self):
        # Accept Country selector if the popup appears
        try:
            if self.env ==  "QA":
                pass  # do nothing, continue with next lines
            else:
                self.timeout(3000)
                if self.is_visible(self.country_selector_continue_button):
                      self.page.click(self.country_selector_continue_button)
                      print("CLICKED CONTINUE CTA ON THE COUNTRY SELECTOR POPUP..")
                else:
                      print("ALREADY CLICKED CONTINUE CTA ON THE COUNTRY SELECTOR POPUP..")
        except:
            print("*****COUNTRY SELECTOR POPUP ERROR..*****")

    def test_email_subscription_popup(self):
        # Close the Newsletter popup if it appears
        try:
            if self.env == "QA":
                pass  # do nothing, continue with next lines
            else:
                self.page.click(self.email_subscription_popup_close_icon)
                print("CLOSED NEWSLETTER POPUP..")
        except:
            print("*****NEWSLETTER POPUP ERROR..*****")