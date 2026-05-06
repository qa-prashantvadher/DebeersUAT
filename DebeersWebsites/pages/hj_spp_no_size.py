from pages.base_page import BasePage
from pages.search_slp_pdp import SearchSKU
from pages.add_engraving import AddEngraving
from pages.take_screenshot import PageScreenshot
import logging

logger = logging.getLogger(__name__)


class HJ_SPP_No_Size(BasePage):

        SKU1 = "E103343"
        SKU1_ADD_TO_BAG_CTA = "//div[@class='primary-btn-wrap']/button[1]"
        SKU1_ADD_ENGRAVING_CTA = "//div[@class='secondary-btn-wrap']/button[1]"

        minicart_close_icon = "//*[@id='minicart']/button"

        def __init__(self, page):
            super().__init__(page)
            self.search = SearchSKU(page)
            self.engraving = AddEngraving(page)
            self.screenshot = PageScreenshot(page)


        def test_hj_spp_no_size_with_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU1)
                self.click(self.SKU1_ADD_ENGRAVING_CTA)
                self.timeout(2000)
                self.engraving.test_add_engraving()
                logger.info(f"[HJ SPP WITHOUT SIZE AND WITH ENGRAVING] {self.SKU1} IS ADDED TO THE CART..")
                self.screenshot.take_page_screenshot("HJ_SPP_NO_SIZE_ADDED_WITH_ENGRAVING")
                self.click(self.minicart_close_icon)
                #self.screenshot.take_Page_screenshot("HJ_SPP_NO_SIZE_ADD_WITH_ENGRAVING")
            except:
                logger.error(f"*****[HJ SPP WITHOUT SIZE AND WITH ENGRAVING] {self.SKU1} IS NOT ADDED TO THE CART..*****")

        def test_hj_spp_no_size_without_engraving(self):
            try:
                self.search.test_search_with_sku(self.SKU1)
                self.click(self.SKU1_ADD_TO_BAG_CTA)
                self.timeout(2000)
                logger.info(f"[HJ SPP WITHOUT SIZE AND WITHOUT ENGRAVING] {self.SKU1} IS ADDED TO THE CART..")
                self.screenshot.take_page_screenshot("HJ_SPP_NO_SIZE_ADDED_WITH_ENGRAVING")
                self.click(self.minicart_close_icon)
                #self.screenshot.take_Page_screenshot("HJ_SPP_NO_SIZE_ADD_BAG")
            except:
                logger.error(f"*****[HJ SPP WITHOUT SIZE AND WITHOUT ENGRAVING] {self.SKU1} IS NOT ADDED TO THE CART..*****")





