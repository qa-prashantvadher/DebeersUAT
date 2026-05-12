from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
from dotenv import load_dotenv
import os
import logging

load_dotenv(override=True)
logger = logging.getLogger(__name__)


class SearchSKU(BasePage):

    COUNTRY = os.getenv("LOCALE").upper()
    URL = os.getenv("BASE_URL")

    search_icon = "//*[@id='headerSearch']"
    search_keyword_input = "#searchInput"
    first_suggestion = "//*[@id='group-0-option-0']/a"

    contact_us_link_search = "div[id='searchModal'] div[class='content-asset'] li:nth-child(1) a:nth-child(1)"
    faq_link_search = "div[id='searchModal'] div[class='content-asset'] li:nth-child(2) a:nth-child(1)"


    #SLP Page > Sorting
    sort_by_label = "#sortRefinement button"
    price_ascending = "//input[@id='price-low-to-high']"
    price_descending = "//input[@id='price-high-to-low']"
    slp_page_records = "//*[@id='navbarFilters']/div/div[1]/div[2]/span"

    if COUNTRY == "FR":
        # SLP  Page > Filter
        filter_label = "button.btn-filtered.js-show-filters"

        material_label = "//span[@id='métal-label']/ancestor::button"
        material_option = "//*[@id='Platine']"
        material_apply_button = "div[class='refinement-content is-filter-bar productMetal'] a[name='apply']"

        size_label = "//span[@id='taille-label']"
        size_50 = "//div[@id='50']"
        size_apply_button = "div[class='refinement-content is-filter-bar size'] a[name='apply']"

        cut_label = "//span[@id='taille_de_diamant-label']"
        cut_emerald_option = "//div[contains(text(),'Émeraude')]"
        cut_apply_button = "div[class='refinement-content is-filter-bar productCut'] a[name='apply']"

    elif COUNTRY == "UK" or COUNTRY == "US":

        # SLP Page > Filter
        filter_label = "button.btn-filtered.js-show-filters"

        material_label = "button:has-text('Material')"
        material_option = "//*[@id='Platinum']"
        material_apply_button = "div[class='refinement-content is-filter-bar productMetal'] a[name='apply']"

        size_label = "button:has-text('Size')"
        size_50 = "//div[@id='50']"
        size_apply_button = "div[class='refinement-content is-filter-bar size'] a[name='apply']"

        cut_label = "button:has-text('Cut')"
        cut_emerald_option = "//div[contains(text(),'Emerald')]"
        cut_apply_button = "div[class='refinement-content is-filter-bar productCut'] a[name='apply']"

    elif COUNTRY == "HK" or COUNTRY == "TW" or COUNTRY == "MO":
        # PLP  Page > Filter
        filter_label = "button.btn-filtered.js-show-filters"

        material_label = "button:has-text('材質')"
        material_option = "//*[@id='鉑金']"
        material_apply_button = "div[class='refinement-content is-filter-bar productMetal'] a[name='apply']"

        size_label = "button:has-text('尺寸')"
        size_50 = "//div[@id='50']"
        size_apply_button = "div[class='refinement-content is-filter-bar size'] a[name='apply']"

        cut_label = "button:has-text('切')"
        cut_emerald_option = "//div[contains(text(),'祖母綠形')]"
        cut_apply_button = "div[class='refinement-content is-filter-bar productCut'] a[name='apply']"


    clear_all_filter = "//div[@id='filterRefinements']/div[@class='offcanvas-body filters-list']/div[@class='clear-cta-wrapper']/a[@class='refinement-dropdown-clear-cta btn btn-link clearButton']"

    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)

    def test_search_with_sku(self, sku):
        try:
            self.timeout(5000)
            self.click(self.search_icon)
            self.is_visible(self.search_keyword_input)
            self.click(self.search_keyword_input)
            self.fill(self.search_keyword_input, "")
            self.type(self.search_keyword_input, sku)
            self.timeout(3000)
            #self.screenshot.take_Page_screenshot("SEARCH_SKU")
            self.click(self.first_suggestion)
            self.timeout(3000)
            logger.info(f"[SEARCH] SEARCHED WITH THE '{sku}' SKU..")
            #self.screenshot.take_Page_screenshot("SEARCH_SKU_PDP")
        except:
            logger.error(f"*****[SEARCH] NOT ABLE TO SEARCH WITH THE '{sku}' SKU..*****")
            self.navigate(self.URL)

    def test_search_with_keyword(self, keyword):
        try:
            self.timeout(3000)
            self.click(self.search_icon)
            self.is_visible(self.search_keyword_input)
            self.click(self.search_keyword_input)
            self.fill(self.search_keyword_input,"")
            self.type(self.search_keyword_input, keyword)
            self.press(self.search_keyword_input, "Enter")
            self.timeout(3000)
            logger.info(f"[SEARCH] SEARCHED WITH THE '{keyword.upper()}' KEYWORD..")
            #self.screenshot.take_Page_screenshot("SEARCH_KEYWORD_SLP")
        except:
            logger.error(f"*****[SEARCH] NOT ABLE TO SEARCH WITH THE '{keyword.upper()}' KEYWORD..*****")


    def test_apply_sorting_on_slp(self):
       try:
            self.click(self.sort_by_label)
            self.timeout(2000)
            result_count = self.inner_text(self.slp_page_records)
            logger.info(f"[SLP] RECORDS WITHOUT SORTING: {result_count.upper()}")
            #self.screenshot.take_Page_screenshot("SLP_WITHOUT_SORTING")
            self.click(self.price_ascending)
            self.timeout(3000)
            result_count = self.inner_text(self.slp_page_records)
            logger.info(f"[SLP] RECORDS AFTER PRICE ASCENDING SORTING: {result_count.upper()}")
            #self.screenshot.take_Page_screenshot("SLP_SORTING_PRICE_ASCENDING")
            self.click(self.sort_by_label)
            self.timeout(2000)
            self.check(self.price_descending)
            self.timeout(3000)
            result_count = self.inner_text(self.slp_page_records)
            logger.info(f"[SLP] RECORDS AFTER PRICE DESCENDING SORTING: {result_count.upper()}")
            #self.screenshot.take_Page_screenshot("SLP_SORTING_PRICE_DESCENDING")
       except:
             logger.error("*****[SLP] NOT ABLE TO PERFORM SORTING..*****")

    def test_apply_filter_on_slp(self):
        try:
            self.timeout(3000)
            self.click(self.filter_label)
            self.timeout(2000)
            self.click(self.material_label)
            self.timeout(2000)
            self.click(self.material_option)
            self.timeout(2000)
            self.click(self.material_apply_button)
            self.timeout(5000)
            result_count = self.inner_text(self.slp_page_records)
            logger.info(f"[SLP] RECORDS AFTER APPLYING MATERIAL FILTER: {result_count.upper()}")
            self.screenshot.take_page_screenshot("SLP_FILTER_MATERIAL")

            self.click(self.size_label)
            self.timeout(2000)
            self.click(self.size_50)
            self.timeout(2000)
            self.click(self.size_apply_button)
            self.timeout(5000)
            result_count = self.inner_text(self.slp_page_records)
            logger.info(f"[SLP] RECORDS AFTER APPLYING MATERIAL + SIZE FILTERS: {result_count.upper()}")
            self.screenshot.take_page_screenshot("SLP_FILTER_MATERIAL_SIZE")

            self.click(self.cut_label)
            self.timeout(2000)
            self.click(self.cut_emerald_option)
            self.timeout(2000)
            self.click(self.cut_apply_button)
            self.timeout(5000)
            result_count = self.inner_text(self.slp_page_records)
            logger.info(f"[SLP] RECORDS AFTER APPLYING MATERIAL + SIZE + CUT FILTERS: {result_count.upper()}")
            self.screenshot.take_page_screenshot("SLP_FILTER_MATERIAL_SIZE_CUT")
        except:
            logger.error("*****[SLP] NOT ABLE TO APPLY FILTERS..*****")

    def test_clear_filter_on_slp(self):
        try:
            self.timeout(2000)
            self.click(self.clear_all_filter)
            self.timeout(10000)
            result_count = self.inner_text(self.slp_page_records)
            logger.info(f"[SLP] RECORDS AFTER CLEAR FILTER: {result_count.upper()}")
            self.screenshot.take_page_screenshot("SLP_CLEAR_ALL_FILTER")
        except:
            logger.error("*****[SLP] UNABLE TO CLEAR APPLIED FILTERS..*****")

    def test_open_contact_us_page_from_search(self):
        try:
            self.timeout(1000)
            self.click(self.search_icon)
            self.is_visible(self.search_keyword_input)
            self.timeout(2000)
            logger.info("[SEARCH] SEARCH MODAL IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("SEARCH_MODAL")
            self.timeout(2000)
            self.click(self.contact_us_link_search)
            self.timeout(2000)
            logger.info("[SEARCH] USER IS REDIRECTED TO THE CONTACT US PAGE..")
            #self.screenshot.take_Page_screenshot("SEARCH_CONTACT_US")
        except:
            logger.error("*****[SEARCH] NOT ABLE TO OPEN CONTACT US PAGE..*****")

    #Not working so not used as of now
    def test_open_faq_page_from_search(self):
        try:
            self.timeout(1000)
            self.click(self.search_icon)
            self.is_visible(self.search_keyword_input)
            self.timeout(2000)
            logger.info("[SEARCH] SEARCH MODAL IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("SEARCH_MODAL")
            self.timeout(2000)
            self.click(self.faq_link_search)
            self.timeout(2000)
            logger.info("[SEARCH] USER IS REDIRECTED TO THE FAQ PAGE..")
            #self.screenshot.take_Page_screenshot("SEARCH_FAQ")
        except:
            logger.error("*****[SEARCH] NOT ABLE TO OPEN FAQ PAGE..*****")
