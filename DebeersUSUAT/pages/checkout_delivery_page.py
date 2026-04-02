from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot

class Checkout_Delivery(BasePage):

    #Shiping Methods
    premium_delivery_tab = "//button[@id='US-SHIPPING-01']"
    collect_in_store_tab = "//button[@id='US-SHIPPING-02']"

    #Premium Delivery > Shipping Address Info
    premium_address_input = "//input[@id='shippingAddressOne']"
    premium_state_dropdown = "//*[@id='state']"
    premium_city_input = "//input[@id='shippingAddressCity']"
    premium_postal_code_input = "//input[@id='shippingZipCode']"

    premium_add_new_address_option = "//a[@class='anchor btn-add-new js-btn-add-new ']"

    premium_address_text = "1128 Park Ave Apt 123"
    premium_city_text = "New York"
    premium_state_text = "NY"
    premium_postal_code_text = "10128-1203"

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

    first_name_text = "Robert"
    last_name_text = "Johnson"
    phone_text = "8090809080"

    collector_first_name_text = "Maria"
    collector_last_name_text = "Rodriguez"
    collector_phone_text = "8989089890"

    gift_message_text = "Testing this gift message for an order containing two products. I hope these two pieces add a nice touch to your collection. Enjoy your jewellery now!"

    continue_payment_cta = "//button[@class='btn btn-primary mx-auto submit-shipping']"


    #Delivery Date
    premium_delivery_date = "//span[@class='method-date__text-time estimatedArrivalTime US-SHIPPING-01']"
    collect_in_store_delivery_date = "//span[@class='method-date__text-time estimatedArrivalTime US-SHIPPING-02']"


    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)

    def test_open_premium_delivery_tab(self):
        try:
            self.timeout(2000)
            self.click(Checkout_Delivery.premium_delivery_tab)
            self.timeout(2000)
        except:
            print("*****[CHECKOUT-PREMIUM] NOT ABLE TO OPEN PREMIUM DELIVERY TAB..*****")

    def test_open_collect_in_store_tab(self):
        try:
            self.timeout(2000)
            self.click(Checkout_Delivery.collect_in_store_tab)
            self.timeout(2000)
        except:
            print("*****[CHECKOUT-COLLECT] NOT ABLE TO OPEN COLLECT IN STORE TAB..*****")

    def test_select_self_collect_checkbox(self):
        try:
            self.timeout(2000)
            self.click(self.self_collect_checkbox)
            self.timeout(2000)
            delivery_date = self.get_text(self.collect_in_store_delivery_date).strip()
            self.screenshot.take_page_screenshot("CHECKOUT_SELF_COLLECT")
            print(f"[CHECKOUT-SELF] DELIVERY DATE: {delivery_date}.")
        except:
            print("*****[CHECKOUT-SELF] NOT ABLE TO SELECT SELF COLLECT CHECKBOX..*****")

    def test_select_someone_else_collect_checkbox(self):
        try:
            self.timeout(2000)
            self.click(self.someone_else_collect_checkbox)
            self.timeout(2000)
            delivery_date = self.get_text(self.collect_in_store_delivery_date).strip()
            self.screenshot.take_page_screenshot("CHECKOUT_SOMEONE_ELSE_COLLECT")
            print(f"[CHECKOUT-SOMEONE] DELIVERY DATE: {delivery_date}.")
        except:
            print("*****[CHECKOUT-SOMEONE] NOT ABLE TO SELECT SOMEONE ELSE COLLECT CHECKBOX..*****")


    def test_enter_user_details_in_premium_delivery(self):
        try:
            self.timeout(2000)
            self.select_option(self.delivery_title_dropdown, self.delivery_title_value)
            self.fill(self.first_name_input, self.first_name_text)
            self.fill(self.last_name_input, self.last_name_text)
            self.fill(self.phone_input, self.phone_text)
            self.timeout(2000)
            print("[CHECKOUT-PREMIUM] USER DETAILS ARE ENTERED SUCCESSFULLY..")
        except:
            print("*****[CHECKOUT-PREMIUM] NOT ABLE TO ENTER USER DETAILS..*****")

    def test_enter_collector_details_in_store_collect(self):
        try:
            self.timeout(2000)
            self.select_option(self.delivery_title_dropdown, self.delivery_title_value)
            self.fill(self.first_name_input, self.collector_first_name_text)
            self.fill(self.last_name_input, self.collector_last_name_text)
            self.fill(self.phone_input, self.collector_phone_text)
            print("[CHECKOUT-COLLECTOR] COLLECTOR DETAILS ARE ENTERED..")

        except:
            print("*****[CHECKOUT-STORE COLLECT] NOT ABLE TO ENTER COLLECTOR DETAILS..*****")

    def test_add_new_address_as_register(self):
        try:
            self.timeout(2000)
            self.click(self.premium_add_new_address_option)
            self.timeout(2000)
        except:
            print("*****[CHECKOUT-PREMIUM] NOT ABLE TO OPEN ADD NEW ADDRESS SECTION..*****")

    def test_enter_valid_delivery_address_in_premium_delivery(self):
        try:
            self.timeout(2000)
            self.fill(self.premium_address_input, self.premium_address_text)
            # State dropdown
            self.select_state_dropdown_value(self.premium_state_dropdown, self.premium_state_text)
            self.fill(self.premium_city_input, self.premium_city_text)
            self.fill(self.premium_postal_code_input, self.premium_postal_code_text)
            self.timeout(2000)
            print("[CHECKOUT-PREMIUM] DELIVERY ADDRESS DETAILS ARE ENTERED SUCCESSFULLY..")

        except:
            print("*****[CHECKOUT-PREMIUM] NOT ABLE TO ENTER DELIVERY ADDRESS DETAILS..*****")

    def test_enter_invalid_delivery_address_on_premium_delivery(self):
        try:
            self.timeout(2000)
            self.fill(self.premium_address_input, self.premium_address_text)
            # State dropdown
            self.select_state_dropdown_value(self.premium_state_dropdown, self.premium_state_text)
            self.fill(self.premium_city_input, "TESTING")
            self.fill(self.premium_postal_code_input, "TESTING")
            self.timeout(2000)
        except:
            print("*****[CHECKOUT-PREMIUM] NOT ABLE TO ENTER DELIVERY ADDRESS DETAILS..*****")


    def test_delivery_date_on_premium_delivery(self):
        try:
            self.timeout(3000)
            delivery_date = self.get_text(self.premium_delivery_date).strip()
            self.screenshot.take_page_screenshot("CHECKOUT_DELIVERY")
            print(f"[CHECKOUT-DELIVERY] DELIVERY DATE: {delivery_date}")
        except:
            print("*****[CHECKOUT-DELIVERY] DELIVERY DATE DETAIL IS MISSING..*****")

    def test_delivery_date_on_collect_in_store(self):
        try:
            self.timeout(3000)
            delivery_date = self.get_text(self.collect_in_store_delivery_date).strip()
            self.screenshot.take_page_screenshot("CHECKOUT_IN_STORE")
            print(f"[CHECKOUT-IN STORE] DELIVERY DATE: {delivery_date}")
        except:
            print("*****[CHECKOUT-IN STORE] DELIVERY DATE DETAIL IS MISSING..*****")

    def test_close_client_service_tax_error_popup(self):
        try:
            self.timeout(2000)
            error_code = self.get_text(self.error_code_text).strip()
            self.screenshot.take_page_screenshot("CHECKOUT_DELIVERY")
            print(f"[CHECKOUT-DELIVERY] ERROR CODE: {error_code}")
            self.click(self.client_service_error_popup_close)
            self.timeout(2000)
        except:
            print("*****[CHECKOUT-DELIVERY] NOT ABLE TO CLOSE CLIENT SERVICE ERROR POPUP..*****")


    def test_enter_gift_message(self):
        try:
            if self.is_checked(self.gift_checkbox):
                print("GIFT OPTION IS ALREADY SELECTED...")
            else:
                self.click(self.gift_checkbox)
            self.timeout(1000)
            self.fill(self.gift_message_input, self.gift_message_text)
            self.timeout(2000)
            self.screenshot.take_page_screenshot("CHECKOUT_GIFT_MESSAGE")
        except:
            print("*****[CHECKOUT-DELIVERY] NOT ABLE TO ENTER GIFT MESSAGE..*****")

    def test_continue_to_payment_from_delivery_page(self):
        try:
            self.timeout(3000)
            self.click(self.continue_payment_cta)
            self.timeout(3000)
            print("CHECKOUT-DELIVERY: USER IS REDIRECTED TO THE PAYMENT PAGE..")
        except:
            print("*****CHECKOUT-DELIVERY: USER IS NOT REDIRECTED TO THE PAYMENT PAGE..*****")
            
            

'''
    def test_premium_delivery_as_guest(self):
        try:
            self.timeout(2000)
            self.click(Checkout_Delivery.premium_delivery_tab)

            if self.is_checked(self.gift_checkbox):
                print("GIFT OPTION IS ALREADY SELECTED...")
            else:
                self.click(self.gift_checkbox)
            self.timeout(1000)
            self.fill(self.gift_message_input, self.gift_message_guest_premium_text)
            self.timeout(2000)
        except:
            print("*****[CHECKOUT-PREMIUM] USER IS NOT REDIRECTED TO PAYMENT PAGE..*****")

    def test_premium_delivery_as_registered(self):
        try:
            self.timeout(2000)
            self.click(Checkout_Delivery.premium_delivery_tab)
            self.timeout(2000)
            self.select_option(self.delivery_title_dropdown,self.delivery_title_value)

            delivery_date = self.get_text(self.premium_delivery_date).strip()
            self.screenshot.take_page_screenshot("CHECKOUT_REGISTERED_PREMIUM")
            print(f"[CHECKOUT-PREMIUM] DELIVERY DATE: {delivery_date}")
        except:
            print("*****[CHECKOUT-PREMIUM] USER IS NOT REDIRECTED TO PAYMENT PAGE..*****")

    def test_self_collect_in_store_as_guest(self):
        try:
            self.timeout(2000)
            self.click(Checkout_Delivery.collect_in_store_tab)
            self.timeout(2000)
            self.click(self.self_collect_checkbox)
            self.timeout(2000)
            self.select_option(self.delivery_title_dropdown,self.delivery_title_value)
            self.fill(self.first_name_input, self.first_name_text)
            self.fill(self.last_name_input, self.last_name_text)
            self.fill(self.phone_input, self.phone_text)

            if self.is_checked(self.gift_checkbox):
                print("GIFT OPTION IS ALREADY SELECTED...")
            else:
                self.click(self.gift_checkbox)
            self.timeout(1000)
            self.fill(self.gift_message_input, self.gift_message_guest_self_collect_text)
            self.timeout(1000)
        except:
            print("*****[CHECKOUT-SELF COLLECT] ERROR ON COLLECT IN STORE (SELF COLLECT) DELIVERY PAGE..*****")


    def test_self_collect_in_store_as_registered(self):
        try:
            self.timeout(2000)
            self.click(Checkout_Delivery.collect_in_store_tab)
            self.timeout(2000)
            self.click(self.self_collect_checkbox)
            self.timeout(1000)
            self.select_option(self.delivery_title_dropdown,self.delivery_title_value)

            if self.is_checked(self.gift_checkbox):
                print("GIFT OPTION IS ALREADY SELECTED...")
            else:
                self.click(self.gift_checkbox)
            self.timeout(1000)
            self.fill(self.gift_message_input, self.gift_message_registered_self_collect_text)
            self.timeout(1000)
            delivery_date = self.get_text(self.collect_in_store_delivery_date).strip()
            self.screenshot.take_page_screenshot("CHECKOUT_REGISTERED_SELF_COLLECT")
            print(f"[CHECKOUT-SELF COLLECT] DELIVERY DATE: {delivery_date}.")
        except:
            print("*****[CHECKOUT-SELF COLLECT] ERROR ON COLLECT IN STORE (SELF COLLECT) DELIVERY PAGE..*****")


    def test_someone_else_collect_in_store_guest(self):
        try:
            self.timeout(2000)
            self.click(Checkout_Delivery.collect_in_store_tab)
            self.timeout(2000)
            self.click(self.someone_else_collect_checkbox)
            self.timeout(1000)
            self.select_option(self.delivery_title_dropdown,self.delivery_title_value)
            self.fill(self.first_name_input, self.first_name_text)
            self.fill(self.last_name_input, self.last_name_text)
            self.fill(self.phone_input, self.phone_text)
            if self.is_checked(self.gift_checkbox):
                print("GIFT OPTION IS ALREADY SELECTED...")
            else:
                self.click(self.gift_checkbox)
            self.timeout(1000)
            self.fill(self.gift_message_input, self.gift_message_guest_someone_else_collect_text)
            self.timeout(1000)
            delivery_date = self.get_text(self.collect_in_store_delivery_date).strip()
            self.screenshot.take_page_screenshot("CHECKOUT_GUEST_SOMEONE_SELF_COLLECT")
            print(f"[CHECKOUT-GUEST-SOMEONE ELSE COLLECT] DELIVERY DATE: {delivery_date}")
        except:
            print(f"*****[CHECKOUT-GUEST-SOMEONE ELSE COLLECT] ERROR ON COLLECT IN STORE (SOMEONE ELSE COLLECT) DELIVERY PAGE..*****")


    def test_someone_else_collect_in_store_registered(self):
        try:
            self.timeout(2000)
            self.click(Checkout_Delivery.collect_in_store_tab)
            self.timeout(2000)
            self.click(self.someone_else_collect_checkbox)
            self.timeout(1000)
            self.select_option(self.delivery_title_dropdown,self.delivery_title_value)
            self.fill(self.first_name_input, self.first_name_text)
            self.fill(self.last_name_input, self.last_name_text)
            self.fill(self.phone_input, self.phone_text)
            if self.is_checked(self.gift_checkbox):
                print("GIFT OPTION IS ALREADY SELECTED...")
            else:
                self.click(self.gift_checkbox)
            self.timeout(1000)
            self.fill(self.gift_message_input, self.gift_message_registered_someone_else_collect_text)
            self.timeout(1000)
            delivery_date = self.get_text(self.collect_in_store_delivery_date).strip()
            self.screenshot.take_page_screenshot("CHECKOUT_REGISTERED_SOMEONE_SELF_COLLECT")
            print(f"[CHECKOUT-REGISTERED-SOMEONE ELSE COLLECT] DELIVERY DATE: {delivery_date}")
        except:
            print(f"*****[CHECKOUT-REGISTERED-SOMEONE ELSE COLLECT] ERROR ON COLLECT IN STORE (SOMEONE ELSE COLLECT) DELIVERY PAGE..*****")



    def test_client_service_tax_error_popup_as_guest(self):
        try:
            self.timeout(2000)
            self.click(Checkout_Delivery.premium_delivery_tab)
            self.timeout(2000)
            self.select_option(self.delivery_title_dropdown,self.delivery_title_value)
            self.fill(self.first_name_input,self.first_name_text)
            self.fill(self.last_name_input,self.last_name_text)
            self.fill(self.phone_input,self.phone_text)
            self.test_enter_invalid_new_delivery_address()
            if self.is_checked(self.gift_checkbox):
                print("GIFT OPTION IS ALREADY SELECTED...")
            else:
                self.click(self.gift_checkbox)
            self.timeout(1000)
            self.fill(self.gift_message_input, self.gift_message_guest_premium_text)
            self.timeout(2000)
        except:
            print("*****[CHECKOUT-PREMIUM] NOT ABLE TO ENTER DELIVERY ADDRESS INFO..*****")


    def test_client_service_tax_error_popup_as_register(self):
        try:
            self.timeout(2000)
            self.click(Checkout_Delivery.premium_delivery_tab)
            self.timeout(2000)
            self.select_option(self.delivery_title_dropdown,self.delivery_title_value)

            if self.is_checked(self.gift_checkbox):
                print("GIFT OPTION IS ALREADY SELECTED...")
            else:
                self.click(self.gift_checkbox)
            self.timeout(1000)
            self.fill(self.gift_message_input, self.gift_message_registered_premium_text)
            self.timeout(2000)
            self.test_add_new_address_as_register()

            self.fill(self.premium_address_input,self.premium_address_text)
            #State dropdown
            self.select_state_dropdown_value(self.premium_state_dropdown, self.premium_state_text)
            self.fill(self.premium_city_input,"TESTING")
            self.fill(self.premium_postal_code_input, "TESTING")
        except:
            print("*****[CHECKOUT-PREMIUM] NOT ABLE TO ENTER DELIVERY ADDRESS INFO..*****")

'''


