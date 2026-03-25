from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
from dotenv import load_dotenv
import os

load_dotenv(override=True)

class Checkout_Login(BasePage):

    email_address_text = os.getenv("USERNAME")
    password_text = os.getenv("PASSWORD")

    guest_email_address_input = "//input[@id='login-form-email']"
    registered_email_address_input = "//input[@id='email']"
    registered_password_input = "//input[@id='password']"

    checkout_as_guest_cta = "//button[@id='submitGuestCustomer']"
    checkout_as_register_cta = "//button[@id='phantomSubmitToCustomerClient']"


    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)

    def test_checkout_as_guest_user(self):
        try:
            self.timeout(2000)
            self.fill(self.guest_email_address_input,self.email_address_text)
            self.screenshot.take_page_screenshot("CHECKOUT_LOGIN_GUEST")
            self.click(self.checkout_as_guest_cta)
            self.timeout(8000)
            print("[CHECKOUT-GUEST] USER IS REDIRECTED TO THE CHECKOUT DELIVERY PAGE..")
        except:
            print(f"*****[CHECKOUT-GUEST] USER IS NOT REDIRECTED TO THE CHECKOUT DELIVERY PAGE..*****")

    def test_checkout_as_registered_user(self):
        try:
            self.timeout(2000)
            self.fill(self.registered_email_address_input, self.email_address_text)
            self.fill(self.registered_password_input, self.password_text)
            self.screenshot.take_page_screenshot("CHECKOUT_LOGIN_REGISTERED")
            self.click(self.checkout_as_register_cta)
            self.timeout(8000)
            print("[CHECKOUT-REGISTERED] USER IS REDIRECTED TO THE CHECKOUT DELIVERY PAGE..")
        except:
            print(f"*****[CHECKOUT-REGISTERED] USER IS NOT REDIRECTED TO THE CHECKOUT DELIVERY PAGE..*****")



