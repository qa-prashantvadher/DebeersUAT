from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
from dotenv import load_dotenv
import os
import logging

load_dotenv(override=True)
logger = logging.getLogger(__name__)

class Login_Page(BasePage):

        username_text = os.getenv("USERNAME")
        password_text = os.getenv("PASSWORD")

        my_account_to_login_icon = "//*[@id='headerMyAccount']/button"
        my_account_view_icon = "//*[@id='headerMyAccount']/a"
        cart_icon = "//*[@id='headerShoppingBag']/div"
        wishlist_icon = "//*[@id='headerWishlist']/a"

        wishlist_create_account_button = "//button[contains(@class,'wish-page__login-btn')]"

        book_appointment_signin = "button.accordion-button.yourDetails__login"
        book_appointment_username_input = "#bookingLoginEmail"
        book_appointment_password_input = "#bookingLoginPassword"
        book_appointment_login_button = "#signIn"

        modal_username_input = "//*[@id='login-form-email-modal']"
        modal_password_input = "//*[@id='login-form-password-modal']"
        modal_login_button = "//*[@id='phantomRecaptchaLoginFormModal']"

        cart_username_input = "//*[@id='login-form-email']"
        cart_password_input = "//*[@id='login-form-password']"
        cart_login_button = "//*[@id='phantomSubmitLoginForm']"

        register_username_input = "//*[@id='login-form-email']"
        register_password_input = "//*[@id='login-form-password']"
        register_login_button = "//*[@id='phantomRecaptchaLoginForm']"
        register_create_account_button = "//*[@id='containerLogin']/p/a"

        my_account_landing_not_you = "//a[contains(@class,'account-header-link')]"
        my_account_landing_logout = "//a[@class='logout-link account-navigation-link']"


        def __init__(self, page):
            super().__init__(page)
            self.screenshot = PageScreenshot(page)

        def test_login_from_header(self):
            try:
                self.click(self.my_account_to_login_icon)
                self.timeout(8000)
                if self.is_visible(self.modal_username_input):
                    self.fill(self.modal_username_input,self.username_text)
                    self.fill(self.modal_password_input,self.password_text)
                    self.timeout(1000)
                    #self.screenshot.take_Page_screenshot("HEADER_LOGIN")
                    self.click(self.modal_login_button)
                    # Wait for my account element
                    self.wait_for_visible(self.my_account_landing_not_you, timeout=30000)
                    self.timeout(15000)
                    #self.screenshot.take_Page_screenshot("HEADER_LOGIN_MY_ACCOUNT")
                    logger.info("[HEADER-LOGIN] USER IS SUCCESSFULLY LOGGED IN..")
                else:
                    pass
                    logger.warning("[HEADER-LOGIN] USER IS ALREADY LOGGED IN..")

            except:
                logger.error("*****[HEADER-LOGIN] USER IS NOT ABLE TO LOGGED IN..*****")

        def test_login_from_cart(self):
            try:
                self.click(self.cart_icon)
                self.timeout(2000)
                self.fill(self.cart_username_input,self.username_text)
                self.fill(self.cart_password_input,self.password_text)
                #self.screenshot.take_Page_screenshot("CART_LOGIN")
                self.timeout(1000)
                self.click(self.cart_login_button)
                self.timeout(10000)
                #self.screenshot.take_Page_screenshot("CART_LOGIN_CART")
                logger.info("[CART-LOGIN] USER IS SUCCESSFULLY LOGGED IN..")
            except:
                logger.error("*****[CART-LOGIN] USER IS NOT ABLE TO LOGGED IN..*****")


        def test_login_from_register(self):
            try:
                self.click(self.cart_icon)
                self.timeout(2000)
                self.click(self.register_create_account_button)
                self.timeout(5000)
                self.fill(self.register_username_input, self.username_text)
                self.fill(self.register_password_input,self.password_text)
                #self.screenshot.take_Page_screenshot("REGISTER_LOGIN")
                self.timeout(1000)
                self.click(self.register_login_button)
                self.timeout(10000)
                #self.screenshot.take_Page_screenshot("REGISTER_LOGIN_MY_ACCOUNT")
                logger.info("[REGISTER-LOGIN] USER IS SUCCESSFULLY LOGGED IN..")
            except:
                logger.error("*****[REGISTER-LOGIN] USER IS NOT ABLE TO LOGGED IN..*****")

        def test_login_from_wishlist(self):
            try:
                self.click(self.wishlist_icon)
                self.timeout(2000)
                self.click(self.wishlist_create_account_button)
                self.timeout(2000)
                self.fill(self.modal_username_input, self.username_text)
                self.fill(self.modal_password_input,self.password_text)
                #self.screenshot.take_Page_screenshot("WISHLIST_LOGIN")
                self.timeout(1000)
                self.click(self.modal_login_button)
                self.timeout(10000)
                #self.screenshot.take_Page_screenshot("WISHLIST_LOGIN_MY_ACCOUNT")
                logger.info("[WISHLIST-LOGIN] USER IS SUCCESSFULLY LOGGED IN..")
            except:
                logger.error("*****[WISHLIST-LOGIN] USER IS NOT ABLE TO LOGGED IN..*****")

        def test_login_from_book_appointment(self):
            try:
                self.click(self.book_appointment_signin)
                self.timeout(3000)
                if self.is_not_visible(self.book_appointment_username_input):
                    self.click(self.book_appointment_signin)
                self.fill(self.book_appointment_username_input, self.username_text)
                self.fill(self.book_appointment_password_input, self.password_text)
                # self.screenshot.take_Page_screenshot("WISHLIST_LOGIN")
                self.timeout(1000)
                self.click(self.book_appointment_login_button)
                self.timeout(10000)
                # self.screenshot.take_Page_screenshot("WISHLIST_LOGIN_MY_ACCOUNT")
                logger.info("[BOOK APPOINTMENT-LOGIN] USER IS SUCCESSFULLY LOGGED IN..")
            except:
                logger.error("*****[BOOK APPOINTMENT-LOGIN] USER IS NOT ABLE TO LOGGED IN..*****")

        def test_logout_from_my_account_not_you(self):
            try:
                self.click(self.my_account_view_icon)
                self.timeout(5000)
                self.click(self.my_account_landing_not_you)
                self.timeout(5000)
                #self.screenshot.take_Page_screenshot("MY_ACCOUNT_NOT_YOU")
                logger.info("[MY ACCOUNT-NOT YOU] USER IS SUCCESSFULLY LOGGED OUT..")
            except:
                logger.error("*****[MY ACCOUNT-NOT YOU] USER IS NOT ABLE TO LOGGED OUT..*****")

        def test_logout_from_my_account_logout(self):
            try:
                self.click(self.my_account_view_icon)
                self.timeout(5000)
                self.screenshot.take_page_screenshot("MY_ACCOUNT_LANDING_PAGE")
                self.click(self.my_account_landing_logout)
                self.timeout(5000)
                #self.screenshot.take_Page_screenshot("MY_ACCOUNT_LOGOUT")
                logger.info("[MY ACCOUNT-LOGOUT] USER IS SUCCESSFULLY LOGGED OUT..")
            except:
                logger.error("*****[MY ACCOUNT-LOGOUT] USER IS NOT ABLE TO LOGGED OUT..*****")


        def test_logout_from_order_confirmation_page(self):
            try:
                self.timeout(2000)
                self.click(self.my_account_landing_logout)
                self.timeout(4000)
                #self.screenshot.take_Page_screenshot("MY_ACCOUNT_NOT_YOU")
                logger.info("[ORDER CONFIRMATION-LOGOUT] USER IS SUCCESSFULLY LOGGED OUT..")
            except:
                logger.error("*****[ORDER CONFIRMATION-LOGOUT] USER IS NOT ABLE TO LOGGED OUT..*****")