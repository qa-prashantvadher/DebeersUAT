from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
import random
from dotenv import load_dotenv
import os
import logging

load_dotenv(override=True)
logger = logging.getLogger(__name__)

class Checkout_Payment(BasePage):
    COUNTRY = os.getenv("LOCALE").upper()
    continue_to_review_cta = "//button[@class='btn btn-primary mx-auto submit-payment']"

    if COUNTRY == "US":
        # Billing Name
        billing_first_name_list = ["Oliver", "Jack", "Harry", "Jacob", "Charlie", "Thomas", "George", "James", "Robert"]
        billing_last_name_list = ["Smith", "Taylor", "Brown", "Williams", "Wilson", "Evans", "Robinson", "Walker","Thompson", "Brook"]
        # State dropdown
        billing_state_dropdown = ".billingState"
        # Billing Address List
        billing_addresses = [
            {
                "billing_address_text": "1128 Park Ave Apt 123",
                "billing_city_text": "New York",
                "billing_state_county_text": "NY",
                "billing_postal_code_text": "10128-1203"
            },
            {
                "billing_address_text": "9221 Hooper Ave Apt 1",
                "billing_city_text": "Los Angeles",
                "billing_state_county_text": "CA",
                "billing_postal_code_text": "90002-2034"
            },
            {
                "billing_address_text": "20 S Pearl St Apt 1",
                "billing_city_text": "Denver",
                "billing_state_county_text": "CO",
                "billing_postal_code_text": "80209-2033"
            },
            {
                "billing_address_text": "417 22nd St SE Apt A",
                "billing_city_text": "Auburn",
                "billing_state_county_text": "WA",
                "billing_postal_code_text": "98002-6832"
            },
            {
                "billing_address_text": "13833 Akers Cir",
                "billing_city_text": "Eagle River",
                "billing_state_county_text": "AK",
                "billing_postal_code_text": "99577-6737"
            }
        ]
    elif COUNTRY == "UK":
        # Billing Name
        billing_first_name_list = ["Oliver", "Jack", "Harry", "Jacob", "Charlie", "Thomas", "George", "James", "Robert"]
        billing_last_name_list = ["Smith", "Taylor", "Brown", "Williams", "Wilson", "Evans", "Robinson", "Walker","Thompson", "Brook"]
        # County Text-field
        billing_county_input = "//input[@id='billingState']"
        # Billing Address List
        billing_addresses = [
            {
                "billing_address_text": "Flat 1, 8 Kensington Palace Gardens",
                "billing_city_text": "London",
                "billing_state_county_text": "",
                "billing_postal_code_text": "W8 4QP"
            },
            {
                "billing_address_text": "16 Rowlandsway, Civic Centre",
                "billing_city_text": "Manchester",
                "billing_state_county_text": "Greater Manchester",
                "billing_postal_code_text": "M22 5RG"
            },
            {
                "billing_address_text": "101 Conleach Road",
                "billing_city_text": "Liverpool",
                "billing_state_county_text": "Merseyside",
                "billing_postal_code_text": "L24 0TR"
            }]
    elif COUNTRY == "FR":
        # Billing Name
        billing_first_name_list = ["Gabriel","Raphaël","Louis","Arthur","Léon","Léo","Oscar","Adam","Noah"]
        billing_last_name_list = ["Martin","Bernard","Dubois","Thomas","Robert","Richard","Michel","Roux","Laurent","Garcia"]
        # State Text-field
        billing_state_input = "//input[@id='billingState']"
        # Billing Address List
        billing_addresses = [
            {
                "billing_address_text": "1 Rue du Général Camou",
                "billing_city_text": "Paris",
                "billing_state_county_text": "Île-de-France",
                "billing_postal_code_text": "75007"
            },
            {
                "billing_address_text": "34 Rue Antoine Primat",
                "billing_city_text": "Villeurbanne",
                "billing_state_county_text": "Auvergne-Rhône-Alpes",
                "billing_postal_code_text": "69100"
            },
            {
                "billing_address_text": "8 Rue De Londres",
                "billing_city_text": "Paris",
                "billing_state_county_text": "Île-de-France",
                "billing_postal_code_text": "75009"
            }]

    elif COUNTRY == "HK":
        # Billing Name
        billing_first_name_list = ["Yan", "Yee", "Wah", "Ming", "Mei", "Man", "Kwong", "Kei", "Ho"]
        billing_last_name_list = ["Chan", "Wong", "Lee", "Leung", "Ho", "Cheung", "Lam", "Lau", "Tang", "Yeung"]
        # State Text-field
        billing_state_input = "//input[@id='billingState']"
        # Billing Address List
        billing_addresses = [
            {
                "billing_address_text": "1 Muk Ning Street",
                "billing_city_text": "Kowloon",
                "billing_state_county_text": "Hong Kong",
                "billing_postal_code_text": ""
            },
            {
                "billing_address_text": "Flat B, 18/F, Tower 3, Metro City, Tseung Kwan O",
                "billing_city_text": "New Territories",
                "billing_state_county_text": "Hong Kong",
                "billing_postal_code_text": ""
            },
            {
                "billing_address_text": "City plaza, 18 Tai Koo Shing Rd, Quarry Bay",
                "billing_city_text": "Hong Kong Island",
                "billing_state_county_text": "Hong Kong",
                "billing_postal_code_text": ""
            }]

    elif COUNTRY == "TW":
        # Billing Name
        billing_first_name_list = ["Yan", "Yee", "Wah", "Ming", "Mei", "Man", "Kwong", "Kei", "Ho"]
        billing_last_name_list = ["Chan", "Wong", "Lee", "Leung", "Ho", "Cheung", "Lam", "Lau", "Tang", "Yeung"]
        # State Text-field
        billing_state_input = "//input[@id='billingState']"
        # Billing Address List
        billing_addresses = [
            {
                "billing_address_text": "No. 18, Alley 2, Lane 410, Minzu E Road",
                "billing_city_text": "Taipei",
                "billing_state_county_text": "Taipei City",
                "billing_postal_code_text": "10491"
            },
            {
                "billing_address_text": "No. 65, Dongxin Street",
                "billing_city_text": "Taichung",
                "billing_state_county_text": "Taichung City",
                "billing_postal_code_text": "401016"
            },
            {
                "billing_address_text": "No. 104, Wenming Road",
                "billing_city_text": "Beigang",
                "billing_state_county_text": "Yunlin County",
                "billing_postal_code_text": "65141"
            }]

    #Payment Methods
    payment_by_cards = "//input[@id='rb_scheme']"
    payment_by_paypal = "//input[@id='rb_paypal']"

    #Cards
    card_number_iframe = "[data-cse='encryptedCardNumber'] iframe"
    expiry_date_iframe = "[data-cse='encryptedExpiryDate'] iframe"
    cvv_iframe = "[data-cse='encryptedSecurityCode'] iframe"
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

    mc_card_number_text = "5555555555554444"
    mc_expiry_date_text = "03/30"
    mc_cvv_text = "737"

    visa_card_number_text = "4444333322221111"
    visa_expiry_date_text = "03/30"
    visa_cvv_text = "737"

    dankort_card_number_text = "4444333322221111"
    dankort_expiry_date_text = "03/30"
    dankort_cvv_text = "737"

    cartes_visa_card_number_text = "4035501000000008"
    cartes_visa_expiry_date_text = "03/30"
    cartes_visa_cvv_text = "737"

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
    billing_city_input = "//input[@id='billingAddressCity']"
    billing_postal_code_input = "//input[@id='billingZipCode']"

    billing_phone_text = "9558112787"


    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)

    def test_select_paypal_payment_method(self):
        try:
            self.timeout(1000)
            self.click(self.payment_by_paypal)
            self.timeout(1000)
            logger.info("[CHECKOUT-PAYMENT] PAYMENT METHOD IS CHANGED TO PAYPAL..")
        except:
            logger.error("*****[CHECKOUT-PAYMENT] NOT ABLE TO SELECT PAYPAL PAYMENT METHOD..******")

    def test_select_cards_payment_method(self):
        try:
            self.timeout(1000)
            self.click(self.payment_by_cards)
            self.timeout(1000)
            logger.info("[CHECKOUT-PAYMENT] PAYMENT METHOD IS CHANGED TO CARDS..")
        except:
            logger.error("*****[CHECKOUT-PAYMENT] NOT ABLE TO SELECT CARDS PAYMENT METHOD..******")

    def test_enter_amex_credit_card_details(self):
        try:
            self.timeout(3000)
            self.page.frame_locator(self.card_number_iframe).get_by_role("textbox").fill(self.amex_card_number_text)
            self.page.frame_locator(self.expiry_date_iframe).get_by_role("textbox").fill(self.amex_expiry_date_text)
            self.page.frame_locator(self.cvv_iframe).get_by_role("textbox").fill(self.amex_cvv_text)
            self.fill(self.card_holder_name_input, self.card_holder_name_text)
            self.timeout(1000)
            self.screenshot.take_order_page_screenshot("CHECKOUT_PAYMENT_AMEX")
            logger.info("[CHECKOUT-CARDS] AMEX CREDIT CARD DETAILS ARE ADDED ON THE PAYMENT PAGE..")
        except:
            logger.error("*****[CHECKOUT-CARDS] AMEX CREDIT CARD DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")

    def test_enter_mastercard_credit_card_details(self):
        try:
            self.timeout(3000)
            self.page.frame_locator(self.card_number_iframe).get_by_role("textbox").fill(self.mc_card_number_text)
            self.page.frame_locator(self.expiry_date_iframe).get_by_role("textbox").fill(self.mc_expiry_date_text)
            self.page.frame_locator(self.cvv_iframe).get_by_role("textbox").fill(self.mc_cvv_text)
            self.fill(self.card_holder_name_input, self.card_holder_name_text)
            self.timeout(1000)
            self.screenshot.take_order_page_screenshot("CHECKOUT_PAYMENT_MASTERCARD")
            logger.info("[CHECKOUT-CARDS] MASTERCARD CREDIT CARD DETAILS ARE ADDED ON THE PAYMENT PAGE..")
        except:
            logger.error("*****[CHECKOUT-CARDS] MASTERCARD CREDIT CARD DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")

    def test_enter_visa_credit_card_details(self):
        try:
            self.timeout(3000)
            self.page.frame_locator(self.card_number_iframe).get_by_role("textbox").fill(self.visa_card_number_text)
            self.page.frame_locator(self.expiry_date_iframe).get_by_role("textbox").fill(self.visa_expiry_date_text)
            self.page.frame_locator(self.cvv_iframe).get_by_role("textbox").fill(self.visa_cvv_text)
            self.fill(self.card_holder_name_input, self.card_holder_name_text)
            self.timeout(1000)
            self.screenshot.take_order_page_screenshot("CHECKOUT_PAYMENT_VISA")
            logger.info("[CHECKOUT-CARDS] VISA CREDIT CARD DETAILS ARE ADDED ON THE PAYMENT PAGE..")
        except:
            logger.error("*****[CHECKOUT-CARDS] VISA CREDIT CARD DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")

    def test_enter_union_pay_credit_card_details(self):
        try:
            self.timeout(3000)
            self.page.frame_locator(self.card_number_iframe).get_by_role("textbox").fill(self.union_pay_card_number_text)
            self.page.frame_locator(self.expiry_date_iframe).get_by_role("textbox").fill(self.union_pay_expiry_date_text)
            self.page.frame_locator(self.cvv_iframe).get_by_role("textbox").fill(self.union_pay_cvv_text)
            self.fill(self.card_holder_name_input, self.card_holder_name_text)
            self.timeout(1000)
            self.screenshot.take_order_page_screenshot("CHECKOUT_PAYMENT_UNION_PAY")
            logger.info("[CHECKOUT-CARDS] UNION PAY CREDIT CARD DETAILS ARE ADDED ON THE PAYMENT PAGE..")
        except:
            logger.error("*****[CHECKOUT-CARDS] UNION PAY CREDIT CARD DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")

    def test_enter_discover_credit_card_details(self):
        try:
            self.timeout(3000)
            self.page.frame_locator(self.card_number_iframe).get_by_role("textbox").fill(self.discover_card_number_text)
            self.page.frame_locator(self.expiry_date_iframe).get_by_role("textbox").fill(self.discover_expiry_date_text)
            self.page.frame_locator(self.cvv_iframe).get_by_role("textbox").fill(self.discover_cvv_text)
            self.fill(self.card_holder_name_input, self.card_holder_name_text)
            self.timeout(1000)
            self.screenshot.take_order_page_screenshot("CHECKOUT_PAYMENT_DISCOVER")
            logger.info("[CHECKOUT-CARDS] DISCOVER CREDIT CARD DETAILS ARE ADDED ON THE PAYMENT PAGE..")
        except:
            logger.error("*****[CHECKOUT-CARDS] DISCOVER CREDIT CARD DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")

    def test_enter_cartes_visa_credit_card_details(self):
        try:
            self.timeout(3000)
            self.page.frame_locator(self.card_number_iframe).get_by_role("textbox").fill(self.cartes_visa_card_number_text)
            self.page.frame_locator(self.expiry_date_iframe).get_by_role("textbox").fill(self.cartes_visa_expiry_date_text)
            self.page.frame_locator(self.cvv_iframe).get_by_role("textbox").fill(self.cartes_visa_cvv_text)
            self.fill(self.card_holder_name_input, self.card_holder_name_text)
            self.timeout(1000)
            self.screenshot.take_order_page_screenshot("CHECKOUT_PAYMENT_DISCOVER")
            logger.info("[CHECKOUT-CARDS] DISCOVER CREDIT CARD DETAILS ARE ADDED ON THE PAYMENT PAGE..")
        except:
            logger.error("*****[CHECKOUT-CARDS] DISCOVER CREDIT CARD DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")

    def test_enter_change_billing_name_details(self):
        try:
            self.timeout(1000)
            billing_first_name_text = random.choice(self.billing_first_name_list)
            billing_last_name_text = random.choice(self.billing_last_name_list)
            self.scroll_down(self.billing_first_name_input)
            self.select_option(self.billing_title_dropdown,self.billing_title_value)
            self.fill(self.billing_first_name_input, billing_first_name_text)
            self.fill(self.billing_last_name_input, billing_last_name_text)
            self.fill(self.billing_phone_input, self.billing_phone_text)
            self.screenshot.take_order_page_screenshot("CHECKOUT_BILLING_NAME")
            logger.info("[CHECKOUT-BILLING] BILLING NAME DETAILS ARE ADDED ON THE PAYMENT PAGE..")
            logger.info(f"#####[CHECKOUT-BILLING] NAME: {self.billing_title_value.upper()} {billing_first_name_text.upper()} {billing_last_name_text.upper()}")
        except:
            logger.error("*****[CHECKOUT-BILLING] BILLING NAME DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")

    def test_enter_change_billing_address_details(self):
        try:
            # Pick random address
            selected_billing_address = random.choice(self.billing_addresses)
            self.timeout(1000)
            self.scroll_down(self.billing_address_input)
            self.fill(self.billing_address_input,selected_billing_address["billing_address_text"])

            if self.COUNTRY == "US":
                # State dropdown
                self.select_state_dropdown_value(self.billing_state_dropdown, selected_billing_address["billing_state_county_text"])
            elif self.COUNTRY == "UK":
                # County Text-field
                self.fill(self.billing_county_input, selected_billing_address["billing_state_county_text"])
            elif self.COUNTRY == "FR" or self.COUNTRY == "HK" or self.COUNTRY == "TW":
                # State Text-field
                self.fill(self.billing_state_input, selected_billing_address["billing_state_county_text"])
            self.fill(self.billing_city_input,selected_billing_address["billing_city_text"])
            self.fill(self.billing_postal_code_input,selected_billing_address["billing_postal_code_text"])
            self.screenshot.take_order_page_screenshot("CHECKOUT_BILLING_ADDRESS")
            logger.info("[CHECKOUT-BILLING] BILLING ADDRESS DETAILS ARE ADDED ON THE PAYMENT PAGE..")
            logger.info(f"#####[CHECKOUT-BILLING] BILLING ADDRESS: {selected_billing_address["billing_address_text"].upper()},{selected_billing_address["billing_city_text"].upper()}, {selected_billing_address["billing_state_county_text"].upper()}, {selected_billing_address["billing_postal_code_text"].upper()}")
        except:
            logger.error("*****[CHECKOUT-BILLING] BILLING ADDRESS DETAILS ARE NOT ADDED ON THE PAYMENT PAGE..*****")

    def test_use_delivery_as_billing_address_checkbox(self):
        try:
            self.timeout(1000)
            self.scroll_down(self.use_delivery_as_billing_input)
            self.click(self.use_delivery_as_billing_input)
            self.timeout(1000)
            self.screenshot.take_order_page_screenshot("CHECKOUT_PAYMENT_SAME_ADDRESS_CHECKBOX")
            logger.info("[CHECKOUT-SAME ADDRESS] CHECKED \"USE DELIVERY ADDRESS AS BILLING ADDRESS\" CHECKBOX..")
        except:
            logger.error("*****[CHECKOUT-SAME ADDRESS] NOT ABLE TO CHECK \"USE DELIVERY ADDRESS AS BILLING ADDRESS\" CHECKBOX..*****")
  
    def test_continue_to_review_from_payment_page(self):
        try:
            self.timeout(1000)
            self.click(self.continue_to_review_cta)
            self.timeout(2000)
            logger.info("[CHECKOUT-PAYMENT] USER IS REDIRECTED TO THE \"ORDER REVIEW\" PAGE..")
        except:
            logger.error("*****[CHECKOUT-PAYMENT] USER IS NOT REDIRECTED TO THE \"ORDER REVIEW\" PAGE..*****")
