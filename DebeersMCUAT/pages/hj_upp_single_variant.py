from pages.base_page import BasePage
from pages.search_slp_pdp import SearchSKU
from pages.add_engraving import AddEngraving
from pages.take_screenshot import PageScreenshot

class HJ_UPP_Single_Variant(BasePage):

        SKU1 = "R102133"
        SKU2 = "N102152"

        ADD_TO_BAG_CTA = "//div[@class='primary-btn-wrap']/div/button[1]"
        ADD_ENGRAVING_CTA = "//div[@class='secondary-btn-wrap']/button[1]"
        ADDED_ENGRAVING_CTA = "//div[@class='secondary-btn-wrap']/button[2]"

        enquire_hj_master_level = "//div[contains(@class,'primary-btn-wrap')]//a[contains(@class,'btn-enquire-online') and not(contains(@class,'d-none'))]"
        minicart_close_icon = '//*[@id="minicart"]/button'

        def __init__(self, page):
            super().__init__(page)
            self.search = SearchSKU(page)
            self.engraving = AddEngraving(page)
            self.screenshot = PageScreenshot(page)


        def test_hj_upp_single_variant_with_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU1)
                self.timeout(3000)
                if self.is_visible(self.ADD_TO_BAG_CTA):
                    #self.screenshot.take_Page_screenshot("HJ_UPP_SINGLE")
                    self.click(self.ADD_ENGRAVING_CTA)
                    self.engraving.test_back_button_engraving_screen()
                    self.click(self.ADD_ENGRAVING_CTA)
                    self.engraving.test_close_engraving_screen()
                    self.click(self.ADD_ENGRAVING_CTA)
                    self.engraving.test_add_engraving()
                    print(f"[HJ] UPP SINGLE VARIANT [WITH ENGRAVING] {self.SKU1} IS ADDED TO THE CART..")
                    self.screenshot.take_page_screenshot("HJ_UPP_SINGLE_ADDED_WITH_ENGRAVING")
                    self.click(self.minicart_close_icon)
                    #self.screenshot.take_Page_screenshot("HJ_UPP_SINGLE_ADD_ENGRAVING")
                    self.click(self.ADDED_ENGRAVING_CTA)
                    self.engraving.test_close_engraving_screen()
                    self.click(self.ADDED_ENGRAVING_CTA)
                    self.engraving.test_update_engraving()
                    print(f"[HJ] UPP SINGLE VARIANT [WITH ENGRAVING] {self.SKU1} ENGRAVING TEXT IS UPDATED..")
                else:
                    print(f"*****[HJ] UPP SINGLE VARIANT [WITH ENGRAVING] {self.SKU1} PRODUCT IS NOT BUYABLE..*****")
                    pass
            except:
                print(f"*****[HJ] UPP SINGLE VARIANT [WITH ENGRAVING] {self.SKU1} IS NOT ADDED TO THE CART..*****")

        def test_hj_upp_single_variant_without_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU2)
                self.timeout(3000)
                #self.screenshot.take_Page_screenshot("HJ_UPP_SINGLE")
                if self.is_visible(self.ADD_TO_BAG_CTA):
                    self.click(self.ADD_TO_BAG_CTA)
                    self.timeout(2000)
                    print(f"[HJ] UPP SINGLE VARIANT [WITHOUT ENGRAVING] {self.SKU2} ENGRAVING TEXT IS UPDATED..")
                    self.screenshot.take_page_screenshot("HJ_UPP_SINGLE_ADDED_WITH_ENGRAVING")
                    self.click(self.minicart_close_icon)
                    #self.screenshot.take_Page_screenshot("HJ_UPP_SINGLE_ADD_BAG")
                else:
                    print(f"*****[HJ] UPP SINGLE VARIANT [WITHOUT ENGRAVING] {self.SKU2} PRODUCT IS NOT BUYABLE..*****")
                    pass
            except:
                print(f"*****[HJ] UPP SINGLE VARIANT [WITHOUT ENGRAVING] {self.SKU2} IS NOT ADDED TO THE CART..*****")



