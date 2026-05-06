from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
import logging

logger = logging.getLogger(__name__)

class AddRemoveWishlist(BasePage):

    wishlist_icon_header = "//*[@id='headerWishlist']/a"
    plp_slp_wishlist_icon_R102205 = "button[data-pid='R102205'] i.product-tile__wishlist-icon"
    guest_my_account_wishlist_remove_R102205 = "//button[contains(@class,'wish-list__remove-btn')]//i"
    pdp_wishlist_icon_R102205 = "//*[@id='image-1']/button[2]/i"


    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)

    def test_add_wishlist_plp_slp(self):
        try:
            self.click(self.plp_slp_wishlist_icon_R102205)
            self.timeout(2000)
            logger.info("[PLP/SLP] PRODUCT IS ADDED TO THE WISHLIST..")
            #self.screenshot.take_Page_screenshot("PLP_WISHLIST_ADD")
        except:
            logger.error("*****[PLP/SLP] NOT ABLE TO ADD PRODUCT TO THE WISHLIST..*****")

    def test_add_wishlist_pdp(self):
        try:
            self.click(self.pdp_wishlist_icon_R102205)
            self.timeout(2000)
            logger.info("[PDP] PRODUCT IS ADDED TO THE WISHLIST..")
            #self.screenshot.take_Page_screenshot("PDP_WISHLIST_ADD")
        except:
            logger.error("*****[PDP] NOT ABLE TO ADD PRODUCT TO THE WISHLIST..*****")

    def test_remove_wishlist_plp_slp(self):
        try:
            self.click(self.plp_slp_wishlist_icon_R102205)
            self.timeout(2000)
            logger.info("[PLP/SLP] PRODUCT IS REMOVED FROM THE WISHLIST..")
            #self.screenshot.take_Page_screenshot("PLP_WISHLIST_REMOVE")
        except:
            logger.error("*****[PLP/SLP] NOT ABLE TO REMOVE PRODUCT FROM THE WISHLIST..*****")

    def test_remove_wishlist_pdp(self):
        try:
            self.click(self.pdp_wishlist_icon_R102205)
            self.timeout(2000)
            logger.info("[PDP] PRODUCT IS REMOVED FROM THE WISHLIST..")
            #self.screenshot.take_Page_screenshot("PDP_WISHLIST_REMOVE")
        except:
            logger.error("*****[PDP] NOT ABLE TO REMOVE PRODUCT FROM THE WISHLIST..*****")

    def test_remove_wishlist_from_my_account_wishlist_page(self):
        try:
            self.click(self.guest_my_account_wishlist_remove_R102205)
            self.timeout(4000)
            logger.info("[MY ACCOUNT-WISHLIST] PRODUCT IS REMOVED FROM THE WISHLIST..")
            #self.screenshot.take_Page_screenshot("MY_ACCOUNT_WISHLIST_REMOVE")
        except:
            logger.error("*****[MY ACCOUNT-WISHLIST] NOT ABLE TO REMOVE PRODUCT FROM THE WISHLIST..*****")
