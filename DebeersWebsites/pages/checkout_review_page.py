from pages.base_page import BasePage
import os
from pages.take_screenshot import PageScreenshot
from pages.shopping_cart_page import Open_Shopping_Cart_Page
from dotenv import load_dotenv
load_dotenv(override=True)

class Checkout_Review(BasePage):
    ENV = os.getenv("ENVIRONMENT")
    URL = os.getenv('BASE_URL')
    COUNTRY = os.getenv('LOCALE')

    if COUNTRY == "US":
        delivery_date_premium_review_page = "//span[@class='time estimatedArrivalTime US-SHIPPING-01']"
        delivery_date_collect_review_page = "//span[@class='time estimatedArrivalTime US-SHIPPING-02']"
    elif COUNTRY == "UK":
        delivery_date_premium_review_page = "//span[@class='time estimatedArrivalTime GB-SHIPPING-01']"
        delivery_date_collect_review_page = "//span[@class='time estimatedArrivalTime GB-SHIPPING-02']"
    elif COUNTRY == "FR":
        delivery_date_premium_review_page = "//span[@class='time estimatedArrivalTime FR-SHIPPING-01']"
        delivery_date_collect_review_page = "//span[@class='time estimatedArrivalTime FR-SHIPPING-02']"
    place_order_cta = "//button[@class='btn btn-primary place-order']"
    payment_tab = "//button[@data-stage='payment']"
    order_number_confirmation_page = "//span[@class='order-number']"

    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)
        self.shopping_bag = Open_Shopping_Cart_Page(page)

    def test_page_refresh(self):
        try:
            self.timeout(2000)
            self.page.reload()
            self.timeout(3000)
            print("[CHECKOUT-REVIEW] REVIEW PAGE REFRESHED SUCCESSFULLY..")
        except:
            print("*****[CHECKOUT-REVIEW] UNABLE TO REFRESH PAGE..*****")

    def test_place_an_order_from_order_review_page(self):
        try:
            self.timeout(5000)
            if self.is_visible(self.delivery_date_premium_review_page):
                delivery_date = self.get_text(self.delivery_date_premium_review_page).strip()
            elif self.is_visible(self.delivery_date_collect_review_page):
                delivery_date = self.get_text(self.delivery_date_collect_review_page).strip()
            else:
                delivery_date = None

            self.timeout(1000)
            self.screenshot.take_order_page_screenshot(f"[{self.COUNTRY}-{self.ENV}]_ORDER_REVIEW")
            if self.ENV in ["UAT", "QA"]:
                self.click(self.place_order_cta)
                self.timeout(10000)
                order_number = self.get_text(self.order_number_confirmation_page).split()[-1]
                print(f"[{self.COUNTRY}-{self.ENV}][ORDER CONFIRMATION] ORDER NUMBER: {order_number} AND DELIVERY DATE: {delivery_date.upper()}..")
                self.screenshot.take_order_page_screenshot(f"[{self.COUNTRY}-{self.ENV}]_ORDER#_{order_number}_{delivery_date.upper()}")
            else:
                # REMOVE ALL PRODUCTS FROM THE CART
                self.navigate(self.URL)
                self.timeout(5000)
                self.shopping_bag.test_open_shopping_cart_page()
                cart_products = self.shopping_bag.test_get_cart_products_count()
                if cart_products > 0:
                    for cart_products in range(1, cart_products + 1):
                        self.shopping_bag.test_remove_product_from_cart()
        except:
            self.navigate(self.URL)
            print(f"*****[CHECKOUT-CONFIRMATION] ORDER IS NOT CREATED.. USER IS NAVIGATED TO: {self.URL.upper()}*****")
