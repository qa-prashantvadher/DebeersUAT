from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot



class Checkout_Go_Back_From_Review(BasePage):
    delivery_tab_from_review = "//*[@id='checkout-step3']/ul/li[1]/button"
    payment_tab_from_review = "//*[@id='checkout-step3']/ul/li[2]/button"
    go_back_to_shopping_bag = "//*[@id='checkout-main']/div/div[1]/div[1]/div/a"
    

    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)

    def test_go_back_to_delivery_from_review_page(self):
        try:
            self.timeout(2000)
            self.click(self.delivery_tab_from_review)
            self.timeout(3000)
            print("[FROM REVIEW PAGE] USER IS REDIRECTED BACK TO THE DELIVERY PAGE..")
            self.screenshot.take_page_screenshot("GO_BACK_FROM_REVIEW_TO_DELIVERY")
        except:
            print("*****[FROM REVIEW PAGE] USER IS NOT REDIRECTED BACK TO THE DELIVERY PAGE..*****")


    def test_go_back_to_payment_from_review_page(self):
        try:
            self.timeout(2000)
            self.click(self.payment_tab_from_review)
            self.timeout(4000)
            print("[FROM REVIEW PAGE] USER IS REDIRECTED BACK TO THE PAYMENT PAGE..")
            self.screenshot.take_page_screenshot("GO_BACK_FROM_REVIEW_TO_PAYMENT")
        except:
            print("*****[FROM REVIEW PAGE] USER IS NOT REDIRECTED BACK TO THE PAYMENT PAGE..*****")

    def test_go_back_to_shopping_cart_from_review_page(self):
        try:
            self.timeout(2000)
            self.click(self.go_back_to_shopping_bag)
            self.timeout(5000)
            print("[FROM REVIEW PAGE] USER IS REDIRECTED BACK TO THE SHOPPING BAG PAGE..")
        except:
            print("*****[FROM REVIEW PAGE] USER IS NOT REDIRECTED BACK TO THE SHOPPING BAG PAGE..*****")
