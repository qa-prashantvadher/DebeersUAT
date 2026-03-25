from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot

class Checkout_Review(BasePage):

    place_order_cta = "//button[@class='btn btn-primary place-order']"
    payment_tab = "//button[@data-stage='payment']"
    delivery_date_premium_review_page = "//span[@class='time estimatedArrivalTime GB-SHIPPING-01']"
    delivery_date_collect_review_page = "//span[@class='time estimatedArrivalTime GB-SHIPPING-02']"
    order_number_confirmation_page = "//span[@class='order-number']"

    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)


    def test_place_an_order_from_order_review_page(self):
        try:
            self.timeout(5000)
            if self.is_visible(self.delivery_date_premium_review_page):
                delivery_date = self.get_text(self.delivery_date_premium_review_page).strip()
            elif self.is_visible(self.delivery_date_collect_review_page):
                delivery_date = self.get_text(self.delivery_date_collect_review_page).strip()
            else:
                delivery_date = None

            self.timeout(2000)
            self.screenshot.take_page_screenshot(f"ORDER_REVIEW")
            self.click(self.place_order_cta)
            self.timeout(10000)
            order_number = self.get_text(self.order_number_confirmation_page).split()[-1]
            print(f"[ORDER CREATED] ORDER NUMBER: {order_number} AND DELIVERY DATE: {delivery_date}..")
            self.screenshot.take_order_page_screenshot(f"ORDER#_{order_number}_{delivery_date}")


        except:
            print("*****[CHECKOUT-CONFIRMATION] ORDER IS NOT CREATED..*****")
