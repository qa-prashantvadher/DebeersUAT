from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
from pages.open_website import OpenHomePage
from dotenv import load_dotenv
import os
load_dotenv(override=True)


class Open_Menu_Header_Options (BasePage):
    URL = os.getenv('BASE_URL')
    COUNTRY = os.getenv('LOCALE')

    menu_icon = "button.btn.btn-hamburger.js-btn-hamburger.p-0.d-flex.align-items-center.text-nowrap.header__hamburger-trigger.me-12.me-lg-16:visible"

    locate_a_store_option = "//ul[@class='quick-links__list menu__quick-links quick-links']//li[1]//button"
    book_appointment_option = "//ul[@class='quick-links__list menu__quick-links quick-links']//li[2]//a"
    delivery_returns_option = "//ul[@class='quick-links__list menu__quick-links quick-links']//li[4]//a"
    contact_us_option = "//ul[@class='quick-links__list menu__quick-links quick-links']//li[5]//a"

    country_language_selector = "//*[@id='languageSelectorLink']"

    choose_language_dropdown = "//*[@id='languageHeading']/button"

    choose_country_dropdown = "//*[@id='countryHeading']/button"
    if COUNTRY == "US":
        # US Country Records
        country_value_locator = {
            "australia": "//*[@id='accordionCountrySelector_mobile']/li[1]/a",
            "austria": "//*[@id='accordionCountrySelector_mobile']/li[2]/a",
            "belgium": "//*[@id='accordionCountrySelector_mobile']/li[3]/a",
            "canada": "//*[@id='accordionCountrySelector_mobile']/li[4]/a",
            "china": "//*[@id='accordionCountrySelector_mobile']/li[5]/a",
            "france": "//*[@id='accordionCountrySelector_mobile']/li[6]/a",
            "germany": "//*[@id='accordionCountrySelector_mobile']/li[7]/a",
            "greece": "//*[@id='accordionCountrySelector_mobile']/li[8]/a",
            "hongkong": "//*[@id='accordionCountrySelector_mobile']/li[9]/a",
            "italy": "//*[@id='accordionCountrySelector_mobile']/li[10]/a",
            "macau": "//*[@id='accordionCountrySelector_mobile']/li[11]/a",
            "netherlands": "//*[@id='accordionCountrySelector_mobile']/li[12]/a",
            "sweden": "//*[@id='accordionCountrySelector_mobile']/li[13]/a",
            "taiwan": "//*[@id='accordionCountrySelector_mobile']/li[14]/a",
            "us": "//*[@id='accordionCountrySelector_mobile']/li[16]/a"
        }
        # Language Records
        language_value_locator = {
            "french": "//div[@id='navigation']//div[@class='accordion-item']//li[2]//a",
            "chinese": "//div[@id='navigation']//div[@class='accordion-item']//li[3]//a",
            "english": "//div[@id='navigation']//div[@class='accordion-item']//li[1]//a"
        }
    elif COUNTRY == "UK":
        # UK Country Records
        country_value_locator = {
            "australia": "//*[@id='accordionCountrySelector_mobile']/li[1]/a",
            "austria": "//*[@id='accordionCountrySelector_mobile']/li[2]/a",
            "belgium": "//*[@id='accordionCountrySelector_mobile']/li[3]/a",
            "canada": "//*[@id='accordionCountrySelector_mobile']/li[4]/a",
            "china": "//*[@id='accordionCountrySelector_mobile']/li[5]/a",
            "france": "//*[@id='accordionCountrySelector_mobile']/li[6]/a",
            "germany": "//*[@id='accordionCountrySelector_mobile']/li[7]/a",
            "greece": "//*[@id='accordionCountrySelector_mobile']/li[8]/a",
            "hongkong": "//*[@id='accordionCountrySelector_mobile']/li[9]/a",
            "italy": "//*[@id='accordionCountrySelector_mobile']/li[10]/a",
            "macau": "//*[@id='accordionCountrySelector_mobile']/li[11]/a",
            "netherlands": "//*[@id='accordionCountrySelector_mobile']/li[12]/a",
            "sweden": "//*[@id='accordionCountrySelector_mobile']/li[13]/a",
            "taiwan": "//*[@id='accordionCountrySelector_mobile']/li[14]/a",
            "uk": "//*[@id='accordionCountrySelector_mobile']/li[15]/a"
        }
        # Language Records
        language_value_locator = {
            "french": "//div[@id='navigation']//div[@class='accordion-item']//li[2]//a",
            "chinese": "//div[@id='navigation']//div[@class='accordion-item']//li[3]//a",
            "english": "//div[@id='navigation']//div[@class='accordion-item']//li[1]//a"
        }
    elif COUNTRY == "FR":
        # FR Country Records
        country_value_locator = {
            "australia": "//*[@id='accordionCountrySelector_mobile']/li[1]/a",
            "austria": "//*[@id='accordionCountrySelector_mobile']/li[2]/a",
            "belgium": "//*[@id='accordionCountrySelector_mobile']/li[3]/a",
            "canada": "//*[@id='accordionCountrySelector_mobile']/li[4]/a",
            "china": "//*[@id='accordionCountrySelector_mobile']/li[5]/a",
            "france": "//*[@id='accordionCountrySelector_mobile']/li[6]/a",
            "germany": "//*[@id='accordionCountrySelector_mobile']/li[7]/a",
            "greece": "//*[@id='accordionCountrySelector_mobile']/li[8]/a",
            "hongkong": "//*[@id='accordionCountrySelector_mobile']/li[9]/a",
            "italy": "//*[@id='accordionCountrySelector_mobile']/li[10]/a",
            "macau": "//*[@id='accordionCountrySelector_mobile']/li[11]/a",
            "netherlands": "//*[@id='accordionCountrySelector_mobile']/li[12]/a",
            "sweden": "//*[@id='accordionCountrySelector_mobile']/li[13]/a",
            "taiwan": "//*[@id='accordionCountrySelector_mobile']/li[14]/a",
            "uk": "//*[@id='accordionCountrySelector_mobile']/li[15]/a"
        }
        # Language Records
        language_value_locator = {
            "chinese": "//div[@id='navigation']//div[@class='accordion-item']//li[3]//a",
            "english": "//div[@id='navigation']//div[@class='accordion-item']//li[1]//a",
            "french": "//div[@id='navigation']//div[@class='accordion-item']//li[2]//a"
        }
    header_client_service_icon = "//*[@id='headerClientSupport']//a[@id='headerClientSupportButton']"
    header_wishlist_icon = "//*[@id='headerWishlist']/a"

    close_menu = "(//div[contains(@class,'menu__nav-header')]//button[contains(@class,'btn-closemenu')])[1]"


    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)
        self.website = OpenHomePage(page)

    def test_open_locate_a_store_page_from_menu(self):
        try:
            self.click(self.menu_icon)
            self.timeout(1000)
            self.click(self.locate_a_store_option)
            self.timeout(4000)
            print("[MENU] STORE LOCATOR PAGE IS NOW VISIBLE..")
        except:
            print("*****[MENU] NOT ABLE TO OPEN STORE LOCATOR PAGE..*****")

    def test_open_book_appointment_page_from_menu(self):
        try:
            self.click(self.menu_icon)
            self.timeout(1000)
            self.click(self.book_appointment_option)
            self.timeout(4000)
            print("[MENU] BOOK AN APPOINTMENT PAGE IS NOW VISIBLE..")
        except:
            print("*****[MENU] NOT ABLE TO OPEN BOOK AN APPOINTMENT PAGE..*****")

    def test_open_delivery_returns_page_from_menu(self):
        try:
            self.click(self.menu_icon)
            self.timeout(1000)
            self.click(self.delivery_returns_option)
            self.timeout(3000)
            print("[MENU] DELIVERY & RETURNS PAGE IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("MENU_DELIVERY_RETURNS")
        except:
            print("*****[MENU] NOT ABLE TO OPEN DELIVERY & RETURNS PAGE..*****")

    def test_open_contact_us_from_menu(self):
        try:
            self.click(self.menu_icon)
            self.timeout(1000)
            self.click(self.contact_us_option)
            self.timeout(3000)
            print("[MENU] CLIENT SERVICE PAGE IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("MENU_CLIENT_SERVICES")
        except:
            print("*****[MENU] NOT ABLE TO OPEN CLIENT SERVICES PAGE..*****")

    def test_open_contact_us_from_header(self):
        try:
            self.click(self.header_client_service_icon)
            self.timeout(3000)
            print("[HEADER] CLIENT SERVICE PAGE IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("HEADER_CLIENT_SERVICES")
        except:
            print("*****[HEADER] NOT ABLE TO OPEN CLIENT SERVICES PAGE..*****")

    def test_open_wishlist_page_header(self):
        try:
            self.click(self.header_wishlist_icon)
            self.timeout(3000)
            print("[HEADER] WISHLIST PAGE IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("HEADER_WISHLIST")
        except:
            print("*****[HEADER] NOT ABLE TO OPEN WISHLIST PAGE..*****")


    def test_change_language_menu(self):
        try:
            for language_name, locator in self.language_value_locator.items():
                 self.timeout(2000)
                 self.click(self.menu_icon)
                 self.timeout(1000)
                 self.click(self.country_language_selector)
                 self.timeout(1000)
                 self.click(self.choose_language_dropdown)
                 self.timeout(1000)
                 print("[MENU] LANGUAGE SECTION IS NOW EXPANDED..")
                 #self.screenshot.take_Page_screenshot("MENU_LANGUAGE_EXPANDED")
                 self.click(locator)
                 self.timeout(5000)
                 page_url = self.page.url
                 print(f"[MENU] '{language_name.upper()}' LANGUAGE IS SELECTED. CURRENT URL: {page_url.upper()}")
                 self.screenshot.take_page_screenshot(f"MENU_LANGUAGE_{language_name.upper()}")
        except:
                 print("[MENU] NOT ABLE TO CHANGE LANGUAGE DETAILS..")

    def test_change_country_menu(self):
        try:
            for country_name, locator in self.country_value_locator.items():
                 self.timeout(2000)
                 self.click(self.menu_icon)
                 self.timeout(1000)
                 self.click(self.country_language_selector)
                 self.timeout(1000)
                 self.click(self.choose_country_dropdown)
                 self.timeout(2000)
                 print("[MENU] COUNTRY SECTION IS NOW EXPANDED..")
                 #self.screenshot.take_Page_screenshot("MENU_COUNTRY_EXPANDED")
                 self.timeout(1000)
                 self.click(locator)
                 self.timeout(8000)
                 try:
                    self.timeout(2000)
                    self.website.test_cookie_consent()
                    self.timeout(2000)
                    self.website.test_country_selector()
                 except:
                     print("[COOKIE] COOKIE CONSENT AND COUNTRY POPUP IS NOT VISIBLE..")
                 self.timeout(2000)
                 page_url = self.page.url
                 print(f"[MENU] '{country_name.upper()}' COUNTRY IS SELECTED. CURRENT URL: {page_url.upper()}")
                 self.screenshot.take_page_screenshot(f"MENU_COUNTRY_{country_name.upper()}")
                 self.navigate(self.URL)
                 print(f"[HOME PAGE] NAVIGATED TO: {self.URL.upper()}")
                 self.timeout(5000)
                 
        except:
            print("[MENU] NOT ABLE TO CHANGE COUNTRY DETAILS..")