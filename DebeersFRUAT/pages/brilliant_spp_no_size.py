from pages.base_page import BasePage
from pages.search_slp_pdp import SearchSKU
from pages.add_engraving import AddEngraving
from pages.take_screenshot import PageScreenshot



class BB_SPP_No_Size(BasePage):

        SKU1 = "E103376"
        SKU1_CTA = "button:has-text('ADD ENGRAVING')"
        SKU2 = "E102158"
        SKU2_CTA = "button:has-text('ADD TO BAG')"
        minicart_close_icon = "//*[@id='minicart']/button"

        def __init__(self, page):
            super().__init__(page)
            self.search = SearchSKU(page)
            self.engraving = AddEngraving(page)
            self.screenshot = PageScreenshot(page)

        def test_bb_spp_no_size_with_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU1)
                self.click(self.SKU1_CTA)
                self.engraving.test_add_engraving()
                print(f"[BB] SPP WITHOUT SIZE [WITH ENGRAVING] {self.SKU1} IS ADDED TO THE CART..")
                self.screenshot.take_page_screenshot("BB_SPP_NO_SIZE_ADDED_WITH_ENGRAVING")
                self.click(self.minicart_close_icon)
            except:
                print(f"*****[BB] SPP WITHOUT SIZE [WITH ENGRAVING] {self.SKU1} IS NOT ADDED TO THE CART..*****")

        def test_bb_spp_no_size_without_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU2)
                self.click(self.SKU2_CTA)
                self.timeout(2000)
                print(f'[BB] SPP WITHOUT SIZE [WITHOUT ENGRAVING] {self.SKU2} IS ADDED TO THE CART..')
                self.screenshot.take_page_screenshot("BB_SPP_NO_SIZE_ADDED_WITHOUT_ENGRAVING")
                self.click(self.minicart_close_icon)
                #self.screenshot.take_Page_screenshot("BB_SPP_NO_SIZE_ADD_BAG")
            except:
                print(f'*****[BB] SPP WITHOUT SIZE [WITHOUT ENGRAVING] {self.SKU2} IS NOT ADDED TO THE CART..*****')





