from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot


class Update_My_Account_Page(BasePage):

    edit_account_details_icon = "//button[contains(@class,'js-edit-details-btn')]"
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
            self.timeout(1000)
            self.screenshot.take_page_screenshot("MY_ACCOUNT_DETAILS_BEFORE_EDIT")
            print("[MY ACCOUNT] EDIT MY ACCOUNT PAGE IS NOW VISIBLE..")
        except:
            print("*****[MY ACCOUNT] NOT ABLE TO OPEN EDIT MY ACCOUNT PAGE..*****")

    def test_update_my_account_details(self):
        try:
            self.timeout(1000)
            self.select_option(self.my_account_title_dropdown, self.my_account_title_value)
            self.fill(self.my_account_first_name_input, self.my_account_first_name_text)
            self.fill(self.my_account_last_name_input, self.my_account_last_name_text)
            self.fill(self.my_account_phone_input, self.my_account_phone_text)
            self.timeout(1000)
            self.click(self.my_account_save_button)
            self.timeout(3000)
            self.screenshot.take_page_screenshot("MY_ACCOUNT_DETAILS_AFTER_EDIT")
            print("[MY ACCOUNT] MY ACCOUNT DETAILS ARE UPDATED SUCCESSFULLY..")
        except:
            print("*****[MY ACCOUNT] NOT ABLE TO UPDATE MY ACCOUNT DETAILS..*****")
