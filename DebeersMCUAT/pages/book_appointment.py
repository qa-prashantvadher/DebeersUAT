from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
from pages.store_locator import Search_Locator_Page



class Book_Appointment(BasePage):

    #Appointment Types
    in_store_appointment_type= "//label[@for='input-inStore']"
    virtual_appointment_type= "//label[@for='input-virtual']"

    #Services
    in_store_after_sales_and_care= "//label[@for='input-afterSaleAndCare']"
    virtual_home_of_diamonds = "label[for='input-virtualHomeOfDiamonds']"

    #Service Details:
    in_store_diamond_setting_care = "//label[@for='input-diamondCare']"
    virtual_jewellery = "label[for='input-jewellery_vhod']"

    #Stores
    book_appointment_first_store = "(//div[contains(@class,'closest-addresses')]//label)[1]"

    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)
        self.store_locator = Search_Locator_Page(page)


    def test_in_store_appointment_type(self):
        try:
            self.timeout(2000)
            self.scroll_down(self.in_store_appointment_type)
            self.click(self.in_store_appointment_type)
            self.timeout(2000)
            self.click(self.in_store_after_sales_and_care)
            self.timeout(2000)
            self.click(self.in_store_diamond_setting_care)
            self.timeout(2000)
            self.click(self.book_appointment_first_store)
            self.timeout(2000)
            self.scroll_down(self.store_locator.paris_flagship_store_map_marker)
            self.store_locator.test_click_close_paris_flagship_in_map()
            print("IN STORE APPOINTMENT: ALL OPTIONS ARE SELECTED..")
            #self.screenshot.take_Page_screenshot("APPOINTMENT_IN_STORE")
        except:
            print("*****IN STORE APPOINTMENT: ALL OPTIONS ARE NOT SELECTED..*****")

    def test_bb_in_store_appointment_type(self):
        try:
            self.timeout(2000)
            self.click(self.in_store_after_sales_and_care)
            self.timeout(2000)
            self.click(self.in_store_diamond_setting_care)
            self.timeout(2000)
            self.click(self.book_appointment_first_store)
            self.timeout(2000)
            self.scroll_down(self.store_locator.paris_flagship_store_map_marker)
            self.store_locator.test_click_close_paris_flagship_in_map()
            print("[BB] IN STORE APPOINTMENT: ALL OPTIONS ARE SELECTED..")
            self.screenshot.take_page_screenshot("APPOINTMENT_DEFAULT_IN_STORE")
        except:
            print("*****[BB] IN STORE APPOINTMENT: ALL OPTIONS ARE NOT SELECTED..*****")


    def test_virtual_appointment_type(self):
        try:
            self.timeout(2000)
            self.scroll_down(self.virtual_appointment_type)
            self.click(self.virtual_appointment_type)
            self.timeout(2000)
            self.click(self.virtual_home_of_diamonds)
            self.timeout(2000)
            self.click(self.virtual_jewellery)
            self.timeout(2000)
            self.click(self.book_appointment_first_store)
            self.timeout(2000)
            self.scroll_down(self.store_locator.paris_flagship_store_map_marker)
            self.store_locator.test_click_close_paris_flagship_in_map()
            print("VIRTUAL APPOINTMENT: ALL OPTIONS ARE SELECTED..")
            #self.screenshot.take_Page_screenshot("APPOINTMENT_VIRTUAL")
        except:
            print("*****VIRTUAL APPOINTMENT: ALL OPTIONS ARE NOT SELECTED..*****")

    def test_bb_virtual_appointment_type(self):
        try:
            self.timeout(2000)
            self.click(self.virtual_home_of_diamonds)
            self.timeout(2000)
            self.click(self.virtual_jewellery)
            self.timeout(2000)
            self.click(self.book_appointment_first_store)
            self.timeout(2000)
            self.scroll_down(self.store_locator.paris_flagship_store_map_marker)
            self.store_locator.test_click_close_paris_flagship_in_map()
            print("[BB] VIRTUAL APPOINTMENT: ALL OPTIONS ARE SELECTED..")
            self.screenshot.take_page_screenshot("APPOINTMENT_DEFAULT_VIRTUAL")
        except:
            print("*****[BB] VIRTUAL APPOINTMENT: ALL OPTIONS ARE NOT SELECTED..*****")
