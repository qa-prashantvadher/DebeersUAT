from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
import logging

logger = logging.getLogger(__name__)

class Update_My_Account_Page(BasePage):

    my_account_address_book_menu_option = "//li[contains(@class,'account-navigation-item')]//a[@title='Address Book']"

    remove_address_book_buttons = "//button[contains(@class,'js-remove-address-button')]"

    edit_account_details_icon = "//i[contains(@class,'dbicon-edit')]"
    my_account_title_dropdown = "//*[@id='customerTitle']"
    my_account_first_name_input = "//input[@id='firstName']"
    my_account_last_name_input = "//input[@id='lastName']"
    my_account_phone_input = "//input[@id='phone']"
    my_account_save_button = "//*[@class='btn btn-primary save-account-btn']"

    my_account_title_value = "mr."
    my_account_first_name_text = "Prashant"
    my_account_last_name_text = "Vadher"
    my_account_phone_text = "9558112787"

    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)

    def test_open_edit_my_account_page(self):
        try:
            self.timeout(3000)
            self.click(self.edit_account_details_icon)
            self.timeout(2000)
            self.screenshot.take_page_screenshot("MY_ACCOUNT_DETAILS_BEFORE_EDIT")
            logger.info("[MY ACCOUNT] EDIT MY ACCOUNT PAGE IS NOW VISIBLE..")
        except:
            logger.error("[MY ACCOUNT] NOT ABLE TO OPEN EDIT MY ACCOUNT PAGE..")

    def test_update_my_account_details(self):
        try:
            self.timeout(3000)
            self.select_option(self.my_account_title_dropdown, self.my_account_title_value)
            self.fill(self.my_account_first_name_input, self.my_account_first_name_text)
            self.fill(self.my_account_last_name_input, self.my_account_last_name_text)
            self.fill(self.my_account_phone_input, self.my_account_phone_text)
            self.timeout(2000)
            self.click(self.my_account_save_button)
            self.timeout(3000)
            self.screenshot.take_page_screenshot("MY_ACCOUNT_DETAILS_AFTER_EDIT")
            logger.info("[MY ACCOUNT] MY ACCOUNT DETAILS ARE UPDATED SUCCESSFULLY..")
        except:
            logger.error("*****[MY ACCOUNT] NOT ABLE TO UPDATE MY ACCOUNT DETAILS..*****")

    def test_open_address_book(self):
        try:
            self.timeout(3000)
            self.click(self.my_account_address_book_menu_option)
            self.timeout(7000)
            logger.info("[MY ACCOUNT-ADDRESS BOOK] USER IS REDIRECTED TO THE \"ADDRESS BOOK\" PAGE..")
        except:
            logger.error("*****[MY ACCOUNT-ADDRESS BOOK] NOT ABLE TO OPEN \"ADDRESS BOOK\" PAGE..*****")

    def test_remove_all_saved_addresses(self):
        try:
            # Check if address exists
            if self.count(self.remove_address_book_buttons) == 0:
                logger.info("[MY ACCOUNT-ADDRESS BOOK] NO ADDRESS RECORD FOUND..")
            else:
                total_addresses = self.count(self.remove_address_book_buttons)
                logger.info(f"[MY ACCOUNT-ADDRESS BOOK] TOTAL AVAILABLE ADDRESSES: {total_addresses}")
                while self.count(self.remove_address_book_buttons) > 0:
                    # Always click first available remove button
                    first_remove_button = self.first(self.remove_address_book_buttons)
                    first_remove_button.scroll_into_view_if_needed()
                    first_remove_button.click()
                    logger.info("[MY ACCOUNT-ADDRESS BOOK] CLICKED \"REMOVE ADDRESS\" BUTTON..")

                    # Wait for address record to be removed
                    self.timeout(5000)
                    total_addresses = self.count(self.remove_address_book_buttons)
                    if total_addresses == 0:
                        logger.info("[MY ACCOUNT-ADDRESS BOOK] ALL ADDRESS RECORDS ARE REMOVED SUCCESSFULLY..")
                    else:
                        logger.info(f"[MY ACCOUNT-ADDRESS BOOK] NOW REMAINING ADDRESSES: {total_addresses}")
        except:
            logger.error("*****[MY ACCOUNT-ADDRESS BOOK] NOT ABLE TO REMOVE ADDRESS BOOK RECORDS..*****")
