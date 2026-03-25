from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot

class Checkout_Payment(BasePage):

    continue_to_review_cta = "//button[@class='btn btn-primary mx-auto submit-payment']"

    #Payment Methods
    payment_by_cards = "//input[@id='rb_scheme']"
    payment_by_paypal = "//input[@id='rb_paypal']"

    #Cards
    card_number_iframe = "iframe[title='Iframe for card number']"
    expiry_date_iframe = "iframe[title='Iframe for expiry date']"
    cvv_iframe = "iframe[title='Iframe for security code']"
    card_holder_name_input = "input[name='holderName']" #not inside iframe

    amex_card_number_text = "370000000000002"
    amex_expiry_date_text = "03/30"
    amex_cvv_text = "7373"

    union_pay_card_number_text = "8171999927660000"
    union_pay_expiry_date_text = "10/30"
    union_pay_cvv_text = "737"

    discover_card_number_text = "6445644564456445"
    discover_expiry_date_text = "03/30"
    discover_cvv_text = "737"

    jcb_card_number_text = "3569990010095841"
    jcb_expiry_date_text = "03/30"
    jcb_cvv_text = "737"

    mc_card_number_text = "5555555555554444"
    mc_expiry_date_text = "03/30"
    mc_cvv_text = "737"

    visa_card_number_text = "4444333322221111"
    visa_expiry_date_text = "03/30"
    visa_cvv_text = "737"

    dankort_card_number_text = "4444333322221111"
    dankort_expiry_date_text = "03/30"
    dankort_cvv_text = "737"


    card_holder_name_text = "Prashant Vadher"

    #Same address checkbox
    use_delivery_as_billing_input = "//input[@id='isShippingBillingAddress']"

    #Premium Delivery > Shipping Address Info
    billing_title_dropdown = "//*[@id='billingCustomerTitle']"
    billing_title_value = "mr."
    billing_first_name_input = "//input[@id='billingFirstName']"
    billing_last_name_input = "//input[@id='billingLastName']"
    billing_phone_input = "//input[@id='billingMobilePhoneNumber']"
    billing_address_input = "//input[@id='billingAddressOne']"
    billing_state_dropdown = ".billingState"
    billing_city_input = "//input[@id='billingAddressCity']"
    billing_postal_code_input = "//input[@id='billingZipCode']"

    billing_first_name_text = "Prashant"
    billing_last_name_text = "Vadher"
    billing_phone_text = "9558112787"
    billing_address_text = "14410 California Ave"
    billing_city_text = "Baldwin Park"
    billing_state_text = "CA"
    billing_postal_code_text = "91706-1740"

    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)

    def test_select_paypal_payment_method(self):
        try:
            self.timeout(2000)
            self.click(self.payment_by_paypal)
            self.timeout(2000)
            print("CHECKOUT PAYMENT: PAYMENT METHOD IS CHANGED TO PAYPAL..")
        except:
            print("*****CHECKOUT PAYMENT: NOT ABLE TO SELECT PAYPAL PAYMENT METHOD..******")

    def test_select_cards_payment_method(self):
        try:
            self.timeout(2000)
            self.click(self.payment_by_cards)
            self.timeout(2000)
            print("CHECKOUT PAYMENT: PAYMENT METHOD IS CHANGED TO CARDS..")

        except:
            print("*****CHECKOUT PAYMENT: NOT ABLE TO SELECT CARDS PAYMENT METHOD..******")
   

    def test_enter_amex_credit_card_details(self):
        try:
            self.timeout(5000)
            self.page.frame_locator(self.card_number_iframe).get_by_role("textbox").fill(self.amex_card_number_text)
            self.page.frame_locator(self.expiry_date_iframe).get_by_role("textbox").fill(self.amex_expiry_date_text)
            self.page.frame_locator(self.cvv_iframe).get_by_role("textbox").fill(self.amex_cvv_text)
            self.fill(self.card_holder_name_input, self.card_holder_name_text)
            self.timeout(2000)
            self.screenshot.take_page_screenshot("CHECKOUT_PAYMENT_AMEX")
            print("[CHECKOUT-CARDS] AMEX CREDIT CARD DETAILS ARE ADDED ON THE PAYMENT PAGE..")

        except:
            print("*****[CHECKOUT-CARDS] AMEX CREDIT CARD DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")

    def test_enter_mastercard_credit_card_details(self):
        try:
            self.timeout(5000)
            self.page.frame_locator(self.card_number_iframe).get_by_role("textbox").fill(self.mc_card_number_text)
            self.page.frame_locator(self.expiry_date_iframe).get_by_role("textbox").fill(self.mc_expiry_date_text)
            self.page.frame_locator(self.cvv_iframe).get_by_role("textbox").fill(self.mc_cvv_text)
            self.fill(self.card_holder_name_input, self.card_holder_name_text)
            self.timeout(2000)
            self.screenshot.take_page_screenshot("CHECKOUT_PAYMENT_MASTERCARD")
            print("[CHECKOUT-CARDS] MASTERCARD CREDIT CARD DETAILS ARE ADDED ON THE PAYMENT PAGE..")

        except:
            print("*****[CHECKOUT-CARDS] MASTERCARD CREDIT CARD DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")


    def test_enter_visa_credit_card_details(self):
        try:
            self.timeout(5000)
            self.page.frame_locator(self.card_number_iframe).get_by_role("textbox").fill(self.visa_card_number_text)
            self.page.frame_locator(self.expiry_date_iframe).get_by_role("textbox").fill(self.visa_expiry_date_text)
            self.page.frame_locator(self.cvv_iframe).get_by_role("textbox").fill(self.visa_cvv_text)
            self.fill(self.card_holder_name_input, self.card_holder_name_text)
            self.timeout(2000)
            self.screenshot.take_page_screenshot("CHECKOUT_PAYMENT_VISA")
            print("[CHECKOUT-CARDS] VISA CREDIT CARD DETAILS ARE ADDED ON THE PAYMENT PAGE..")

        except:
            print("*****[CHECKOUT-CARDS] VISA CREDIT CARD DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")

    def test_enter_union_pay_credit_card_details(self):
        try:
            self.timeout(5000)
            self.page.frame_locator(self.card_number_iframe).get_by_role("textbox").fill(self.union_pay_card_number_text)
            self.page.frame_locator(self.expiry_date_iframe).get_by_role("textbox").fill(self.union_pay_expiry_date_text)
            self.page.frame_locator(self.cvv_iframe).get_by_role("textbox").fill(self.union_pay_cvv_text)
            self.fill(self.card_holder_name_input, self.card_holder_name_text)
            self.timeout(2000)
            self.screenshot.take_page_screenshot("CHECKOUT_PAYMENT_UNION_PAY")
            print("[CHECKOUT-CARDS] UNION PAY CREDIT CARD DETAILS ARE ADDED ON THE PAYMENT PAGE..")

        except:
            print("*****[CHECKOUT-CARDS] UNION PAY CREDIT CARD DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")

    def test_enter_discover_credit_card_details(self):
        try:
            self.timeout(5000)
            self.page.frame_locator(self.card_number_iframe).get_by_role("textbox").fill(self.discover_card_number_text)
            self.page.frame_locator(self.expiry_date_iframe).get_by_role("textbox").fill(self.discover_expiry_date_text)
            self.page.frame_locator(self.cvv_iframe).get_by_role("textbox").fill(self.discover_cvv_text)
            self.fill(self.card_holder_name_input, self.card_holder_name_text)
            self.timeout(2000)
            self.screenshot.take_page_screenshot("CHECKOUT_PAYMENT_DISCOVER")
            print("[CHECKOUT-CARDS] DISCOVER CREDIT CARD DETAILS ARE ADDED ON THE PAYMENT PAGE..")

        except:
            print("*****[CHECKOUT-CARDS] DISCOVER CREDIT CARD DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")

    def test_enter_jcb_credit_card_details(self):
        try:
            self.timeout(5000)
            self.page.frame_locator(self.card_number_iframe).get_by_role("textbox").fill(self.jcb_card_number_text)
            self.page.frame_locator(self.expiry_date_iframe).get_by_role("textbox").fill(self.jcb_expiry_date_text)
            self.page.frame_locator(self.cvv_iframe).get_by_role("textbox").fill(self.jcb_cvv_text)
            self.fill(self.card_holder_name_input, self.card_holder_name_text)
            self.timeout(2000)
            self.screenshot.take_page_screenshot("CHECKOUT_PAYMENT_JCB")
            print("[CHECKOUT-CARDS] JCB CREDIT CARD DETAILS ARE ADDED ON THE PAYMENT PAGE..")

        except:
            print("*****[CHECKOUT-CARDS] JCB CREDIT CARD DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")

    def test_enter_change_billing_name_details(self):
        try:
            self.timeout(2000)
            self.scroll_down(self.billing_first_name_input)
            self.select_option(self.billing_title_dropdown,self.billing_title_value)
            self.fill(self.billing_first_name_input, self.billing_first_name_text)
            self.fill(self.billing_last_name_input, self.billing_last_name_text)
            self.fill(self.billing_phone_input, self.billing_phone_text)
            self.screenshot.take_page_screenshot("CHECKOUT_BILLING_NAME")
            print("[CHECKOUT-BILLING_NAME] BILLING NAME DETAILS ARE ADDED ON THE PAYMENT PAGE..")
        except:
            print("*****[CHECKOUT-BILLING] BILLING NAME DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")


    def test_enter_change_billing_address_details(self):
        try:
            self.timeout(2000)
            self.scroll_down(self.billing_address_input)
            self.fill(self.billing_address_input,self.billing_address_text)
            #State dropdown
            print(self.page.locator("#state").count())
            print(self.page.locator("#state option").count())
            self.select_state_dropdown_value(self.billing_state_dropdown, self.billing_state_text)
            self.fill(self.billing_city_input,self.billing_city_text)
            self.fill(self.billing_postal_code_input,self.billing_postal_code_text)
            self.screenshot.take_page_screenshot("CHECKOUT_BILLING_ADDRESS")
            print("[CHECKOUT-BILLING] BILLING ADDRESS DETAILS ARE ADDED ON THE PAYMENT PAGE..")
        except:
            print("*****[CHECKOUT-BILLING] BILLING ADDRESS DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")

    def test_use_delivery_as_billing_address_checkbox(self):
        try:
            self.timeout(2000)
            self.scroll_down(self.use_delivery_as_billing_input)
            self.click(self.use_delivery_as_billing_input)
            self.timeout(3000)
            self.screenshot.take_page_screenshot("CHECKOUT_PAYMENT_SAME_ADDRESS")
            print("[CHECKOUT-SAME ADDRESS] CHECKED USE DELIVERY ADDRESS AS BILLING ADDRESS CHECKBOX..")
        except:
            print("[CHECKOUT-SAME ADDRESS] NOT ABLE TO CHECK USE DELIVERY ADDRESS AS BILLING ADDRESS CHECKBOX..")
  
    def test_continue_to_review_from_payment_page(self):
        try:
            self.timeout(3000)
            self.click(self.continue_to_review_cta)
            self.timeout(3000)
            print("[CHECKOUT-PAYMENT] USER IS REDIRECTED TO THE ORDER REVIEW PAGE..")
        except:
            print("*****[CHECKOUT-PAYMENT] USER IS NOT REDIRECTED TO THE ORDER REVIEW PAGE..*****")
