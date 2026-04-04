from pages.base_page import BasePage
from pages.open_website import OpenHomePage
from pages.take_screenshot import PageScreenshot
import os


class Footer_Page(BasePage):

    #Client Services Links
    locate_a_store_footer = "//*[@id='footeracc-collapse-Client-Services']/ul/li[1]/a"
    book_an_appointment_footer = "//*[@id='footeracc-collapse-Client-Services']/ul/li[2]/a"
    delivery_returns_footer = "//*[@id='footeracc-collapse-Client-Services']/ul/li[3]/a"
    contact_us_footer = "//*[@id='footeracc-collapse-Client-Services']/ul/li[4]/a"
    faq_footer = "//*[@id='footeracc-collapse-Client-Services']/ul/li[5]/a"

    #Connect/NewsLetter Subscription
    email_address_footer_input = "//*[@id='email_footer']"
    invalid_email_address_alert_footer = "//*[@id='invalidEmailText']"
    email_address_text = os.getenv("USERNAME")

    #Locator dropdown
    locator_dropdown_footer = "//*[@id='countryHeadingFooter']/button"

    #Locator dropdown records
    location_keyword = {
       # "australia": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[1]/a",
       # "austria": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[2]/a",
       # "belgium": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[3]/a",
        "canada": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[4]/a",
        "china": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[5]/a",
        "france": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[6]/a",
       # "germany": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[7]/a",
       # "greece": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[8]/a",
        "hong_kong": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[9]/a",
       # "italy": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[10]/a",
        "macau": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[11]/a",
       # "netherlands": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[12]/a",
       # "sweden": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[13]/a",
        "taiwan": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[14]/a",
        "united_kingdom": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[15]/a",
        "united_states": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[16]/a",
    }

    #Language Dropdown
    language_dropdown_footer = "//*[@id='languageHeadingFooter']/button"
    language_keyword = {
        "france_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[2]/a",
        "chinese_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[3]/a",
        "english_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[1]/a"
    }

    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)
        self.website = OpenHomePage(page)


    def test_locate_a_store_link_from_footer(self):
         try:
             self.scroll_down(self.locate_a_store_footer)
             self.click(self.locate_a_store_footer)
             self.timeout(4000)
             print("[FOOTER] STORE LOCATOR PAGE IS NOW VISIBLE..")
             #self.screenshot.take_Page_screenshot("FOOTER_LOCATE_STORE")
         except:
             print("*****[FOOTER] NOT ABLE TO OPEN STORE LOCATOR PAGE..*****")

    def test_book_an_appointment_link_from_footer(self):
        try:
            self.scroll_down(self.book_an_appointment_footer)
            self.click(self.book_an_appointment_footer)
            self.timeout(4000)
            print("[FOOTER] BOOK AN APPOINTMENT PAGE IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("FOOTER_BOOK_APPOINTMENT")
        except:
            print("*****[FOOTER] NOT ABLE TO OPEN BOOK AN APPOINTMENT PAGE..*****")

    def test_delivery_returns_link_from_footer(self):
        try:
            self.scroll_down(self.delivery_returns_footer)
            self.click(self.delivery_returns_footer)
            self.timeout(3000)
            print("[FOOTER] DELIVERY & RETURNS PAGE IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("FOOTER_DELIVERY_RETURNS")
        except:
            print("*****[FOOTER] NOT ABLE TO OPEN DELIVERY & RETURNS PAGE..*****")

    def test_contact_us_link_from_footer(self):
        try:
            self.scroll_down(self.contact_us_footer)
            self.click(self.contact_us_footer)
            self.timeout(3000)
            print("[FOOTER] CLIENT SERVICE PAGE IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("FOOTER_CLIENT_SERVICES")
        except:
            print("*****[FOOTER] NOT ABLE TO OPEN CLIENT SERVICES PAGE..*****")

    def test_faq_link_from_footer(self):
        try:
            self.scroll_down(self.faq_footer)
            self.click(self.faq_footer)
            self.timeout(3000)
            print("[FOOTER] FAQ PAGE IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("FOOTER_FAQ")
        except:
            print("*****[FOOTER] NOT ABLE TO OPEN FAQ PAGE..*****")

    def test_news_letter_from_footer(self):
        try:
            self.scroll_down(self.email_address_footer_input)
            self.fill(self.email_address_footer_input,"test")
            self.press(self.email_address_footer_input,"Enter")
            self.timeout(1000)
            #self.screenshot.take_Page_screenshot("FOOTER_NEWSLETTER_INVALID")

            self.fill(self.email_address_footer_input, "")
            self.press(self.email_address_footer_input, "Enter")
            self.timeout(1000)
            #self.screenshot.take_Page_screenshot("FOOTER_NEWSLETTER_BLANK")

            self.fill(self.email_address_footer_input, self.email_address_text)
            self.press(self.email_address_footer_input, "Enter")
            self.timeout(3000)
            self.screenshot.take_page_screenshot("FOOTER_NEWSLETTER_VALID")
        except:
            print("*****[FOOTER] NOT ABLE TO CHECK NEWSLETTER SECTION..*****")

    def test_location_dropdown_from_footer(self):
        try:
            self.scroll_down(self.locator_dropdown_footer)
            self.click(self.locator_dropdown_footer)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("FOOTER_LOCATION_EXPAND")
            print("[FOOTER] LOCATION DROPDOWN IS NOW EXPANDED..")
        except:
            print("*****[FOOTER] NOT ABLE TO EXPAND LOCATION DROPDOWN..*****")

    def test_language_dropdown_from_footer(self):
        try:
            self.scroll_down(self.language_dropdown_footer)
            self.click(self.language_dropdown_footer)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("FOOTER_LANGUAGE_EXPAND")
            print("[FOOTER] LANGUAGE DROPDOWN IS NOW EXPANDED..")
        except:
            print("*****[FOOTER] NOT ABLE TO EXPAND LANGUAGE DROPDOWN..*****")

    def test_select_country_records_from_location_footer(self):
        try:
            self.test_location_dropdown_from_footer()
            for country,locator in self.location_keyword.items():
                self.click(locator)
                self.timeout(5000)
                try:
                    self.website.test_cookie_consent()
                    self.website.test_country_selector()
                except:
                    print("*****[FOOTER] COOKIE CONSENT AND COUNTRY POPUP IS NOT VISIBLE..*****")
                page_url = self.page.url
                print(f"[FOOTER] '{country.upper()}' COUNTRY IS SELECTED. CURRENT URL: {page_url.upper()}")
                self.screenshot.take_page_screenshot(f"FOOTER_LOCATION_{country.upper()}")
                self.test_location_dropdown_from_footer()
        except:
            print("*****[FOOTER] NOT ABLE TO SELECT LOCATION RECORDS..*****")

    def test_select_language_records_from_language_footer(self):
        try:
            self.test_language_dropdown_from_footer()
            for language, locator  in self.language_keyword.items():
                self.click(locator)
                self.timeout(5000)
                page_url = self.page.url
                print(f"[FOOTER] '{language.upper()}' LANGUAGE IS SELECTED. CURRENT URL: {page_url.upper()}")
                self.screenshot.take_page_screenshot(f"FOOTER_LANGUAGE_{language.upper()}")
                self.test_language_dropdown_from_footer()
        except:
            print("*****[FOOTER] NOT ABLE TO SELECT LANGUAGE RECORDS..*****")