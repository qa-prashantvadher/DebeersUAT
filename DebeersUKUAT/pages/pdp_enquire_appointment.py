from pages.base_page import BasePage
from pages.search_slp_pdp import SearchSKU
from pages.take_screenshot import PageScreenshot
from dotenv import load_dotenv
import os

load_dotenv(override=True)

class PDP_Enquire_Book_Appointment(BasePage):

    SKU1="E103401"
    enquire_old_master_level = "//div[contains(@class,'primary-btn-wrap')]//button[contains(@class,'btn-enquire-online') and not(contains(@class,'d-none'))]"
    contact_us_old = "//li[contains(@class,'product-info__footer-item')]//a[contains(@class,'btn-clientServices-secondary btn-clientServices') and not(contains(@class,'d-none'))]"

    SKU2="E103387"
    enquire_hj_master_level = "//div[contains(@class,'primary-btn-wrap')]//a[contains(@class,'btn-enquire-online') and not(contains(@class,'d-none'))]"
    book_appointment_hj_master_level = "//div[contains(@class,'secondary-btn-wrap')]//a[contains(@class,'btn-bookAppointment') and not(contains(@class,'d-none'))]"

    if os.getenv('ENVIRONMENT') == "PRDO":
        SKU3="E102112"
    else:
        SKU3="R102265"
    find_your_diamond_cta = "//div[@class='primary-btn-wrap']/button[1]"
    enquire_upp_multiple_variant = "(//li[contains(@class,'variation-tile')]//button[contains(@class,'btn-enquire-online')])[1]"

    bb_contact_us_section = "//*[@id='pdpAttrAccContactUs']/button"
    bb_email_us_button = "button:has-text('Email Us')"
    bb_book_in_store_appointment_button = "a[title='Book in store appointment']"
    bb_book_a_virtual_appointment_button = "a[title='Book a virtual appointment']"

    def __init__(self, page):
        super().__init__(page)
        self.search = SearchSKU(page)
        self.screenshot = PageScreenshot(page)


    def test_enquire_old_master_level(self):
        try:
            self.timeout(3000)
            self.search.test_search_with_sku(self.SKU1)
            self.timeout(3000)
            self.click(self.enquire_old_master_level)
            self.timeout(3000)
            print("EMAIL US POPUP IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("OLD_MASTER_ENQUIRE")

        except:
            print("*****NOT ABLE TO CLICK ENQUIRE ONLINE CTA AT MASTER LEVEL..*****")

    def test_contact_us_old_master_level(self):
        try:
            self.timeout(3000)
            self.search.test_search_with_sku(self.SKU1)
            self.timeout(3000)
            self.click(self.contact_us_old)
            self.timeout(3000)
            print("USER IS REDIRECTED TO THE CLIENT SERVICE PAGE..")
            #self.screenshot.take_Page_screenshot("OLD_MASTER_CONTACT_US")

        except:
            print("*****NOT ABLE TO CLICK CONTACT US CTA AT MASTER LEVEL..*****")


    def test_enquire_hj_master_level(self):
        try:
            self.timeout(3000)
            self.search.test_search_with_sku(self.SKU2)
            self.timeout(2000)
            self.click(self.enquire_hj_master_level)
            self.timeout(2000)
            print("USER IS REDIRECTED TO THE CLIENT SERVICE PAGE..")
            #self.screenshot.take_Page_screenshot("HJ_MASTER_ENQUIRE")

        except:
            print("*****NOT ABLE TO CLICK ENQUIRE CTA AT MASTER LEVEL..*****")

    def test_book_appointment_hj_master_level(self):
        try:
            self.timeout(3000)
            self.search.test_search_with_sku(self.SKU2)
            self.timeout(3000)
            self.is_visible(self.book_appointment_hj_master_level)
            self.click(self.book_appointment_hj_master_level)
            self.timeout(3000)
            print("USER IS REDIRECTED TO THE BOOK AN APPOINTMENT PAGE [BY DEFAULT APPOINTMENT TYPE IS NOT SELECTED]..")
            #self.screenshot.take_Page_screenshot("HJ_MASTER_BOOK_APPOINTMENT")

        except:
            print("*****NOT ABLE TO CLICK BOOK APPOINTMENT CTA AT MASTER LEVEL..*****")


    def test_enquire_online_bb_upp_variant_level(self):
        try:
            self.timeout(3000)
            self.search.test_search_with_sku(self.SKU3)
            self.timeout(3000)
            self.click(self.find_your_diamonds_cta)
            self.click(self.enquire_upp_multiple_variant)
            self.timeout(3000)
            print("EMAIL US POPUP IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("BB_UPP_VARIANT_ENQUIRE")
        except:
            print("*****NOT ABLE TO CLICK ENQUIRE ONLINE CTA AT VARIANT LEVEL..*****")

    def test_in_store_appointment_bb_contact_us(self):
        try:
            self.timeout(3000)
            self.search.test_search_with_sku(self.SKU3)
            self.timeout(3000)
            self.click(self.bb_contact_us_section)
            self.click(self.bb_book_in_store_appointment_button)
            self.timeout(2000)
            print("USER IS REDIRECTED TO THE BOOK AN APPOINTMENT PAGE (BY DEFAULT IN STORE APPOINTMENT TYPE SELECTED)..")
            #self.screenshot.take_Page_screenshot("BB_CONTACT_US_IN_STORE_APPOINTMENT")

        except:
            print("*****NOT ABLE TO CLICK BOOK IN STORE APPOINTMENT CTA FROM THE CONTACT US SECTION..*****")

    def test_virtual_appointment_bb_contact_us(self):
        try:
            self.timeout(3000)
            self.search.test_search_with_sku(self.SKU3)
            self.timeout(3000)
            self.click(self.bb_contact_us_section)
            self.click(self.bb_book_a_virtual_appointment_button)
            self.timeout(2000)
            print("USER IS REDIRECTED TO THE BOOK AN APPOINTMENT PAGE (BY DEFAULT VIRTUAL APPOINTMENT TYPE SELECTED)..")
            #self.screenshot.take_Page_screenshot("BB_CONTACT_US_VIRTUAL_APPOINTMENT")

        except:
            print("*****NOT ABLE TO CLICK BOOK A VIRTUAL APPOINTMENT CTA FROM THE CONTACT US SECTION..*****")

    def test_email_us_bb_contact_us(self):
        try:
            self.timeout(3000)
            self.search.test_search_with_sku(self.SKU3)
            self.timeout(3000)
            self.click(self.bb_contact_us_section)
            self.click(self.bb_email_us_button)
            print("EMAIL US POPUP IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("BB_CONTACT_US_EMAIL_US")
        except:
            print("*****NOT ABLE TO CLICK EMAIL US CTA FROM THE CONTACT US SECTION..*****")