from pages.base_page import BasePage
from pages.search_slp_pdp import SearchSKU
from pages.take_screenshot import PageScreenshot


class UPP_Multiple_Variant_Filter(BasePage):
    SKU1 = "R102127"
    SKU1_FIND_YOUR_DIAMOND_CTA = "//div[@class='primary-btn-wrap']/button[1]"

    SKU2 = "R102205"
    SKU2_FIND_YOUR_DIAMOND_CTA = "//div[@class='primary-btn-wrap']/button[1]"

    ring_size_dropdown = "//*[@id='size-refinement']"
    ring_size_53 = "53"
    ring_size_52 = "52"
    clarity_si1 = "button[data-attribute-value='SI1']"
    clarity_vs2 = "button[data-attribute-value='VS2']"
    colour_g = "button[data-attribute-value='whiteG']"
    #min_carat_slider = "a[data-target='minCarat']"
    #max_carat_slider = "a[data-target='minCarat']"

    filter_result_count = "//div[@class='text-center result-count-status']//span[1]"

    clear_all_filter = "button[data-attribute-value='clearAll']"


    def __init__(self, page):
        super().__init__(page)
        self.search = SearchSKU(page)
        self.screenshot = PageScreenshot(page)


    def test_hj_upp_variant_filter(self):
        try:
            self.search.test_search_with_sku(self.SKU1)
            self.timeout(8000)
            self.click(self.SKU1_FIND_YOUR_DIAMOND_CTA)
            result_count = self.inner_text(self.filter_result_count)
            self.screenshot.take_page_screenshot("HJ_VARIANT_FILTER")
            print(f"[HJ UPP MULTIPLE VARIANT] RECORDS WITHOUT FILTER: {result_count.upper()}")
            self.select_value(self.ring_size_dropdown, self.ring_size_53)
            self.timeout(8000)
            self.screenshot.take_page_screenshot("HJ_VARIANT_FILTER_SIZE")
            result_count = self.inner_text(self.filter_result_count)
            print(f"[HJ UPP MULTIPLE VARIANT] RECORDS AFTER SIZE FILTER: {result_count.upper()}")
            self.click(self.clarity_si1)
            self.timeout(8000)
            self.screenshot.take_page_screenshot("HJ_VARIANT_FILTER_SIZE_CLARITY")
            result_count = self.inner_text(self.filter_result_count)
            print(f"[HJ UPP MULTIPLE VARIANT] RECORDS AFTER SIZE + CLARITY FILTERS: {result_count.upper()}")
            min_price_slider = self.page.locator("a[data-target='priceMin']")
            min_price_slider.focus()
            min_price_slider.press("ArrowRight")
            self.timeout(8000)
            self.screenshot.take_page_screenshot("HJ_VARIANT_FILTER_SIZE_CLARITY_PRICE")
            result_count = self.inner_text(self.filter_result_count)
            print(f"[HJ UPP MULTIPLE VARIANT] RECORDS AFTER SIZE + CLARITY + PRICE FILTERS: {result_count.upper()}")
        except:
            print(f"*****[HJ UPP MULTIPLE VARIANT] FILTER IS NOT APPLIED IN THE VARIANT SECTION [UPP SKU: {self.SKU1}]..*****")

    def test_bb_upp_variant_filter(self):
        try:
            self.search.test_search_with_sku(self.SKU2)
            self.timeout(8000)
            self.click(self.SKU2_FIND_YOUR_DIAMOND_CTA)
            self.screenshot.take_page_screenshot("BB_VARIANT_FILTER")
            result_count = self.inner_text(self.filter_result_count)
            print(f"[BB UPP MULTIPLE VARIANT] RECORDS WITHOUT FILTER: {result_count.upper()}")
            self.select_value(self.ring_size_dropdown, self.ring_size_52)
            self.timeout(8000)
            self.screenshot.take_page_screenshot("BB_VARIANT_FILTER_SIZE")
            result_count = self.inner_text(self.filter_result_count)
            print(f"[BB UPP MULTIPLE VARIANT] RECORDS AFTER SIZE FILTER: {result_count.upper()}")
            self.click(self.colour_g)
            self.timeout(8000)
            self.screenshot.take_page_screenshot("BB_VARIANT_FILTER_SIZE_COLOUR")
            result_count = self.inner_text(self.filter_result_count)
            print(f"[BB UPP MULTIPLE VARIANT] RECORDS AFTER SIZE + COLOUR FILTERS: {result_count.upper()}")
            self.click(self.clarity_vs2)
            self.timeout(8000)
            self.screenshot.take_page_screenshot("BB_VARIANT_FILTER_SIZE_COLOUR_CLARITY")
            result_count = self.inner_text(self.filter_result_count)
            print(f"[BB UPP MULTIPLE VARIANT] RECORDS AFTER SIZE + COLOUR + CLARITY FILTERS: {result_count.upper()}")
            min_carat_slider = self.page.locator("a[data-target='minCarat']")
            min_carat_slider.focus()
            min_carat_slider.press("ArrowRight")
            self.timeout(8000)
            self.screenshot.take_page_screenshot("BB_VARIANT_FILTER_SIZE_COLOUR_CLARITY_CARAT")
            result_count = self.inner_text(self.filter_result_count)
            print(f"[BB UPP MULTIPLE VARIANT] RECORDS AFTER SIZE + COLOUR + CLARITY + CARAT FILTERS: {result_count.upper()}")
            min_price_slider = self.page.locator("a[data-target='priceMin']")
            min_price_slider.focus()
            min_price_slider.press("ArrowRight")
            self.timeout(8000)
            self.screenshot.take_page_screenshot("BB_VARIANT_FILTER_SIZE_COLOUR_CLARITY_CARAT_PRICE")
            result_count = self.inner_text(self.filter_result_count)
            print(f"[BB UPP MULTIPLE VARIANT] RECORDS AFTER SIZE + COLOUR + CLARITY + CARAT + PRICE FILTERS: {result_count.upper()}")
        except:
            print(f"*****[BB UPP MULTIPLE VARIANT] FILTER IS NOT APPLIED IN THE VARIANT SECTION [UPP SKU: {self.SKU2}]..*****")

    def test_bb_clear_all_filters(self):
        try:
            self.timeout(2000)
            self.click(self.clear_all_filter)
            self.timeout(10000)
            result_count = self.inner_text(self.filter_result_count)
            self.screenshot.take_page_screenshot("BB_VARIANT_CLEAR_ALL_FILTER")
            print(f"[BB UPP MULTIPLE VARIANT] RECORDS AFTER CLEAR ALL FILTER: {result_count.upper()}")
        except:
            print("*****[BB UPP MULTIPLE VARIANT] NOT ABLE TO PERFORM CLEAR ALL ACTION..*****")

    def test_hj_clear_all_filters(self):
        try:
            self.timeout(2000)
            self.click(self.clear_all_filter)
            self.timeout(10000)
            self.screenshot.take_page_screenshot("HJ_VARIANT_CLEAR_ALL_FILTER")
            result_count = self.inner_text(self.filter_result_count)
            print(f"[HJ UPP MULTIPLE VARIANT] RECORDS AFTER CLEAR ALL FILTER: {result_count.upper()}")
        except:
            print("*****[HJ UPP MULTIPLE VARIANT] NOT ABLE TO PERFORM CLEAR ALL ACTION..*****")
