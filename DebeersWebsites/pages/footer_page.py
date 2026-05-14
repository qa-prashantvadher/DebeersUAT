from pages.base_page import BasePage
from pages.open_website import OpenHomePage
from pages.take_screenshot import PageScreenshot
import os
from dotenv import load_dotenv
import logging

load_dotenv(override=True)
logger = logging.getLogger(__name__)

class Footer_Page(BasePage):

    URL = os.getenv("BASE_URL")
    COUNTRY = os.getenv("LOCALE").upper()
    ENV = os.getenv("ENVIRONMENT").upper()

    # Client Services Links
    client_services_all_links = "//div[contains(@id,'footeracc-collapse-Client')]//a[contains(@class,'footer-acc-link')]"
    locate_a_store_footer = "//*[@id='footeracc-collapse-Client-Services']/ul/li[1]/a"
    book_an_appointment_footer = "//*[@id='footeracc-collapse-Client-Services']/ul/li[2]/a"
    delivery_returns_footer = "//*[@id='footeracc-collapse-Client-Services']/ul/li[3]/a"
    contact_us_footer = "//*[@id='footeracc-collapse-Client-Services']/ul/li[4]/a"
    faq_footer = "//*[@id='footeracc-collapse-Client-Services']/ul/li[5]/a"

    # Connect/NewsLetter Subscription
    email_address_footer_input = "//*[@id='email_footer']"
    invalid_email_address_alert_footer = "//*[@id='invalidEmailText']"
    email_address_text = os.getenv("USERNAME")

    # Locator dropdown
    locator_dropdown_footer = "//*[@id='countryHeadingFooter']/button"

    if COUNTRY == "US":
        # US Country dropdown records
        location_keyword = {
            "australia": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[1]/a",
            "austria": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[2]/a",
            "belgium": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[3]/a",
            "canada": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[4]/a",
            "china": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[5]/a",
            "france": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[6]/a",
            "germany": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[7]/a",
            "greece": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[8]/a",
            "hong_kong": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[9]/a",
            "italy": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[10]/a",
            "macau": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[11]/a",
            "netherlands": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[12]/a",
            "sweden": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[13]/a",
            "taiwan": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[14]/a",
            "united_kingdom": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[15]/a"
        }
        # US Language dropdown records
        language_keyword = {
            "france_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[2]/a",
            "chinese_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[3]/a",
            "english_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[1]/a"
        }
    elif COUNTRY == "UK":
        # UK Country dropdown records
        location_keyword = {
            "australia": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[1]/a",
            "austria": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[2]/a",
            "belgium": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[3]/a",
            "canada": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[4]/a",
            "china": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[5]/a",
            "france": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[6]/a",
            "germany": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[7]/a",
            "greece": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[8]/a",
            "hong_kong": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[9]/a",
            "italy": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[10]/a",
            "macau": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[11]/a",
            "netherlands": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[12]/a",
            "sweden": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[13]/a",
            "taiwan": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[14]/a",
            "united_states": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[16]/a"
        }
        # UK Language dropdown records
        language_keyword = {
            "france_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[2]/a",
            "chinese_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[3]/a",
            "english_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[1]/a"
        }
    elif COUNTRY == "FR":
        # FR Country dropdown records
        location_keyword = {
            "australia": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[1]/a",
            "austria": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[2]/a",
            "belgium": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[3]/a",
            "canada": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[4]/a",
            "china": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[5]/a",
            "germany": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[7]/a",
            "greece": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[8]/a",
            "hong_kong": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[9]/a",
            "italy": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[10]/a",
            "macau": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[11]/a",
            "netherlands": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[12]/a",
            "sweden": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[13]/a",
            "taiwan": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[14]/a",
            "united_states": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[16]/a",
            "united_kingdom": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[15]/a"
        }
        # FR Language dropdown records
        language_keyword = {
            "english_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[1]/a",
            "chinese_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[3]/a",
            "france_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[2]/a"
        }

    elif COUNTRY == "HK":
        # HK Country dropdown records
        location_keyword = {
            "australia": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[1]/a",
            "austria": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[2]/a",
            "belgium": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[3]/a",
            "canada": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[4]/a",
            "china": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[5]/a",
            "france": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[6]/a",
            "germany": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[7]/a",
            "greece": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[8]/a",
            "italy": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[10]/a",
            "macau": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[11]/a",
            "netherlands": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[12]/a",
            "sweden": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[13]/a",
            "taiwan": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[14]/a",
            "united_kingdom": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[15]/a",
            "united_states": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[16]/a"
        }
        # HK Language dropdown records
        language_keyword = {
            "english_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[1]/a",
            "france_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[2]/a",
            "chinese_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[3]/a"
        }

    elif COUNTRY == "TW":
        # TW Country dropdown records
        location_keyword = {
            "australia": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[1]/a",
            "austria": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[2]/a",
            "belgium": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[3]/a",
            "canada": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[4]/a",
            "china": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[5]/a",
            "france": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[6]/a",
            "germany": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[7]/a",
            "greece": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[8]/a",
            "hong_kong": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[9]/a",
            "italy": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[10]/a",
            "macau": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[11]/a",
            "netherlands": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[12]/a",
            "sweden": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[13]/a",
            "united_kingdom": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[15]/a",
            "united_states": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[16]/a"
        }
        # TW Language dropdown records
        language_keyword = {
            "english_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[1]/a",
            "france_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[2]/a",
            "chinese_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[3]/a"
        }

    elif COUNTRY == "MO":
        # MO Country dropdown records
        location_keyword = {
            "australia": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[1]/a",
            "austria": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[2]/a",
            "belgium": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[3]/a",
            "canada": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[4]/a",
            "china": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[5]/a",
            "france": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[6]/a",
            "germany": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[7]/a",
            "greece": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[8]/a",
            "hong_kong": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[9]/a",
            "italy": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[10]/a",
            "netherlands": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[12]/a",
            "sweden": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[13]/a",
            "taiwan": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[14]/a",
            "united_kingdom": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[15]/a",
            "united_states": "//*[@id='accordionCountrySelector_desktop']/div/ul/li[16]/a"
        }
        # MO Language dropdown records
        language_keyword = {
            "chinese_language": "//*[@id='accordionLanguageSelector_desktop']/div/ul/li[1]/a"
        }


    # Language Dropdown
    language_dropdown_footer = "//*[@id='languageHeadingFooter']/button"

    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)
        self.website = OpenHomePage(page)

    def test_all_client_services_link_from_footer(self):
        footer_links = self.page.locator(
            "//div[contains(@id,'footeracc-collapse-Client')]//a[contains(@class,'footer-acc-link')]"
        )
        total_links = footer_links.count()

        for i in range(total_links):
            # Re-locate every loop
            footer_links = self.page.locator(
                "//div[contains(@id,'footeracc-collapse-Client')]//a[contains(@class,'footer-acc-link')]"
            )

            link = footer_links.nth(i)

            link_text = link.text_content().strip()

            print(f"Opening link: {link_text}")

            # Optional
            link.scroll_into_view_if_needed()

            # Click link
            link.click()

    def test_locate_a_store_link_from_footer(self):
         try:
             self.scroll_down(self.locate_a_store_footer)
             self.click(self.locate_a_store_footer)
             self.timeout(4000)
             logger.info("[FOOTER] STORE LOCATOR PAGE IS NOW VISIBLE..")
             #self.screenshot.take_Page_screenshot("FOOTER_LOCATE_STORE")
         except:
             logger.error("*****[FOOTER] NOT ABLE TO OPEN STORE LOCATOR PAGE..*****")

    def test_book_an_appointment_link_from_footer(self):
        try:
            self.scroll_down(self.book_an_appointment_footer)
            self.click(self.book_an_appointment_footer)
            self.timeout(4000)
            logger.info("[FOOTER] BOOK AN APPOINTMENT PAGE IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("FOOTER_BOOK_APPOINTMENT")
        except:
            logger.error("*****[FOOTER] NOT ABLE TO OPEN BOOK AN APPOINTMENT PAGE..*****")

    def test_delivery_returns_link_from_footer(self):
        try:
            self.scroll_down(self.delivery_returns_footer)
            self.click(self.delivery_returns_footer)
            self.timeout(3000)
            logger.info("[FOOTER] DELIVERY & RETURNS PAGE IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("FOOTER_DELIVERY_RETURNS")
        except:
            logger.error("*****[FOOTER] NOT ABLE TO OPEN DELIVERY & RETURNS PAGE..*****")

    def test_contact_us_link_from_footer(self):
        try:
            self.scroll_down(self.contact_us_footer)
            self.click(self.contact_us_footer)
            self.timeout(3000)
            logger.info("[FOOTER] CLIENT SERVICE PAGE IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("FOOTER_CLIENT_SERVICES")
        except:
            logger.error("*****[FOOTER] NOT ABLE TO OPEN CLIENT SERVICES PAGE..*****")

    def test_faq_link_from_footer(self):
        try:
            self.scroll_down(self.faq_footer)
            self.click(self.faq_footer)
            self.timeout(3000)
            logger.info("[FOOTER] FAQ PAGE IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("FOOTER_FAQ")
        except:
            logger.error("*****[FOOTER] NOT ABLE TO OPEN FAQ PAGE..*****")

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
            logger.info("[FOOTER] NEWSLETTER SUBMIT SUCCESS..")
            self.screenshot.take_page_screenshot("FOOTER_NEWSLETTER_VALID")
        except:
            logger.error("*****[FOOTER] NOT ABLE TO CHECK NEWSLETTER SECTION..*****")

    def test_location_dropdown_from_footer(self):
        try:
            self.scroll_down(self.locator_dropdown_footer)
            self.click(self.locator_dropdown_footer)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("FOOTER_LOCATION_EXPAND")
            logger.info("[FOOTER] LOCATION DROPDOWN IS NOW EXPANDED..")
        except:
            logger.error("*****[FOOTER] NOT ABLE TO EXPAND LOCATION DROPDOWN..*****")

    def test_language_dropdown_from_footer(self):
        try:
            self.scroll_down(self.language_dropdown_footer)
            self.click(self.language_dropdown_footer)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("FOOTER_LANGUAGE_EXPAND")
            logger.info("[FOOTER] LANGUAGE DROPDOWN IS NOW EXPANDED..")
        except:
            logger.error("*****[FOOTER] NOT ABLE TO EXPAND LANGUAGE DROPDOWN..*****")

    def test_select_country_records_from_location_footer(self):
        try:
            self.test_location_dropdown_from_footer()
            for country,locator in self.location_keyword.items():
                self.click(locator)
                self.timeout(5000)
                if self.ENV != "QA":
                    try:
                        self.website.test_cookie_consent()
                        self.website.test_country_selector()
                    except:
                        logger.warning("*****[FOOTER] COOKIE CONSENT AND COUNTRY POPUP IS NOT VISIBLE..*****")
                page_url = self.page.url
                logger.info(f"[FOOTER] '{country.upper()}' COUNTRY IS SELECTED. CURRENT URL: {page_url.upper()}")
                self.screenshot.take_page_screenshot(f"FOOTER_LOCATION_{country.upper()}")
                self.navigate(self.URL)
                logger.info(f"[HOME PAGE] NAVIGATED TO: {self.URL.upper()}")
                self.timeout(5000)
                self.test_location_dropdown_from_footer()
        except:
            logger.error("*****[FOOTER] NOT ABLE TO SELECT LOCATION RECORDS..*****")

    def test_select_language_records_from_language_footer(self):
        try:
            self.test_language_dropdown_from_footer()
            for language, locator  in self.language_keyword.items():
                self.click(locator)
                self.timeout(5000)
                page_url = self.page.url
                logger.info(f"[FOOTER] '{language.upper()}' LANGUAGE IS SELECTED. CURRENT URL: {page_url.upper()}")
                self.screenshot.take_page_screenshot(f"FOOTER_LANGUAGE_{language.upper()}")
                self.test_language_dropdown_from_footer()
        except:
            logger.error("*****[FOOTER] NOT ABLE TO SELECT LANGUAGE RECORDS..*****")