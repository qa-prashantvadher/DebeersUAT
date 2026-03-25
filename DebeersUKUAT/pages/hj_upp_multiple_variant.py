from pages.base_page import BasePage
from pages.search_slp_pdp import SearchSKU
from pages.add_engraving import AddEngraving
from pages.take_screenshot import PageScreenshot


class HJ_UPP_Multiple_Variant(BasePage):

        SKU1 = "R102134"
        SKU2 = "R102218"
        FIND_YOUR_DIAMOND_CTA = ":text('FIND YOUR DIAMOND')"
        # CTA details for the upp product with engraving support
        ADD_ENGRAVING_CTA = "//*[@id='find-your-ring']/div[3]/div[3]/ul/li[1]/figure/figcaption/div/div[4]/div/button[1]"
        ADD_TO_BAG_CTA = "//*[@id='find-your-ring']/div[3]/div[3]/ul/li[1]/figure/figcaption/div/div[4]/div/button[3]"
        ADDED_ENGRAVING_CTA = "//*[@id='find-your-ring']/div[3]/div[3]/ul/li[1]/figure/figcaption/div/div[4]/div/button[2]"

        # CTA details for the upp product without engraving support
        ADD_TO_BAG_WOE_CTA = "//*[@id='find-your-ring']/div[3]/div[3]/ul/li[1]/figure/figcaption/div/div[4]/div/button[1]"

        minicart_close_icon = '//*[@id="minicart"]/button'


        def __init__(self, page):
            super().__init__(page)
            self.search = SearchSKU(page)
            self.engraving = AddEngraving(page)
            self.screenshot = PageScreenshot(page)


        def test_hj_upp_multiple_variant_with_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU1)
                self.timeout(8000)
                self.click(self.FIND_YOUR_DIAMOND_CTA)
                #self.screenshot.take_Page_screenshot("HJ_UPP_MULTIPLE_LIST")
                self.click(self.ADD_ENGRAVING_CTA)
                self.engraving.test_back_button_engraving_screen()
                self.click(self.ADD_ENGRAVING_CTA)
                self.engraving.test_close_engraving_screen()
                self.click(self.ADD_ENGRAVING_CTA)
                self.engraving.test_add_engraving()
                print(f"[HJ] UPP MULTIPLE VARIANT [WITH ENGRAVING] {self.SKU1} IS ADDED TO THE CART..")
                self.screenshot.take_page_screenshot("HJ_UPP_MULTIPLE_ADDED_WITH_ENGRAVING")
                self.click(self.minicart_close_icon)
                self.click(self.ADDED_ENGRAVING_CTA)
                self.engraving.test_close_engraving_screen()
                self.click(self.ADDED_ENGRAVING_CTA)
                self.engraving.test_update_engraving()
                print(f"[HJ] UPP MULTIPLE VARIANT [WITH ENGRAVING] {self.SKU1} ENGRAVING TEXT IS UPDATED..")
                #self.screenshot.take_Page_screenshot("HJ_UPP_MULTIPLE_UPDATE_ENGRAVING")
            except:
                print(f"*****[HJ] UPP MULTIPLE VARIANT [WITH ENGRAVING] {self.SKU1} IS NOT ADDED TO THE CART..*****")

        def test_hj_upp_multiple_variant_without_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU2)
                self.timeout(8000)
                self.click(self.FIND_YOUR_DIAMOND_CTA)
                self.timeout(2000)
                #self.screenshot.take_Page_screenshot("HJ_UPP_MULTIPLE_LIST")
                self.click(self.ADD_TO_BAG_WOE_CTA)
                self.timeout(2000)
                print(f"[HJ] UPP MULTIPLE VARIANT [WITHOUT ENGRAVING] {self.SKU2} ENGRAVING TEXT IS ADDED..")
                self.screenshot.take_page_screenshot("HJ_UPP_MULTIPLE_ADDED_WITHOUT_ENGRAVING")
                self.click(self.minicart_close_icon)
                #self.screenshot.take_Page_screenshot("HJ_UPP_MULTIPLE_ADD_BAG")
            except:
                print(f"*****[HJ] UPP MULTIPLE VARIANT [WITHOUT ENGRAVING] {self.SKU2} IS NOT ADDED TO THE CART..*****")