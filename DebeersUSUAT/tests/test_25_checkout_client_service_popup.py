from pages.checkout_pdp_add_to_cart_page import Checkout_PDP_SPP_No_Size
from pages.checkout_login import Checkout_Login
from pages.checkout_delivery_page import Checkout_Delivery
from pages.checkout_payment_page import Checkout_Payment
from pages.checkout_review_page import Checkout_Review
from pages.login_pages import Login_Page
import os
from dotenv import load_dotenv
load_dotenv(override=True)

env = os.getenv("ENVIRONMENT")

def test_checkout_client_service_popup(page):

    checkout_pdp = Checkout_PDP_SPP_No_Size(page)
    checkout_login = Checkout_Login(page)
    checkout_delivery = Checkout_Delivery(page)
    checkout_payment = Checkout_Payment(page)
    checkout_review = Checkout_Review(page)
    login_logout = Login_Page(page)


    # Case 1: As a Registered User + Premium Delivery > Invalid Address > Then Valid Address
    checkout_pdp.test_checkout_spp_no_size_with_engraving()
    checkout_pdp.test_checkout_spp_no_size_without_engraving()
    checkout_pdp.test_secure_checkout_from_minicart()
    checkout_login.test_checkout_as_registered_user()
    checkout_delivery.test_open_premium_delivery_tab()
    checkout_delivery.test_add_new_address_as_register()
    checkout_delivery.test_enter_invalid_delivery_address_in_premium_delivery()
    checkout_delivery.test_continue_to_payment_from_delivery_page()
    checkout_delivery.test_close_client_service_tax_error_popup()
    checkout_delivery.test_delivery_date_on_premium_delivery()
    checkout_delivery.test_enter_valid_delivery_address_in_premium_delivery()
    checkout_delivery.test_enter_gift_message()
    checkout_delivery.test_delivery_date_on_premium_delivery()
    checkout_delivery.test_continue_to_payment_from_delivery_page()
    checkout_payment.test_enter_amex_credit_card_details()
    checkout_payment.test_continue_to_review_from_payment_page()
    checkout_review.test_place_an_order_from_order_review_page()
    if env == "UAT":
        login_logout.test_logout_from_order_confirmation_page()

    # Case 2: As a Guest User + Premium Delivery > Invalid Address > Then Valid Address
    checkout_pdp.test_checkout_spp_no_size_with_engraving()
    checkout_pdp.test_checkout_spp_no_size_without_engraving()
    checkout_pdp.test_secure_checkout_from_minicart()
    checkout_login.test_checkout_as_guest_user()
    checkout_delivery.test_open_premium_delivery_tab()
    checkout_delivery.test_enter_user_details_in_premium_delivery()
    checkout_delivery.test_enter_invalid_delivery_address_in_premium_delivery()
    checkout_delivery.test_continue_to_payment_from_delivery_page()
    checkout_delivery.test_close_client_service_tax_error_popup()
    checkout_delivery.test_delivery_date_on_premium_delivery()
    checkout_delivery.test_enter_valid_delivery_address_in_premium_delivery()
    checkout_delivery.test_enter_gift_message()
    checkout_delivery.test_delivery_date_on_premium_delivery()
    checkout_delivery.test_continue_to_payment_from_delivery_page()
    checkout_payment.test_enter_mastercard_credit_card_details()
    checkout_payment.test_continue_to_review_from_payment_page()
    checkout_review.test_place_an_order_from_order_review_page()
    if env == "UAT":
        login_logout.test_logout_from_order_confirmation_page()

