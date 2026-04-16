from pages.base_page import BasePage
from pages.search_slp_pdp import SearchSKU
from pages.add_engraving import AddEngraving
from pages.take_screenshot import PageScreenshot
import re
import random
from datetime import datetime, timedelta
import locale
from dotenv import load_dotenv
import os

load_dotenv(override=True)

class Checkout_PDP_SPP_No_Size(BasePage):

    COUNTRY = os.getenv("LOCALE")

    # SPP WITHOUT SIZE  - WITH ENGRAVING
    SKU1_LIST = ["E103376", "E103115","E103454", "E103116"]
    
    # SPP WITHOUT SIZE  - WITHOUT ENGRAVING
    SKU2_LIST = ["E102189", "E103475", "E102161", "E103450", "E102190", "E103380", "E103385", "E102158"]

    ADD_TO_BAG_CTA = "//div[@class='primary-btn-wrap']/button[1]"
    ADD_ENGRAVING_CTA = "//div[@class='secondary-btn-wrap']/button[1]"

    
    DELIVERY_DATE_WITHOUT_ENGRAVING = "(//*[@id='deliveryDate'])[1]"
    DELIVERY_DATE_WITH_ENGRAVING = "(//*[@id='deliveryDate'])[2]"


    minicart_close_icon = "//*[@id='minicart']/button"
    minicart_secure_checkout = "//div[@id='minicart']/section/div/a"


    def __init__(self, page):
        super().__init__(page)
        self.search = SearchSKU(page)
        self.engraving = AddEngraving(page)
        self.screenshot = PageScreenshot(page)

    def test_checkout_spp_no_size_with_engraving(self):
        SKU1 = random.choice(self.SKU1_LIST)
        print(f"[CHECKOUT] SKU1: {SKU1}")
        try:

            if self.COUNTRY == "FR":
                #locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")  # For Linux/Mac
                locale.setlocale(locale.LC_TIME, "French_France")  # For Windows, because of new_date = date_obj + timedelta(days=10) line
            elif self.COUNTRY == "HK":
                #locale.setlocale(locale.LC_TIME, "zh_HK.UTF-8")  # For Linux/Mac
                locale.setlocale(locale.LC_TIME, "Chinese_Hong Kong SAR")  # For Windows, because of new_date = date_obj + timedelta(days=10) line

            self.search.test_search_with_sku(SKU1)
            delivery_date = self.get_text(self.DELIVERY_DATE_WITHOUT_ENGRAVING).strip()
            clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', delivery_date).strip()
            date_obj = datetime.strptime(clean_date, "%A %d %B %Y")

            new_date = date_obj + timedelta(days=10)
            expected_date = new_date.strftime("%A %d %B %Y")
            self.click(self.ADD_ENGRAVING_CTA)
            self.engraving.test_add_engraving()
            print(f"[CHECKOUT] SKU: {SKU1} [ADDED WITH ENGRAVING], DELIVERY DATE: {expected_date.upper()}..")
            #self.screenshot.take_Page_screenshot("CHECKOUT_SPP_NO_SIZE_ADD_WITH_ENGRAVING")
        except:
            print(f"*****[CHECKOUT] SKU: {SKU1} IS NOT ADDED TO THE CART..*****")


    def test_checkout_spp_no_size_without_engraving(self):
        SKU2 = random.choice(self.SKU2_LIST)
        print(f"[CHECKOUT] SKU2: {SKU2}")
        try:
            self.search.test_search_with_sku(SKU2)
            delivery_date = self.get_text(self.DELIVERY_DATE_WITHOUT_ENGRAVING).strip()
            self.click(self.ADD_TO_BAG_CTA)
            self.timeout(2000)
            print(f"[CHECKOUT] SKU: {SKU2} [ADDED WITHOUT ENGRAVING], DELIVERY DATE: {delivery_date.upper()}..")
            #self.screenshot.take_Page_screenshot("CHECKOUT_SPP_NO_SIZE_ADD_BAG")
            self.click(self.minicart_close_icon)
        except:
            print(f"*****[CHECKOUT] SPP WITHOUT SIZE [WITHOUT ENGRAVING] {SKU2} IS NOT ADDED TO THE CART..*****")

    def test_secure_checkout_from_minicart(self):
        try:
            self.click(self.minicart_secure_checkout)
            self.timeout(5000)
            print(f"[CHECKOUT-MINI CART] USER IS PROCEED WITH THE CHECKOUT PROCESS..")
        except:
            print("*****[CHECKOUT-MINI CART] NOT ABLE TO PROCEED WITH THE CHECKOUT PROCESS..*****")

