from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot

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
            print("[CART] USER IS REDIRECTED TO THE CART PAGE..")
            self.screenshot.take_page_screenshot("CART_PAGE")
        except:
            print("*****[CART] USER IS NOT REDIRECTED TO THE CART PAGE..*****")

    def test_get_cart_products_count(self):
        try:
            count = self.get_text(self.added_product_count)
            count=int(count)
            print(f"[CART] TOTAL {count} PRODUCTS ARE AVAILABLE IN THE CART..")
            return count
        except:
            count=0
            return count

    def test_remove_product_from_cart(self):
        try:
            self.timeout(3000)
            self.click(self.remove_product_icon)
            self.timeout(7000)
            print("[CART] PRODUCT IS REMOVED FROM THE CART..")
            #self.screenshot.take_Page_screenshot("CART_REMOVE_PRODUCT")
        except:
            print("*****[CART] PRODUCT IS NOT REMOVED FROM THE CART PAGE..*****")

    def test_continue_to_checkout_from_cart(self):
        try:
            self.timeout(3000)
            self.screenshot.take_page_screenshot("CHECKOUT_CART_PAGE")
            self.click(self.continue_to_checkout_cta)
            self.timeout(5000)
            print("[CHECKOUT] USER IS REDIRECTED TO THE DELIVERY PAGE..")

        except:
            print("*****[CHECKOUT] USER IS NOT REDIRECTED TO THE DELIVERY PAGE..*****")
   