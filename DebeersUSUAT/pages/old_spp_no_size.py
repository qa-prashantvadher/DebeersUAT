from pages.base_page import BasePage
from pages.search_slp_pdp import SearchSKU
from pages.add_engraving import AddEngraving
from pages.take_screenshot import PageScreenshot



class OLD_SPP_No_Size(BasePage):

        SKU1 = "A1021110000"
        ADD_TO_BAG_CTA = "//div[@class='primary-btn-wrap']/button[1]"
        ADD_ENGRAVING_CTA = "//div[@class='secondary-btn-wrap']/button[1]"

        minicart_close_icon = '//*[@id="minicart"]/button'

        def __init__(self, page):
            super().__init__(page)
            self.search = SearchSKU(page)
            self.engraving = AddEngraving(page)
            self.screenshot = PageScreenshot(page)

        def test_old_spp_no_size_with_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU1)
                self.click(self.ADD_ENGRAVING_CTA)
                self.engraving.test_add_engraving()
                print(f"[OLD] SPP WITHOUT SIZE [WITH ENGRAVING] {self.SKU1} IS ADDED TO THE CART..")
                self.screenshot.take_page_screenshot("OLD_SPP_NO_SIZE_ADDED_WITH_ENGRAVING")
                self.click(self.minicart_close_icon)
            except:
                print(f"*****[OLD] SPP WITHOUT SIZE [WITH ENGRAVING] {self.SKU1} IS NOT ADDED TO THE CART..*****")

        def test_old_spp_no_size_without_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU1)
                if self.is_visible(self.ADD_TO_BAG_CTA):
                    self.click(self.ADD_TO_BAG_CTA)
                    print(f"[OLD] SPP WITHOUT SIZE [WITHOUT ENGRAVING] {self.SKU1} IS ADDED TO THE CART..")
                    self.screenshot.take_page_screenshot("OLD_SPP_NO_SIZE_ADDED_WITHOUT_ENGRAVING")
                    self.click(self.minicart_close_icon)
                else:
                    print(f"*****[OLD] SPP WITHOUT SIZE [WITHOUT ENGRAVING] {self.SKU1} PRODUCT IS NOT BUYABLE..*****")
                    pass

            except:
                print(f"*****[OLD] SPP WITHOUT SIZE [WITHOUT ENGRAVING] {self.SKU1} IS NOT ADDED TO THE CART..*****")





