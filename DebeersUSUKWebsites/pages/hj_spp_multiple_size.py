from pages.base_page import BasePage
from pages.search_slp_pdp import SearchSKU
from pages.add_engraving import AddEngraving
from pages.take_screenshot import PageScreenshot

class HJ_SPP_Multiple_Size(BasePage):

        SKU1 = "R103140"
        SKU2 = "R103731"
        SELECT_SIZE_CTA = "//div[contains(@class,'primary-btn-wrap')]//button[contains(@class,'js-pdp-variation-size__button') and not(contains(@class,'d-none'))]"
        SIZE_OPTION = "button:has-text('51')"

        ADD_TO_BAG_CTA = "div[id='pdpSizes'] button[type='submit']"
        ADD_ENGRAVING_CTA = "//div[contains(@class,'pdp-variation-size__buttons')]//button[contains(@class,'js-select-engraving-btn') and not(contains(@class,'d-none'))]"

        minicart_close_icon = "//*[@id='minicart']/button"


        def __init__(self, page):
            super().__init__(page)
            self.search = SearchSKU(page)
            self.engraving = AddEngraving(page)
            self.screenshot = PageScreenshot(page)

        def test_hj_spp_multiple_size_with_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU1)
                self.click(self.SELECT_SIZE_CTA)
                self.timeout(3000)
                self.click(self.SIZE_OPTION)
                self.timeout(2000)
                #self.screenshot.take_Page_screenshot("HJ_SPP_MULTIPLE_SELECT_SIZE")
                self.click(self.ADD_ENGRAVING_CTA)
                #self.screenshot.take_Page_screenshot("HJ_SPP_MULTIPLE_ADD_ENGRAVING")
                self.engraving.test_add_engraving()
                print(f"[HJ SPP MULTIPLE SIZE WITH ENGRAVING] {self.SKU1} IS ADDED TO THE CART..")
                self.screenshot.take_page_screenshot("HJ_SPP_MULTIPLE_ADDED_WITH_ENGRAVING")
                self.click(self.minicart_close_icon)
                #self.screenshot.take_Page_screenshot("HJ_SPP_MULTIPLE_ADD_WITH_ENGRAVING")
            except:
                 print(f"*****[HJ SPP MULTIPLE SIZE WITH ENGRAVING] {self.SKU1} IS NOT ADDED TO THE CART..*****")

        def test_hj_spp_multiple_size_without_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU2)
                self.click(self.SELECT_SIZE_CTA)
                self.timeout(3000)
                self.click(self.SIZE_OPTION)
                self.timeout(2000)
                #self.screenshot.take_Page_screenshot("HJ_SPP_MULTIPLE_SELECT_SIZE")
                self.click(self.ADD_TO_BAG_CTA)
                print(f"[HJ SPP MULTIPLE SIZE WITHOUT ENGRAVING] {self.SKU2} IS ADDED TO THE CART..")
                self.screenshot.take_page_screenshot("HJ_SPP_MULTIPLE_ADDED_WITHOUT_ENGRAVING")
                self.click(self.minicart_close_icon)
                #self.screenshot.take_Page_screenshot("HJ_SPP_MULTIPLE_ADD_BAG")
            except:
                print(f"*****[HJ SPP MULTIPLE SIZE WITHOUT ENGRAVING] {self.SKU2} IS NOT ADDED TO THE CART..*****")