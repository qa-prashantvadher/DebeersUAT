from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger(__name__)

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
            self.timeout(3000)
            if self.is_visible(self.guest_email_address_input):
                # Customer Email
                guest_email_value = self.page.locator(self.guest_email_address_input).input_value()
                registered_email_value = self.page.locator(self.registered_email_address_input).input_value()
                logger.info("[CHECKOUT-LOGIN] CHECKOUT LOGIN PAGE APPEARS..")
                if guest_email_value.strip():
                    logger.info(f"[CHECKOUT-LOGIN] GUEST EMAIL [PRE-FILLED]: {guest_email_value}")
                if registered_email_value.strip():
                    logger.info(f"[CHECKOUT-LOGIN] REGISTERED EMAIL [PRE-FILLED]: {registered_email_value}")
                self.fill(self.guest_email_address_input,self.email_address_text)
                self.screenshot.take_order_page_screenshot("CHECKOUT_LOGIN_GUEST")
                self.click(self.checkout_as_guest_cta)
                self.timeout(5000)
                logger.info("[CHECKOUT-GUEST] USER IS REDIRECTED TO THE \"DELIVERY\" PAGE..")
            else:
                pass
        except:
            logger.error(f"*****[CHECKOUT-GUEST] USER IS NOT REDIRECTED TO THE \"DELIVERY\" PAGE..*****")

    def test_checkout_as_registered_user(self):
        try:
            self.timeout(3000)
            if self.is_visible(self.registered_email_address_input):
                # Customer Email
                guest_email_value = self.page.locator(self.guest_email_address_input).input_value()
                registered_email_value = self.page.locator(self.registered_email_address_input).input_value()
                logger.info("[CHECKOUT-LOGIN] CHECKOUT LOGIN PAGE APPEARS..")
                if guest_email_value.strip():
                    logger.info(f"[CHECKOUT-LOGIN] GUEST EMAIL [PRE-FILLED]: {guest_email_value}")
                if registered_email_value.strip():
                    logger.info(f"[CHECKOUT-LOGIN] REGISTERED EMAIL [PRE-FILLED]: {registered_email_value}")
                self.fill(self.registered_email_address_input, self.email_address_text)
                self.fill(self.registered_password_input, self.password_text)
                self.screenshot.take_page_screenshot("CHECKOUT_LOGIN_REGISTERED")
                self.click(self.checkout_as_register_cta)
                self.timeout(5000)
                logger.info("[CHECKOUT-REGISTERED] USER IS REDIRECTED TO THE \"DELIVERY\" PAGE..")
            else:
                pass
        except:
            logger.error(f"*****[CHECKOUT-REGISTERED] USER IS NOT REDIRECTED TO THE \"DELIVERY\" PAGE..*****")



