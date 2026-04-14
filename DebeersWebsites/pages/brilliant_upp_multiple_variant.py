from pages.base_page import BasePage
from pages.search_slp_pdp import SearchSKU
from pages.add_engraving import AddEngraving
from pages.take_screenshot import PageScreenshot

class BB_UPP_Multiple_Variant(BasePage):

        SKU1 = "R102260"
        SKU2 = "N102187"

        FIND_YOUR_DIAMOND_CTA = "//div[@class='primary-btn-wrap']/button[1]"

        # CTA details for the upp product with and without engraving support
        ADD_ENGRAVING_CTA = "(//li[contains(@class,'variation-tile') and not(contains(@class,'view-more'))]//button[contains(@class,'js-engraving-modal-button') and not(contains(@class,'d-none'))])[1]"
        ADDED_ENGRAVING_CTA = "(//li[contains(@class,'variation-tile') and not(contains(@class,'view-more'))]//button[contains(@class,'js-engraving-modal-button') and not(contains(@class,'d-none'))])[1]"
        ADD_TO_BAG_CTA = "(//li[contains(@class,'variation-tile')]//button[contains(@class,'js-btn-addToBag')])[1]"

        minicart_close_icon = "//*[@id='minicart']/button"


        def __init__(self, page):
            super().__init__(page)
            self.search = SearchSKU(page)
            self.engraving = AddEngraving(page)
            self.screenshot = PageScreenshot(page)

        def test_bb_upp_multiple_variant_with_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU1)
                self.timeout(8000)
                self.click(self.FIND_YOUR_DIAMOND_CTA)
                self.timeout(2000)
                self.click(self.ADD_ENGRAVING_CTA)
                self.engraving.test_back_button_engraving_screen()
                self.click(self.ADD_ENGRAVING_CTA)
                self.engraving.test_close_engraving_screen()
                self.click(self.ADD_ENGRAVING_CTA)
                self.engraving.test_add_engraving()
                self.screenshot.take_page_screenshot("BB_UPP_MULTIPLE_ADDED_WITH_ENGRAVING")
                print(f"[BB UPP MULTIPLE VARIANT WITH ENGRAVING] {self.SKU1} IS ADDED TO THE CART..")
                self.click(self.minicart_close_icon)
                self.click(self.ADDED_ENGRAVING_CTA)
                #self.screenshot.take_Page_screenshot("BB_UPP_MULTIPLE_UPDATE_ENGRAVING")
                self.engraving.test_close_engraving_screen()
                self.click(self.ADDED_ENGRAVING_CTA)
                self.engraving.test_update_engraving()
                print(f"[BB UPP MULTIPLE VARIANT WITH ENGRAVING] {self.SKU1} ENGRAVING TEXT IS UPDATED..")

            except:
                print(f"*****[BB UPP MULTIPLE VARIANT WITH ENGRAVING] {self.SKU1} IS NOT ADDED TO THE CART..*****")

        def test_bb_upp_multiple_variant_without_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU2)
                self.timeout(8000)
                self.click(self.FIND_YOUR_DIAMOND_CTA)
                self.timeout(2000)
                self.click(self.ADD_TO_BAG_CTA)
                self.timeout(2000)
                print(f"[BB UPP MULTIPLE VARIANT WITHOUT ENGRAVING] {self.SKU2} IS ADDED TO THE CART..")
                self.screenshot.take_page_screenshot("BB_UPP_MULTIPLE_ADDED_WITHOUT_ENGRAVING")
                self.click(self.minicart_close_icon)
            except:
                print(f"*****[BB UPP MULTIPLE VARIANT WITHOUT ENGRAVING] {self.SKU1} IS NOT ADDED TO THE CART..*****")