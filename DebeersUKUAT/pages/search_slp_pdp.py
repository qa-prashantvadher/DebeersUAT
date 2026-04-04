from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot

class SearchSKU(BasePage):
    search_icon = "//*[@id='headerSearch']"
    search_keyword_input = "#searchInput"
    first_suggestion = "//*[@id='group-0-option-0']/a"

    contact_us_link_search = "div[id='searchModal'] div[class='content-asset'] li:nth-child(1) a:nth-child(1)"
    faq_link_search = "div[id='searchModal'] div[class='content-asset'] li:nth-child(2) a:nth-child(1)"


    #SLP Page > Sorting
    sort_by_label = "#sortRefinement button"
    price_ascending = "//input[@id='price-low-to-high']"
    ascending_label_text = "price ascending"
    descending_label_text = "price descending"
    price_descending = "//input[@id='price-high-to-low']"
    slp_page_records = '//*[@id="navbarFilters"]/div/div[1]/div[2]/span'

    # SLP Page > Filter
    filter_label = "//button[normalize-space()='Filter']"

    material_label = "button:has-text('Material')"
    material_option = "//*[@id='Platinum']"
    material_apply_button = "div[class='refinement-content is-filter-bar productMetal'] a[name='apply']"

    size_label = "button:has-text('Size')"
    size_50 = "//div[@id='50']"
    size_apply_button = "div[class='refinement-content is-filter-bar size'] a[name='apply']"

    cut_label = "button:has-text('Cut')"
    cut_emerald_option = "//div[contains(text(),'Emerald')]"
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
            self.fill(self.search_keyword_input, sku)
            self.timeout(3000)
            #self.screenshot.take_Page_screenshot("SEARCH_SKU")
            self.click(self.first_suggestion)
            self.timeout(3000)
            print(f"SEARCHED WITH THE '{sku}' SKU..")
            #self.screenshot.take_Page_screenshot("SEARCH_SKU_PDP")
        except:
            print(f"*****NOT ABLE TO SEARCH WITH THE '{sku}' SKU..*****")

    def test_search_with_keyword(self, keyword):
        try:
            self.timeout(3000)
            self.click(self.search_icon)
            self.is_visible(self.search_keyword_input)
            self.fill(self.search_keyword_input, keyword)
            self.press(self.search_keyword_input, "Enter")
            self.timeout(3000)
            print(f"SEARCHED WITH THE '{keyword.upper()}' KEYWORD..")
            #self.screenshot.take_Page_screenshot("SEARCH_KEYWORD_SLP")
        except:
            print(f"*****NOT ABLE TO SEARCH WITH THE '{keyword.upper()}' KEYWORD..*****")


    def test_apply_sorting_on_slp(self):
       try:
            self.timeout(2000)
            self.click(self.sort_by_label)
            result_count = self.inner_text(self.slp_page_records)
            print(f"SLP RECORDS [WITHOUT SORTING]: {result_count.upper()}")
            #self.screenshot.take_Page_screenshot("SLP_WITHOUT_SORTING")
            self.click(self.price_ascending)
            self.timeout(3000)
            result_count = self.inner_text(self.slp_page_records)
            print(f"SLP RECORDS [AFTER SORTING: PRICE ASCENDING]: {result_count.upper()}")
            #self.screenshot.take_Page_screenshot("SLP_SORTING_PRICE_ASCENDING")
            self.click(self.sort_by_label)
            self.check(self.price_descending)
            self.timeout(3000)
            result_count = self.inner_text(self.slp_page_records)
            print(f"SLP RECORDS [AFTER SORTING: PRICE DESCENDING]: {result_count.upper()}")
            #self.screenshot.take_Page_screenshot("SLP_SORTING_PRICE_DESCENDING")

       except:
             print("*****NOT ABLE TO PERFORM SORTING ON THE SLP..*****")

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
            print(f"SLP RECORDS [AFTER APPLYING MATERIAL FILTER]: {result_count.upper()}")
            self.screenshot.take_page_screenshot("SLP_FILTER_MATERIAL")

            self.click(self.size_label)
            self.timeout(2000)
            self.click(self.size_50)
            self.timeout(2000)
            self.click(self.size_apply_button)
            self.timeout(5000)
            result_count = self.inner_text(self.slp_page_records)
            print(f"SLP RECORDS [AFTER APPLYING MATERIAL + SIZE FILTERS]: {result_count.upper()}")
            self.screenshot.take_page_screenshot("SLP_FILTER_MATERIAL_SIZE")

            self.click(self.cut_label)
            self.timeout(2000)
            self.click(self.cut_emerald_option)
            self.timeout(2000)
            self.click(self.cut_apply_button)
            self.timeout(5000)
            result_count = self.inner_text(self.slp_page_records)
            print(f"SLP RECORDS [AFTER APPLYING MATERIAL + SIZE + CUT FILTERS]: {result_count.upper()}")
            self.screenshot.take_page_screenshot("SLP_FILTER_MATERIAL_SIZE_CUT")

        except:
            print("*****NOT ABLE TO APPLY FILTERS ON THE SLP..*****")

    def test_clear_filter_on_slp(self):
        try:
            self.timeout(2000)
            self.click(self.clear_all_filter)
            self.timeout(10000)
            result_count = self.inner_text(self.slp_page_records)
            print(f"SLP RECORDS [AFTER CLEAR FILTER]: {result_count.upper()}")
            self.screenshot.take_page_screenshot("SLP_CLEAR_ALL_FILTER")

        except:
            print("*****UNABLE TO CLEAR APPLIED FILTERS FROM THE SLP..*****")

    def test_open_contact_us_page_from_search(self):
        try:
            self.timeout(1000)
            self.click(self.search_icon)
            self.is_visible(self.search_keyword_input)
            self.timeout(2000)
            print("SEARCH MODAL IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("SEARCH_MODAL")
            self.timeout(2000)
            self.click(self.contact_us_link_search)
            self.timeout(2000)
            print("[SEARCH] USER IS REDIRECTED TO THE CONTACT US PAGE..")
            #self.screenshot.take_Page_screenshot("SEARCH_CONTACT_US")

        except:
            print("*****[SEARCH] NOT ABLE TO OPEN CONTACT US PAGE..*****")

    #Not working so not used as of now
    def test_open_faq_page_from_search(self):
        try:
            self.timeout(1000)
            self.click(self.search_icon)
            self.is_visible(self.search_keyword_input)
            self.timeout(2000)
            print("SEARCH MODAL IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("SEARCH_MODAL")
            self.timeout(2000)
            self.click(self.faq_link_search)
            self.timeout(2000)
            print("[SEARCH] USER IS REDIRECTED TO THE FAQ PAGE..")
            #self.screenshot.take_Page_screenshot("SEARCH_FAQ")

        except:
            print("*****[SEARCH] NOT ABLE TO OPEN FAQ PAGE..*****")
