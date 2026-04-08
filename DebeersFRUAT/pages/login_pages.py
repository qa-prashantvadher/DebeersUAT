from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
from dotenv import load_dotenv
import os

load_dotenv(override=True)

class Login_Page(BasePage):

        user_name_text = os.getenv("USERNAME")
        password_text = os.getenv("PASSWORD")

        my_account_to_login_icon = "//*[@id='headerMyAccount']/button"
        my_account_view_icon = "//*[@id='headerMyAccount']/a"
        cart_icon = "//*[@id='headerShoppingBag']/div"
        wishlist_icon = "//*[@id='headerWishlist']/a"

        wishlist_create_account_button = ".wish-page__login-btn.btn.btn-primary.d-none.d-lg-inline-block"

        modal_user_name_input = "//*[@id='login-form-email-modal']"
        modal_password_input = "//*[@id='login-form-password-modal']"
        modal_login_button = "//*[@id='phantomRecaptchaLoginFormModal']"

        cart_username_input = "//*[@id='login-form-email']"
        cart_password_input = "//*[@id='login-form-password']"
        cart_login_button = "//*[@id='phantomSubmitLoginForm']"

        register_username_input = "//*[@id='login-form-email']"
        register_password_input = "//*[@id='login-form-password']"
        register_login_button = "//*[@id='phantomRecaptchaLoginForm']"
        register_create_account_button = "//*[@id='containerLogin']/p/a"

        my_account_landing_not_you = "a.account-header-link.btn.btn-link"
        my_account_landing_logout = "//a[@class='logout-link account-navigation-link']"


        def __init__(self, page):
            super().__init__(page)
            self.screenshot = PageScreenshot(page)

        def test_login_from_header(self):
            try:
                self.click(self.my_account_to_login_icon)
                self.timeout(2000)
                self.fill(self.modal_user_name_input,self.user_name_text)
                self.fill(self.modal_password_input,self.password_text)
                self.timeout(1000)
                #self.screenshot.take_Page_screenshot("HEADER_LOGIN")
                self.click(self.modal_login_button)
                self.timeout(5000)
                #self.screenshot.take_Page_screenshot("HEADER_LOGIN_MY_ACCOUNT")
                print("[HEADER LOGIN] USER IS SUCCESSFULLY LOGGED IN..")

            except:
                print("*****[HEADER LOGIN] USER IS NOT ABLE TO LOGGED IN..*****")

        def test_login_from_cart(self):
            try:
                self.click(self.cart_icon)
                self.timeout(2000)
                self.fill(self.cart_username_input,self.user_name_text)
                self.fill(self.cart_password_input,self.password_text)
                #self.screenshot.take_Page_screenshot("CART_LOGIN")
                self.timeout(1000)
                self.click(self.cart_login_button)
                self.timeout(5000)
                #self.screenshot.take_Page_screenshot("CART_LOGIN_CART")
                print("[CART LOGIN] USER IS SUCCESSFULLY LOGGED IN..")

            except:
                print("*****[CART LOGIN] USER IS NOT ABLE TO LOGGED IN..*****")


        def test_login_from_register(self):
            try:
                self.click(self.cart_icon)
                self.timeout(2000)
                self.click(self.register_create_account_button)
                self.timeout(5000)
                self.fill(self.register_username_input, self.user_name_text)
                self.fill(self.register_password_input,self.password_text)
                #self.screenshot.take_Page_screenshot("REGISTER_LOGIN")
                self.timeout(1000)
                self.click(self.register_login_button)
                self.timeout(5000)
                #self.screenshot.take_Page_screenshot("REGISTER_LOGIN_MY_ACCOUNT")
                print("[REGISTER LOGIN] USER IS SUCCESSFULLY LOGGED IN..")
            except:
                print("*****[REGISTER LOGIN] USER IS NOT ABLE TO LOGGED IN..*****")

        def test_login_from_wishlist(self):
            try:
                self.click(self.wishlist_icon)
                self.timeout(2000)
                self.click(self.wishlist_create_account_button)
                self.timeout(2000)
                self.fill(self.modal_user_name_input, self.user_name_text)
                self.fill(self.modal_password_input,self.password_text)
                #self.screenshot.take_Page_screenshot("WISHLIST_LOGIN")
                self.timeout(1000)
                self.click(self.modal_login_button)
                self.timeout(5000)
                #self.screenshot.take_Page_screenshot("WISHLIST_LOGIN_MY_ACCOUNT")
                print("[WISHLIST LOGIN] USER IS SUCCESSFULLY LOGGED IN..")
            except:
                print("*****[WISHLIST LOGIN] USER IS NOT ABLE TO LOGGED IN..*****")


        def test_logout_from_my_account_not_you(self):
            try:
                self.click(self.my_account_view_icon)
                self.timeout(5000)
                self.click(self.my_account_landing_not_you)
                self.timeout(5000)
                #self.screenshot.take_Page_screenshot("MY_ACCOUNT_NOT_YOU")
                print("[MY ACCOUNT-NOT YOU] USER IS SUCCESSFULLY LOGGED OUT..")

            except:
                print("*****[MY ACCOUNT-NOT YOU] USER IS NOT ABLE TO LOGGED OUT..*****")

        def test_logout_from_my_account_logout(self):
            try:
                self.click(self.my_account_view_icon)
                self.timeout(5000)
                self.screenshot.take_page_screenshot("MY_ACCOUNT_LANDING_PAGE")
                self.click(self.my_account_landing_logout)
                self.timeout(5000)
                #self.screenshot.take_Page_screenshot("MY_ACCOUNT_LOGOUT")
                print("[MY ACCOUNT-LOGOUT] USER IS SUCCESSFULLY LOGGED OUT..")
            except:
                print("*****[MY ACCOUNT-LOGOUT] USER IS NOT ABLE TO LOGGED OUT..*****")


        def test_logout_from_order_confirmation_page(self):
            try:
                self.timeout(2000)
                self.click(self.my_account_landing_logout)
                self.timeout(4000)
                #self.screenshot.take_Page_screenshot("MY_ACCOUNT_NOT_YOU")
                print("[ORDER CONFIRMATION-LOGOUT] USER IS SUCCESSFULLY LOGGED OUT..")

            except:
                print("*****[ORDER CONFIRMATION-LOGOUT] USER IS NOT ABLE TO LOGGED OUT..*****")