from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
import logging

logger = logging.getLogger(__name__)


class Checkout_Go_Back_From_Payment(BasePage):
   
    delivery_tab_from_payment = "//*[@id='checkout-step2']/ul/li[1]/button"
    go_back_to_shopping_bag = "//*[@id='checkout-main']/div/div[1]/div[1]/div/a"


    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)

    def test_go_back_to_delivery_from_payment_page(self):
        try:
            self.timeout(1000)
            self.click(self.delivery_tab_from_payment)
            self.timeout(3000)
            logger.info("[FROM PAYMENT PAGE] USER IS REDIRECTED BACK TO THE DELIVERY PAGE..")
            self.screenshot.take_order_page_screenshot("GO_BACK_FROM_PAYMENT_TO_DELIVERY")
        except:
            logger.error("*****[FROM PAYMENT PAGE] USER IS NOT REDIRECTED BACK TO THE DELIVERY PAGE..*****")

    def test_go_back_to_shopping_cart_from_payment_page(self):
        try:
            self.timeout(1000)
            self.click(self.go_back_to_shopping_bag)
            self.timeout(5000)
            logger.info("[FROM REVIEW PAGE] USER IS REDIRECTED BACK TO THE SHOPPING BAG PAGE..")
            self.screenshot.take_order_page_screenshot("GO_BACK_FROM_PAYMENT_TO_CART")
        except:
            logger.error("*****[FROM REVIEW PAGE] USER IS NOT REDIRECTED BACK TO THE SHOPPING BAG PAGE..*****")