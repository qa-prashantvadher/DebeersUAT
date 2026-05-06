from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
from dotenv import load_dotenv
import os
import logging

load_dotenv(override=True)
logger = logging.getLogger(__name__)

class Open_EngagementRings_PLP_Page(BasePage):
    COUNTRY = os.getenv("LOCALE").upper()

    menu_icon = "//button[contains(@class,'js-btn-hamburger')]"

    if COUNTRY == "US":
        engagement_bridal_sub_menu = "button[id='N10002'] span[class='menu__nav-link-span']"
        engagement_rings = "a[id='N10050'] span[class='menu__nav-link-span']"


    elif COUNTRY == "UK" or COUNTRY == "FR" or COUNTRY == "HK" or COUNTRY == "TW":
        engagement_bridal_sub_menu = "button[id='G10002'] span[class='menu__nav-link-span']"
        engagement_rings = "a[id='G10050'] span[class='menu__nav-link-span']"

    # PLP Page > Sorting
    sort_by_label = "#sortRefinement button"
    price_ascending = "//input[@id='price-low-to-high']"
    price_descending = "//input[@id='price-high-to-low']"
    slp_page_records = "//*[@id='navbarFilters']/div/div[1]/div[2]/span"

    if COUNTRY == "FR":
        # PLP  Page > Filter
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
        # PLP  Page > Filter
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

    elif COUNTRY == "HK" or COUNTRY == "TW":
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

    def test_open_engagement_rings_plp_page(self):
        try:
            self.click(self.menu_icon)
            self.timeout(2000)
            self.click(self.engagement_bridal_sub_menu)
            self.timeout(2000)
            self.click(self.engagement_rings)
            self.timeout(5000)
            self.scroll_down(self.slp_page_records)
            logger.info("[PLP] USER IS REDIRECTED TO THE ENGAGEMENT RINGS PAGE..")
            result_count = self.inner_text(self.slp_page_records)
            logger.info(f"[PLP] RECORDS WITHOUT SORTING: {result_count.upper()}")
            #self.screenshot.take_Page_screenshot("PLP_WITHOUT_SORTING")
        except:
            logger.error("*****[PLP] USER IS NOT REDIRECTED TO THE ENGAGEMENT RINGS PAGE..*****")

    def test_apply_sorting_on_plp(self):
       try:
            self.click(self.sort_by_label)
            self.timeout(2000)
            self.click(self.price_ascending)
            self.timeout(3000)
            result_count = self.inner_text(self.slp_page_records)
            logger.info(f"[PLP] RECORDS AFTER PRICE ASCENDING SORTING: {result_count.upper()}")
            #self.screenshot.take_Page_screenshot("PLP_SORTING_PRICE_ASCENDING")
            self.click(self.sort_by_label)
            self.timeout(2000)
            self.check(self.price_descending)
            self.timeout(3000)
            result_count = self.inner_text(self.slp_page_records)
            logger.info(f"[PLP] RECORDS AFTER PRICE DESCENDING SORTING: {result_count.upper()}")
            #self.screenshot.take_Page_screenshot("PLP_SORTING_PRICE_DESCENDING")
       except:
            logger.error(f"*****[PLP] UNABLE TO PERFORM SORTING..*****")

    def test_apply_filter_on_plp(self):
        try:
            self.click(self.filter_label)
            self.timeout(2000)
            self.click(self.material_label)
            self.timeout(2000)
            self.click(self.material_option)
            self.timeout(2000)
            self.click(self.material_apply_button)
            self.timeout(5000)
            result_count = self.inner_text(self.slp_page_records)
            logger.info(f"[PLP] RECORDS AFTER APPLYING MATERIAL FILTER: {result_count.upper()}")
            self.screenshot.take_page_screenshot("PLP_FILTER_MATERIAL")


            self.click(self.size_label)
            self.timeout(2000)
            self.click(self.size_50)
            self.timeout(2000)
            self.click(self.size_apply_button)
            self.timeout(5000)
            result_count = self.inner_text(self.slp_page_records)
            logger.info(f"[PLP] RECORDS AFTER APPLYING MATERIAL + SIZE FILTERS: {result_count.upper()}")
            self.screenshot.take_page_screenshot("PLP_FILTER_MATERIAL_SIZE")

            self.click(self.cut_label)
            self.timeout(2000)
            self.click(self.cut_emerald_option)
            self.timeout(2000)
            self.click(self.cut_apply_button)
            self.timeout(5000)
            result_count = self.inner_text(self.slp_page_records)
            logger.info(f"[PLP] RECORDS AFTER APPLYING MATERIAL + SIZE + CUT FILTERS: {result_count.upper()}")
            self.screenshot.take_page_screenshot("PLP_FILTER_MATERIAL_SIZE_CUT")
        except:
            logger.error("*****[PLP] NOT ABLE TO APPLY FILTERS..*****")

    def test_clear_filter_on_plp(self):
        try:
            self.timeout(2000)
            self.click(self.clear_all_filter)
            self.timeout(10000)
            result_count = self.inner_text(self.slp_page_records)
            logger.info(f"[PLP] TOTAL RECORDS AFTER CLEAR FILTER: {result_count.upper()}")
            self.screenshot.take_page_screenshot("PLP_CLEAR_ALL_FILTER")
        except:
            logger.error("*****[PLP] NOT ABE TO CLEAR FILTERS..*****")
