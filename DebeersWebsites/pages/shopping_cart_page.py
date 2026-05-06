from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
import logging

logger = logging.getLogger(__name__)

class Open_Shopping_Cart_Page(BasePage):

    added_product_count = "span.minicart-quantity.counter-block.not-empty"
    header_cart_icon = "//*[@id='headerShoppingBag']/div/a"
    remove_product_icon = "(//i[contains(@class,'dbicon-close')])[1]"
    continue_to_checkout_cta = "//a[@role='button']"

    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)

    def test_open_shopping_cart_page(self):
        try:
            # Goto Shopping Bag
            self.timeout(3000)
            self.click(self.header_cart_icon)
            self.timeout(2000)
            logger.info("[CART] USER IS REDIRECTED TO THE CART PAGE..")
            self.screenshot.take_page_screenshot("CART_PAGE")
        except:
            logger.error("*****[CART] USER IS NOT REDIRECTED TO THE CART PAGE..*****")

    def test_get_cart_products_count(self):
        try:
            count = self.get_text(self.added_product_count)
            count=int(count)
            logger.info(f"[CART] TOTAL PRODUCTS IN THE CART: {count}")
            return count
        except:
            count=0
            return count

    def test_remove_product_from_cart(self):
        try:
            self.timeout(3000)
            self.click(self.remove_product_icon)
            self.timeout(7000)
            logger.info("[CART] PRODUCT IS REMOVED FROM THE CART..")
            #self.screenshot.take_Page_screenshot("CART_REMOVE_PRODUCT")
        except:
            logger.error("*****[CART] PRODUCT IS NOT REMOVED FROM THE CART PAGE..*****")

    def test_continue_to_checkout_from_cart(self):
        try:
            self.timeout(3000)
            self.click(self.continue_to_checkout_cta)
            self.timeout(5000)
            logger.info("[CHECKOUT-CART] USER IS REDIRECTED TO THE DELIVERY PAGE..")
        except:
            logger.error("*****[CHECKOUT-CART] USER IS NOT REDIRECTED TO THE DELIVERY PAGE..*****")
   