from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
import random
from dotenv import load_dotenv
import os

load_dotenv(override=True)

class Checkout_Delivery(BasePage):
    COUNTRY = os.getenv("LOCALE")

    if COUNTRY == "US":
        # Shipping Methods
        premium_delivery_tab = "//button[@id='US-SHIPPING-01']"
        collect_in_store_tab = "//button[@id='US-SHIPPING-02']"
        #State Dropdown
        premium_state_dropdown = "//*[@id='state']"
        # Delivery Date
        premium_delivery_date = "//span[@class='method-date__text-time estimatedArrivalTime US-SHIPPING-01']"
        collect_in_store_delivery_date = "//span[@class='method-date__text-time estimatedArrivalTime US-SHIPPING-02']"
        #Delivery Address list
        delivery_addresses = [
            {
                "premium_address_text": "1128 Park Ave Apt 123",
                "premium_city_text": "New York",
                "premium_state_county_text": "NY",
                "premium_postal_code_text": "10128-1203"
            },
            {
                "premium_address_text": "9221 Hooper Ave Apt 1",
                "premium_city_text": "Los Angeles",
                "premium_state_county_text": "CA",
                "premium_postal_code_text": "90002-2034"
            },
            {
                "premium_address_text": "20 S Pearl St Apt 1",
                "premium_city_text": "Denver",
                "premium_state_county_text": "CO",
                "premium_postal_code_text": "80209-2033"
            }, {
                "premium_address_text": "417 22nd St SE Apt A",
                "premium_city_text": "Auburn",
                "premium_state_county_text": "WA",
                "premium_postal_code_text": "98002-6832"
            },
            {
                "premium_address_text": "13833 Akers Cir",
                "premium_city_text": "Eagle River",
                "premium_state_county_text": "AK",
                "premium_postal_code_text": "99577-6737"
            }]

    elif COUNTRY == "UK":
        # Shipping Methods
        premium_delivery_tab = "//button[@id='GB-SHIPPING-01']"
        collect_in_store_tab = "//button[@id='GB-SHIPPING-02']"
        # County Input Field
        premium_county_input = "//input[@id='shippingState']"
        # Delivery Date
        premium_delivery_date = "//span[@class='method-date__text-time estimatedArrivalTime GB-SHIPPING-01']"
        collect_in_store_delivery_date = "//span[@class='method-date__text-time estimatedArrivalTime GB-SHIPPING-02']"
        # Delivery Address list
        delivery_addresses = [
            {
                "premium_address_text": "Flat 1, 8 Kensington Palace Gardens",
                "premium_city_text": "London",
                "premium_state_county_text": "",
                "premium_postal_code_text": "W8 4QP"
            },
            {
                "premium_address_text": "16 Rowlandsway, Civic Centre",
                "premium_city_text": "Manchester",
                "premium_state_county_text": "Greater Manchester",
                "premium_postal_code_text": "M22 5RG"
            },
            {
                "premium_address_text": "101 Conleach Road",
                "premium_city_text": "Liverpool",
                "premium_state_county_text": "CMerseysideO",
                "premium_postal_code_text": "L24 0TR"
            }]

    #Premium Delivery > Shipping Address Info
    premium_address_input = "//input[@id='shippingAddressOne']"
    premium_city_input = "//input[@id='shippingAddressCity']"
    premium_postal_code_input = "//input[@id='shippingZipCode']"
    premium_add_new_address_option = "//a[@class='anchor btn-add-new js-btn-add-new ']"

    # Client Service Error Popup
    client_service_error_popup_close = "//button[@class='btn close']"
    error_code_text = "#errorCodeModal"

    # Collect in Store Info:
    self_collect_checkbox = "//input[@id='collectByBuyer']"
    someone_else_collect_checkbox = "//input[@id='collectByAgent']"

    # General Info:
    delivery_title_dropdown = "//*[@id='customerTitle']"
    delivery_title_value = "mr."
    first_name_input = "//input[@id='shippingFirstName']"
    last_name_input = "//input[@id='shippingLastName']"
    phone_input = "//input[@id='accountMobilePhoneNumber']"
    gift_checkbox = "input[name='dwfrm_shipping_shippingAddress_isGift']"
    gift_message_input = "[name='dwfrm_shipping_shippingAddress_giftMessage']"

    delivery_collector_first_name_list = ["Oliver","Jack","Harry","Jacob","Charlie","Thomas","George","James","Robert"]
    delivery_collector_last_name_list = ["Smith","Taylor","Brown","Williams","Wilson","Evans","Robinson","Walker","Thompson","Brook"]
    phone_text = "8090809080"
    collector_phone_text = "8989089890"

    gift_message_text = "Test order with a gift message. I hope this piece adds a beautiful touch to your collection and truly brings you joy and elegance each day you wear it"

    continue_payment_cta = "//button[@class='btn btn-primary mx-auto submit-shipping']"



    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)

    def test_open_premium_delivery_tab(self):
        try:
            self.timeout(1000)
            self.click(Checkout_Delivery.premium_delivery_tab)
            self.timeout(2000)
        except:
            print("*****[CHECKOUT-PREMIUM] NOT ABLE TO OPEN PREMIUM DELIVERY TAB..*****")

    def test_open_collect_in_store_tab(self):
        try:
            self.timeout(1000)
            self.click(Checkout_Delivery.collect_in_store_tab)
            self.timeout(2000)
        except:
            print("*****[CHECKOUT-COLLECT] NOT ABLE TO OPEN COLLECT IN STORE TAB..*****")

    def test_select_self_collect_checkbox(self):
        try:
            self.timeout(7000)
            self.click(self.self_collect_checkbox)
            self.timeout(3000)
            delivery_date = self.get_text(self.collect_in_store_delivery_date).strip()
            self.screenshot.take_order_page_screenshot("CHECKOUT_SELF_COLLECT")
            print(f"[CHECKOUT-SELF] DELIVERY DATE: {delivery_date.upper()}.")
        except:
            print("*****[CHECKOUT-SELF] NOT ABLE TO SELECT SELF COLLECT CHECKBOX..*****")

    def test_select_someone_else_collect_checkbox(self):
        try:
            self.timeout(7000)
            self.click(self.someone_else_collect_checkbox)
            self.timeout(3000)
            delivery_date = self.get_text(self.collect_in_store_delivery_date).strip()
            self.screenshot.take_order_page_screenshot("CHECKOUT_SOMEONE_ELSE_COLLECT")
            print(f"[CHECKOUT-SOMEONE] DELIVERY DATE: {delivery_date.upper()}.")
        except:
            print("*****[CHECKOUT-SOMEONE] NOT ABLE TO SELECT SOMEONE ELSE COLLECT CHECKBOX..*****")


    def test_enter_user_details_in_premium_delivery(self):
        try:
            self.timeout(1000)
            first_name_text = random.choice(self.delivery_collector_first_name_list)
            last_name_text = random.choice(self.delivery_collector_last_name_list)
            self.select_option(self.delivery_title_dropdown, self.delivery_title_value)
            self.fill(self.first_name_input, first_name_text)
            self.fill(self.last_name_input, last_name_text)
            self.fill(self.phone_input, self.phone_text)
            self.timeout(1000)
            print("[CHECKOUT-PREMIUM] USER DETAILS ARE ENTERED SUCCESSFULLY..")
        except:
            print("*****[CHECKOUT-PREMIUM] NOT ABLE TO ENTER USER DETAILS..*****")

    def test_enter_collector_details_in_store_collect(self):
        try:
            self.timeout(1000)
            collector_first_name_text = random.choice(self.delivery_collector_first_name_list)
            collector_last_name_text = random.choice(self.delivery_collector_last_name_list)
            self.select_option(self.delivery_title_dropdown, self.delivery_title_value)
            self.fill(self.first_name_input, collector_first_name_text)
            self.fill(self.last_name_input, collector_last_name_text)
            self.fill(self.phone_input, self.collector_phone_text)
            print("[CHECKOUT-COLLECTOR] COLLECTOR DETAILS ARE ENTERED..")

        except:
            print("*****[CHECKOUT-COLLECTOR] NOT ABLE TO ENTER COLLECTOR DETAILS..*****")

    def test_add_new_address_as_register(self):
        try:
            self.timeout(1000)
            if self.is_visible(self.premium_add_new_address_option):
                self.click(self.premium_add_new_address_option)
                self.timeout(1000)
            else:
                pass  # do nothing, continue with next lines
        except:
            print("*****[CHECKOUT-PREMIUM] NOT ABLE TO OPEN ADD NEW ADDRESS SECTION..*****")

    def test_enter_valid_delivery_address_in_premium_delivery(self):
        try:
            # Pick random address
            selected_delivery_address = random.choice(self.delivery_addresses)

            self.timeout(3000)
            if self.is_visible(self.premium_add_new_address_option):
                pass  # do nothing, continue with next lines
            else:
                self.timeout(1000)
                self.fill(self.premium_address_input, selected_delivery_address["premium_address_text"])
                if self.COUNTRY == "US":
                   # State dropdown
                    self.select_state_dropdown_value(self.premium_state_dropdown, selected_delivery_address["premium_state_county_text"])
                elif self.COUNTRY == "UK":
                    # County Text-field
                    self.fill(self.premium_county_input, selected_delivery_address["premium_state_county_text"])
                self.fill(self.premium_city_input, selected_delivery_address["premium_city_text"])
                self.fill(self.premium_postal_code_input, selected_delivery_address["premium_postal_code_text"])
                self.timeout(1000)
                print("[CHECKOUT-PREMIUM] VALID DELIVERY ADDRESS DETAILS ARE ENTERED SUCCESSFULLY..")

        except:
            print("*****[CHECKOUT-PREMIUM] NOT ABLE TO ENTER DELIVERY ADDRESS DETAILS..*****")

    def test_enter_invalid_delivery_address_in_premium_delivery(self):
        try:
            # Pick random address
            selected_delivery_address = random.choice(self.delivery_addresses)

            self.timeout(1000)
            self.fill(self.premium_address_input, selected_delivery_address["premium_address_text"])
            if self.COUNTRY == "US":
                # State dropdown
                self.select_state_dropdown_value(self.premium_state_dropdown, selected_delivery_address["premium_state_county_text"])
            elif self.COUNTRY == "UK":
                # County Text-field
                self.fill(self.premium_county_input, selected_delivery_address["premium_state_county_text"])
            self.fill(self.premium_city_input, "TESTING")
            self.fill(self.premium_postal_code_input, "TESTING")
            self.timeout(1000)
            print("[CHECKOUT-PREMIUM] INVALID DELIVERY ADDRESS DETAILS ARE ENTERED SUCCESSFULLY..")

        except:
            print("*****[CHECKOUT-PREMIUM] NOT ABLE TO ENTER DELIVERY ADDRESS DETAILS..*****")


    def test_delivery_date_on_premium_delivery(self):
        try:
            self.timeout(2000)
            delivery_date = self.get_text(self.premium_delivery_date).strip()
            self.screenshot.take_order_page_screenshot("CHECKOUT_DELIVERY")
            print(f"[CHECKOUT-DELIVERY] DELIVERY DATE: {delivery_date.upper()}")
        except:
            print("*****[CHECKOUT-DELIVERY] DELIVERY DATE DETAIL IS MISSING..*****")

    def test_delivery_date_on_collect_in_store(self):
        try:
            self.timeout(2000)
            delivery_date = self.get_text(self.collect_in_store_delivery_date).strip()
            self.screenshot.take_order_page_screenshot("CHECKOUT_IN_STORE")
            print(f"[CHECKOUT-IN STORE] DELIVERY DATE: {delivery_date.upper()}")
        except:
            print("*****[CHECKOUT-IN STORE] DELIVERY DATE DETAIL IS MISSING..*****")

    def test_close_client_service_tax_error_popup(self):
        try:
            self.timeout(1000)
            error_code = self.get_text(self.error_code_text).strip()
            self.screenshot.take_order_page_screenshot("CHECKOUT_DELIVERY")
            print(f"[CHECKOUT-DELIVERY] ERROR CODE: {error_code}")
            self.click(self.client_service_error_popup_close)
            self.timeout(1000)
        except:
            print("*****[CHECKOUT-DELIVERY] NOT ABLE TO CLOSE CLIENT SERVICE ERROR POPUP..*****")


    def test_enter_gift_message(self):
        try:
            if self.is_checked(self.gift_checkbox):
                print("[CHECKOUT-DELIVERY] GIFT OPTION IS ALREADY SELECTED...")
            else:
                self.click(self.gift_checkbox)
            self.timeout(1000)
            self.fill(self.gift_message_input, self.gift_message_text)
            self.timeout(1000)
            self.screenshot.take_order_page_screenshot("CHECKOUT_GIFT_MESSAGE")
        except:
            print("*****[CHECKOUT-DELIVERY] NOT ABLE TO ENTER GIFT MESSAGE..*****")

    def test_continue_to_payment_from_delivery_page(self):
        try:
            self.timeout(1000)
            self.click(self.continue_payment_cta)
            self.timeout(2000)
            print("[CHECKOUT-DELIVERY] USER IS REDIRECTED TO THE PAYMENT PAGE..")
        except:
            print("*****[CHECKOUT-DELIVERY] USER IS NOT REDIRECTED TO THE PAYMENT PAGE..*****")