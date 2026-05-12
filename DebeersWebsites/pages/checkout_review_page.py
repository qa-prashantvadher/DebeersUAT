from pages.base_page import BasePage
import os
from pages.take_screenshot import PageScreenshot
from pages.shopping_cart_page import Open_Shopping_Cart_Page
from dotenv import load_dotenv
import logging

load_dotenv(override=True)
logger = logging.getLogger(__name__)

class Checkout_Review(BasePage):
    ENV = os.getenv("ENVIRONMENT").upper()
    URL = os.getenv("BASE_URL")
    COUNTRY = os.getenv("LOCALE").upper()

    if COUNTRY == "US":
        delivery_date_premium_review_page = "//span[@class='time estimatedArrivalTime US-SHIPPING-01']"
        delivery_date_collect_review_page = "//span[@class='time estimatedArrivalTime US-SHIPPING-02']"
    elif COUNTRY == "UK":
        delivery_date_premium_review_page = "//span[@class='time estimatedArrivalTime GB-SHIPPING-01']"
        delivery_date_collect_review_page = "//span[@class='time estimatedArrivalTime GB-SHIPPING-02']"
    elif COUNTRY == "FR":
        delivery_date_premium_review_page = "//span[@class='time estimatedArrivalTime FR-SHIPPING-01']"
        delivery_date_collect_review_page = "//span[@class='time estimatedArrivalTime FR-SHIPPING-02']"
    elif COUNTRY == "HK":
        delivery_date_premium_review_page = "//span[@class='time estimatedArrivalTime HK-SHIPPING-01']"
        delivery_date_collect_review_page = "//span[@class='time estimatedArrivalTime HK-SHIPPING-02']"
    elif COUNTRY == "TW":
        delivery_date_premium_review_page = "//span[@class='time estimatedArrivalTime TW-SHIPPING-01']"
        delivery_date_collect_review_page = "//span[@class='time estimatedArrivalTime TW-SHIPPING-02']"
    elif COUNTRY == "MO":
        delivery_date_premium_review_page = "//span[@class='time estimatedArrivalTime MO-SHIPPING-01']"
        delivery_date_collect_review_page = "//span[@class='time estimatedArrivalTime MO-SHIPPING-02']"
    place_order_cta = "//button[@class='btn btn-primary place-order']"
    payment_tab = "//button[@data-stage='payment']"
    order_number_confirmation_page = "//span[@class='order-number']"
    shipping_method = ".shipping-method-title"
    delivery_address_summary = "//div[@class='summary-details shipping']"
    billing_address_summary = "//div[@class='summary-details billing']"
    payment_image = "xpath=//div[@class='payment-details']//img"

    subtotal = "(//div[@class='cart-summary__price'])[1]"
    tax_value = "#taxValue"
    total_including_tax = "#totalIncludingValue"


    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)
        self.shopping_bag = Open_Shopping_Cart_Page(page)

    def test_page_refresh(self):
        try:
            self.timeout(2000)
            self.page.reload()
            self.timeout(3000)
            logger.info("[CHECKOUT-REVIEW] REVIEW PAGE IS REFRESHED SUCCESSFULLY..")
        except:
            logger.error("*****[CHECKOUT-REVIEW] UNABLE TO REFRESH PAGE..*****")

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

            payment_method_alt_text = self.page.locator(self.payment_image).get_attribute("alt")
            logger.info(f"##### [{self.COUNTRY}-{self.ENV}][ORDER REVIEW] PAYMENT METHOD: {payment_method_alt_text.upper()}")

            subtotal = self.get_text(self.subtotal).strip()
            calculated_tax = self.get_text(self.tax_value).strip()
            total_including_tax = self.get_text(self.total_including_tax).strip()

            logger.info(f"##### [{self.COUNTRY}-{self.ENV}][ORDER REVIEW] SUBTOTAL: {subtotal.upper()}")
            if self.COUNTRY == "US":
                logger.info(f"##### [{self.COUNTRY}-{self.ENV}][ORDER REVIEW] TAX (EXCLUSIVE): {calculated_tax.upper()}")
            else:
                logger.info(f"##### [{self.COUNTRY}-{self.ENV}][ORDER REVIEW] TAX (INCLUSIVE): {calculated_tax.upper()}")
            logger.info(f"##### [{self.COUNTRY}-{self.ENV}][ORDER REVIEW] GRAND TOTAL (INCLUDING TAX): {total_including_tax.upper()}")

            shipping_method_text = self.get_text(self.shipping_method).strip()
            logger.info(f"##### [{self.COUNTRY}-{self.ENV}][ORDER REVIEW] SHIPPING METHOD: {shipping_method_text.upper()}")

            delivery_address_summary_text = self.get_text(self.delivery_address_summary)
            clean_delivery_address_summary_text = "\n".join(line.strip() for line in delivery_address_summary_text.splitlines() if line.strip())
            logger.info(f"##### [{self.COUNTRY}-{self.ENV}][ORDER REVIEW] DELIVERY ADDRESS: \n{clean_delivery_address_summary_text.upper()}")


            billing_address_summary_text = self.get_text(self.billing_address_summary)
            clean_billing_address_summary_text = "\n".join(line.strip() for line in billing_address_summary_text.splitlines() if line.strip())
            logger.info(f"##### [{self.COUNTRY}-{self.ENV}][ORDER REVIEW] BILLING ADDRESS: \n{clean_billing_address_summary_text.upper()}")

            if self.ENV in ["UAT", "QA"]:
                self.click(self.place_order_cta)
                self.timeout(10000)
                order_number = self.get_text(self.order_number_confirmation_page).split()[-1]
                logger.info(f"##### [{self.COUNTRY}-{self.ENV}][ORDER CONFIRMATION] ORDER NUMBER: {order_number} AND DELIVERY DATE: {delivery_date.upper()}")
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
            logger.error(f"*****[CHECKOUT-CONFIRMATION] ORDER IS NOT CREATED.. USER IS NAVIGATED TO: {self.URL.upper()}*****")
