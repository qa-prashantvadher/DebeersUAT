from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
from pages.take_screenshot import PageScreenshot
from dotenv import load_dotenv
import os
import logging

load_dotenv(override=True)
logger = logging.getLogger(__name__)

class Search_Locator_Page(BasePage):
    COUNTRY = os.getenv("LOCALE").upper()

    stores_icon_header = "//*[@id='storeLocatorButton']"
    search_store_input = "//*[@id='storeLocator-store-address']"
    show_list_section = "//*[@id='js-show-list']"
    close_icon = "button[class='storeLocator-close']"

    if COUNTRY == "UK" or COUNTRY == "US":
        show_all_stores_section = "//*[@id='js-view-all']"
        europe_in_show_all="h3:has-text('EUROPE')"
        middle_east_in_show_all="h3:has-text('MIDDLE EAST')"
        americas_in_show_all="h3:has-text('AMERICAS')"
        asia_in_show_all="h3:has-text('ASIA')"

        # STORE LINK IN RESULT
        paris_flagship_store = "//a[.//h3[normalize-space()='Paris Flagship Store']]"
        london_old_bond_street = "//a[.//h3[normalize-space()='London Old Bond Street']]"
        new_york_madison_avenue = "//a[.//h3[normalize-space()='New York Madison Avenue']]"

        # MAP
        london_old_bond_street_map_marker = "gmp-advanced-marker[title='London Old Bond Street'] div[class='js-store-marker'] svg"
        paris_flagship_store_map_marker="gmp-advanced-marker[title='Paris Flagship Store'] div[class='js-store-marker'] svg"
        new_york_madison_avenue_map_marker="gmp-advanced-marker[title='New York Madison Avenue'] div[class='js-store-marker'] svg"
        hover_map_marker_close = "button[class='gm-ui-hover-effect']"

    elif COUNTRY == "FR":
        show_all_stores_section = "//*[@id='js-view-all']"
        europe_in_show_all = "h3:has-text('Europe')"
        middle_east_in_show_all = "h3:has-text('Moyen-Orient')"
        americas_in_show_all = "h3:has-text('Amérique')"
        asia_in_show_all = "h3:has-text('Asie')"

        # STORE LINK IN RESULT
        paris_flagship_store = "//a[.//h3[normalize-space()='Paris Flagship Store']]"
        london_old_bond_street = "//a[.//h3[normalize-space()='Londres Old Bond Street']]"
        new_york_madison_avenue = "//a[.//h3[normalize-space()='New York Madison Avenue']]"

        # MAP
        london_old_bond_street_map_marker = "gmp-advanced-marker[title='Londres Old Bond Street'] div[class='js-store-marker'] svg"
        paris_flagship_store_map_marker = "gmp-advanced-marker[title='Paris Flagship Store'] div[class='js-store-marker'] svg"
        new_york_madison_avenue_map_marker = "gmp-advanced-marker[title='New York Madison Avenue'] div[class='js-store-marker'] svg"
        hover_map_marker_close = "button[class='gm-ui-hover-effect']"

    elif COUNTRY == "HK" or COUNTRY == "TW" or COUNTRY == "MO":
        show_all_stores_section = "//*[@id='js-view-all']"
        europe_in_show_all = "h3:has-text('歐洲')"
        middle_east_in_show_all = "h3:has-text('中東')"
        americas_in_show_all = "h3:has-text('美洲')"
        asia_in_show_all = "h3:has-text('亞洲')"

        # STORE LINK IN RESULT
        paris_flagship_store = "//a[.//h3[normalize-space()='Paris Flagship Store']]"
        london_old_bond_street = "//a[.//h3[normalize-space()='London Old Bond Street']]"
        new_york_madison_avenue = "//a[.//h3[normalize-space()='New York Madison Avenue']]"

        # MAP
        london_old_bond_street_map_marker = "gmp-advanced-marker[title='London Old Bond Street'] div[class='js-store-marker'] svg"
        paris_flagship_store_map_marker = "gmp-advanced-marker[title='Paris Flagship Store'] div[class='js-store-marker'] svg"
        new_york_madison_avenue_map_marker = "gmp-advanced-marker[title='New York Madison Avenue'] div[class='js-store-marker'] svg"
        hover_map_marker_close = "button[class='gm-ui-hover-effect']"

    #STORE DETAIL PAGE
    opening_hour = "//div[@class='storeDetails__title']"
    book_appointment_cta = "//div[@id='bookAppointment']/a[@class='btn btn-primary store-details-app-button']"

    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)

    def test_open_store_locator_page_from_header(self):
        try:
            self.click(self.stores_icon_header)
            self.timeout(3000)
            logger.info("[HEADER] STORE LOCATOR PAGE IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("STORE_LOCATOR_PAGE")
        except:
            logger.error("*****[HEADER] NOT ABLE TO OPEN STORE LOCATOR PAGE..*****")

    def test_close_store_locator_page(self):
        try:
            self.click(self.close_icon)
            self.timeout(3000)
            logger.info("[STORE LOCATOR] STORE LOCATOR PAGE IS NOW CLOSED..")
            #self.screenshot.take_Page_screenshot("STORE_LOCATOR_CLOSE")
        except:
            logger.error("*****[STORE LOCATOR] NOT ABLE TO CLOSE STORE LOCATOR PAGE..*****")

    def test_show_all_show_list_store(self):
        try:
            self.click(self.show_all_stores_section)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("STORE_LOCATOR_SHOW_ALL")
            self.scroll_down(self.middle_east_in_show_all)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("STORE_LOCATOR_SHOW_ALL_MIDDLE_EAST")
            self.scroll_down(self.americas_in_show_all)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("STORE_LOCATOR_SHOW_ALL_AMERICAS")
            self.scroll_down(self.asia_in_show_all)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("STORE_LOCATOR_SHOW_ALL_ASIA")
            self.click(self.show_list_section)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("STORE_LOCATOR_SHOW_LIST")
            logger.info("[STORE LOCATOR] PAGE IS NOW VISIBLE WITH THE SHOW ALL SECTION..")
        except:
            logger.error("*****[STORE LOCATOR] NOT ABLE TO OPEN SHOW ALL SECTION..*****")

    def test_search_store_by_keyword(self,keyword):
        try:
            self.fill(self.search_store_input, keyword)
            self.press(self.search_store_input, "Enter")
            self.timeout(3000)
            #self.screenshot.take_Page_screenshot(f"STORE_SEARCH_{keyword}")
            logger.info(f"[STORE LOCATOR] PAGE IS NOW VISIBLE WITH THE KEYWORD:{keyword.upper()}..")
        except:
            logger.error("*****[STORE LOCATOR] NOT ABLE TO SEARCH RECORDS..*****")

    def test_click_close_london_marker_in_map(self):
        try:
            self.is_visible(self.london_old_bond_street_map_marker)
            self.click(self.london_old_bond_street_map_marker)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("LONDON_STORE_OPEN_MAP_MARKER")
            self.click(self.hover_map_marker_close)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("STORE_LONDON_MAP_MARKER_CLOSE")
            logger.info("[LONDON] MAP MARKER IS SUCCESSFULLY OPENED AND CLOSED..")
        except:
            logger.error("*****[LONDON] NOT ABLE OPEN AND CLOSE MARKER IN THE MAP..*****")

    def test_click_close_paris_flagship_in_map(self):
        try:
            self.is_visible(self.paris_flagship_store_map_marker)
            self.click(self.paris_flagship_store_map_marker)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("PARIS_STORE_OPEN_MAP_MARKER")
            self.click(self.hover_map_marker_close)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("STORE_PARIS_MAP_MARKER_CLOSE")
            logger.info("[PARIS] MAP MARKER IS SUCCESSFULLY OPENED AND CLOSED..")
        except:
            logger.error("*****[PARIS] NOT ABLE OPEN AND CLOSE MARKER IN THE MAP..*****")

    def test_click_close_new_york_madison_avenue_in_map(self):
        try:
            self.is_visible(self.new_york_madison_avenue_map_marker)
            self.click(self.new_york_madison_avenue_map_marker)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("NEW_YORK_STORE_OPEN_MAP_MARKER")
            self.click(self.hover_map_marker_close)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("STORE_NEW_YORK_MAP_MARKER_CLOSE")
            logger.info("[NEW YORK] MAP MARKER IS SUCCESSFULLY OPENED AND CLOSED..")
        except:
            logger.error("*****[NEW YORK] NOT ABLE OPEN AND CLOSE MARKER IN THE MAP..*****")

    def test_open_new_york_store_detail_page(self):
        try:
            self.click(self.new_york_madison_avenue)
            self.timeout(4000)
            self.scroll_down(self.opening_hour)
            self.timeout(1000)
            self.screenshot.take_page_screenshot("NEW_YORK_STORE_DETAIL")
            logger.info("[STORE DETAIL] USER IS REDIRECTED TO THE NEW YORK STORE DETAIL PAGE..")
        except:
            logger.error("*****[STORE DETAIL] NOT ABLE TO OPEN NEW YORK STORE DETAIL PAGE FROM THE RESULTS..*****")

    def test_open_london_store_detail_page(self):
        try:
            self.click(self.london_old_bond_street)
            self.timeout(4000)
            self.scroll_down(self.opening_hour)
            self.timeout(1000)
            self.screenshot.take_page_screenshot("LONDON_STORE_DETAIL")
            logger.info("[STORE DETAIL] USER IS REDIRECTED TO THE LONDON STORE DETAIL PAGE..")
        except:
            logger.error("*****[STORE DETAIL] NOT ABLE TO OPEN LONDON STORE DETAIL PAGE FROM THE RESULTS..*****")

    def test_open_paris_store_detail_page(self):
         try:
            self.click(self.paris_flagship_store)
            self.timeout(4000)
            self.scroll_down(self.opening_hour)
            self.timeout(1000)
            self.screenshot.take_page_screenshot("PARIS_STORE_DETAIL")
            logger.info("[STORE DETAIL] USER IS REDIRECTED TO THE PARIS STORE DETAIL PAGE..")
         except:
            logger.error("*****[STORE DETAIL] NOT ABLE TO OPEN PARIS STORE DETAIL PAGE FROM THE RESULTS..*****")

    def test_book_an_appointment_cta_store_detail_page(self):
        try:
            self.timeout(2000)
            self.click(self.book_appointment_cta)
            self.timeout(8000)
            logger.info("[STORE DETAIL] USER IS REDIRECTED TO THE BOOK AN APPOINTMENT PAGE..")
            #self.screenshot.take_Page_screenshot("STORE_DETAIL_APPOINTMENT")
        except:
            logger.error("*****[STORE DETAIL] USER IS NOT REDIRECTED TO THE BOOK AN APPOINTMENT PAGE..*****")
