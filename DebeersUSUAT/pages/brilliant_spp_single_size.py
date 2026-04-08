from pages.base_page import BasePage
from pages.search_slp_pdp import SearchSKU
from pages.add_engraving import AddEngraving
from pages.take_screenshot import PageScreenshot


class BB_SPP_Single_Size(BasePage):

        SKU1 = "N103491"
        SKU2 = "N103116"
        SELECT_SIZE_CTA = "//div[contains(@class,'primary-btn-wrap')]//button[contains(@class,'js-pdp-variation-size__button') and not(contains(@class,'d-none'))]"
        ADD_TO_BAG_CTA = "div[id='pdpSizes'] button[type='submit']"
        ADD_ENGRAVING_CTA = "//div[contains(@class,'pdp-variation-size__buttons')]//button[contains(@class,'js-select-engraving-btn') and not(contains(@class,'d-none'))]"

        minicart_close_icon = "//*[@id='minicart']/button"

        def __init__(self, page):
            super().__init__(page)
            self.search = SearchSKU(page)
            self.engraving = AddEngraving(page)
            self.screenshot = PageScreenshot(page)

        def test_bb_spp_single_size_with_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU1)
                self.click(self.SELECT_SIZE_CTA)
                self.timeout(3000)
                self.click(self.ADD_ENGRAVING_CTA)
                self.engraving.test_add_engraving()
                print(f"[BB SPP SINGLE SIZE WITH ENGRAVING] {self.SKU1} IS ADDED TO THE CART..")
                self.screenshot.take_page_screenshot("BB_SPP_SINGLE_ADDED_WITH_ENGRAVING")
                self.click(self.minicart_close_icon)
            except:
                print(f"*****[BB SPP SINGLE SIZE WITH ENGRAVING] {self.SKU1} IS NOT ADDED TO THE CART..*****")

        def test_bb_spp_single_size_without_engraving(self):
           try:
                self.search.test_search_with_sku(self.SKU2)
                self.click(self.SELECT_SIZE_CTA)
                self.timeout(3000)
                self.click(self.ADD_TO_BAG_CTA)
                print(f"[BB SPP SINGLE SIZE WITHOUT ENGRAVING] {self.SKU2} IS ADDED TO THE CART..")
                self.screenshot.take_page_screenshot("BB_SPP_SINGLE_ADDED_WITHOUT_ENGRAVING")
                self.click(self.minicart_close_icon)
           except:
                print(f"*****[BB SPP SINGLE SIZE WITHOUT ENGRAVING] {self.SKU2} IS NOT ADDED TO THE CART..*****")