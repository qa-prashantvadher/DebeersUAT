import os
from pages.checkout_pdp_add_to_cart_page import Checkout_PDP_SPP_No_Size
from pages.checkout_login import Checkout_Login
from pages.checkout_delivery_page import Checkout_Delivery
from pages.checkout_payment_page import Checkout_Payment
from pages.checkout_review_page import Checkout_Review
from pages.login_pages import Login_Page
from pages.go_back_from_review_page import Checkout_Go_Back_From_Review
from dotenv import load_dotenv
import logging

load_dotenv(override=True)
logger = logging.getLogger(__name__)

ENV = os.getenv("ENVIRONMENT").upper()
COUNTRY = os.getenv("LOCALE").upper()
REFRESH = os.getenv("PAGE_REFRESH").upper()
ONETIME_LOGIN = os.getenv("CHECKOUT_ONETIME_LOGIN").upper()
TESTING_TYPE = os.getenv("TESTING_TYPE").upper()



def test_checkout_as_mixed_user(page):

    checkout_pdp = Checkout_PDP_SPP_No_Size(page)
    checkout_login = Checkout_Login(page)
    checkout_delivery = Checkout_Delivery(page)
    checkout_payment = Checkout_Payment(page)
    checkout_review = Checkout_Review(page)
    login_logout = Login_Page(page)
    checkout_back_from_review =  Checkout_Go_Back_From_Review(page)

    if COUNTRY == "UK" or COUNTRY == "US" or COUNTRY == "HK":

            print("----> TEST CASE 1 OF 4")
            # REGISTERED
            login_logout.test_login_from_header()
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_delivery.test_open_premium_delivery_tab()
            checkout_delivery.test_delivery_date_on_premium_delivery()
            checkout_delivery.test_enter_valid_delivery_address_in_premium_delivery()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_amex_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_back_from_review.test_go_back_to_shopping_cart_from_review_page()
            login_logout.test_logout_from_my_account_logout()
            # GUEST
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_guest_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_self_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_mastercard_credit_card_details()
            checkout_payment.test_enter_change_billing_address_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_review.test_place_an_order_from_order_review_page()

            print("----> TEST CASE 2 OF 4")
            # REGISTERED
            login_logout.test_login_from_header()
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_mastercard_credit_card_details()
            checkout_payment.test_enter_change_billing_address_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_back_from_review.test_go_back_to_shopping_cart_from_review_page()
            login_logout.test_logout_from_my_account_logout()
            # GUEST
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_guest_user()
            checkout_delivery.test_open_premium_delivery_tab()
            checkout_delivery.test_enter_user_details_in_premium_delivery()
            checkout_delivery.test_enter_valid_delivery_address_in_premium_delivery()
            checkout_delivery.test_delivery_date_on_premium_delivery()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_amex_credit_card_details()
            checkout_payment.test_enter_change_billing_address_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_review.test_place_an_order_from_order_review_page()

            print("----> TEST CASE 3 OF 4")
            #Pre Setup
            login_logout.test_login_from_header()
            login_logout.test_logout_from_my_account_logout()
            # GUEST
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_guest_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_self_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_payment.test_enter_change_billing_address_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_back_from_review.test_go_back_to_shopping_cart_from_review_page()
            # REGISTERED
            login_logout.test_login_from_header()
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_delivery.test_open_premium_delivery_tab()
            checkout_delivery.test_delivery_date_on_premium_delivery()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_discover_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_review.test_place_an_order_from_order_review_page()
            if ENV in ["UAT", "QA"]:
                login_logout.test_logout_from_order_confirmation_page()
            elif ENV == "PROD":
                login_logout.test_logout_from_my_account_logout()


            print("----> TEST CASE 4 OF 4")
            # GUEST
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_guest_user()
            checkout_delivery.test_open_premium_delivery_tab()
            checkout_delivery.test_enter_user_details_in_premium_delivery()
            checkout_delivery.test_enter_valid_delivery_address_in_premium_delivery()
            checkout_delivery.test_delivery_date_on_premium_delivery()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            checkout_payment.test_enter_change_billing_address_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_back_from_review.test_go_back_to_shopping_cart_from_review_page()
            # REGISTERED
            login_logout.test_login_from_header()
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_self_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_mastercard_credit_card_details()
            checkout_payment.test_enter_change_billing_address_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_review.test_place_an_order_from_order_review_page()
            if ENV in ["UAT", "QA"]:
                login_logout.test_logout_from_order_confirmation_page()
            elif ENV == "PROD":
                login_logout.test_logout_from_my_account_logout()

    else:
            logger.info(f"[{ENV}-{COUNTRY}] NO MIXED CHECKOUT CASES TO VERIFY..")