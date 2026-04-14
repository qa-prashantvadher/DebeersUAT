from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
from dotenv import load_dotenv
import os

load_dotenv(override=True)

class FAQ_Page(BasePage):
    COUNTRY = os.getenv("LOCALE")

    #FAQ Categories
    online_shopping_category = "//*[@id='online-shoping-tab']"
    your_account_category = "//*[@id='your-account-tab']"
    your_store_visit_category = "//*[@id='your-store-visit-tab']"
    our_diamonds_metals_category = "//*[@id='diamonds-metals-tab']"
    diamond_care_aftersales_services_category = "//*[@id='diamond-care-aftersales-tab']"
    our_brand_category = "//*[@id='our-brand-tab']"
    debeers_group_category = "//*[@id='debeers-group-tab']"
    affirm_category = "//*[@id='affirm-tab']"

    if COUNTRY == "US":
        affirm_category = "//*[@id='affirm-tab']"
    elif COUNTRY == "UK":
        klarna_category = "//*[@id='klarna-tab']"
    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)


    def test_all_faq_categories(self):
         try:
             self.click(self.your_account_category)
             print("[FAQ] YOUR ACCOUNT CATEGORY TAB IS SELECTED..")
             #self.screenshot.take_Page_screenshot("FAQ_YOUR_ACCOUNT")

             self.click(self.your_store_visit_category)
             print("[FAQ] YOUR STORE VISIT CATEGORY TAB IS SELECTED..")
             #self.screenshot.take_Page_screenshot("FAQ_YOUR_STORE_VISIT")

             self.click(self.our_diamonds_metals_category)
             print("[FAQ] OUR DIAMONDS & METALS CATEGORY TAB IS SELECTED..")
             #self.screenshot.take_Page_screenshot("FAQ_OUR_DIAMONDS")

             self.click(self.diamond_care_aftersales_services_category)
             print("[FAQ] DIAMOND CARE & AFTER SALES SERVICES CATEGORY TAB IS SELECTED..")
             #self.screenshot.take_Page_screenshot("FAQ_DIAMOND_CARE")

             self.click(self.our_brand_category)
             print("[FAQ] OUR BRAND CATEGORY TAB IS SELECTED..")
             #self.screenshot.take_Page_screenshot("FAQ_OUR_BRAND")

             self.click(self.debeers_group_category)
             print("[FAQ] DEBEERS GROUP CATEGORY TAB IS SELECTED..")
             #self.screenshot.take_Page_screenshot("FAQ_DEBEERS_GROUP")

             if self.COUNTRY == "US":
                 self.click(self.affirm_category)
                 print("[FAQ] AFFIRM CATEGORY TAB IS SELECTED..")
                 #self.screenshot.take_Page_screenshot("FAQ_AFFIRM)

             elif self.COUNTRY == "UK":
                 self.click(self.klarna_category)
                 print("[FAQ] KLARNA CATEGORY TAB IS SELECTED..")
                 # self.screenshot.take_Page_screenshot("FAQ_KLARNA")

             self.click(self.online_shopping_category)
             print("[FAQ] ONLINE SHOPPING CATEGORY TAB IS SELECTED..")
             #self.screenshot.take_Page_screenshot("FAQ_ONLINE_SHOPPING")

         except:
             print("*****[FAQ] NOT ABLE TO VIEW FAQ CATEGORIES..*****")


