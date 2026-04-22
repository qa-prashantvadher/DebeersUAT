import os
from pages.checkout_pdp_add_to_cart_page import Checkout_PDP_SPP_No_Size
from pages.checkout_login import Checkout_Login
from pages.checkout_delivery_page import Checkout_Delivery
from pages.checkout_payment_page import Checkout_Payment
from pages.checkout_review_page import Checkout_Review
from pages.login_pages import Login_Page
from pages.shopping_cart_page import Open_Shopping_Cart_Page
from pages.go_back_from_payment_page import Checkout_Go_Back_From_Payment
from pages.go_back_from_review_page import Checkout_Go_Back_From_Review
from dotenv import load_dotenv
load_dotenv(override=True)

ENV = os.getenv("ENVIRONMENT").upper()
COUNTRY = os.getenv("LOCALE").upper()
REFRESH = os.getenv("PAGE_REFRESH").upper()
ONETIME_LOGIN = os.getenv("CHECKOUT_ONETIME_LOGIN").upper()
TESTING_TYPE = os.getenv("TESTING_TYPE").upper()



def test_checkout_as_registered_user_someone_else_collect(page):

    checkout_pdp = Checkout_PDP_SPP_No_Size(page)
    checkout_login = Checkout_Login(page)
    checkout_delivery = Checkout_Delivery(page)
    checkout_payment = Checkout_Payment(page)
    checkout_review = Checkout_Review(page)
    login_logout = Login_Page(page)
    shopping_cart = Open_Shopping_Cart_Page(page)
    checkout_back_from_payment = Checkout_Go_Back_From_Payment(page)
    checkout_back_from_review =  Checkout_Go_Back_From_Review(page)

    if (COUNTRY == "UK" or COUNTRY == "US" or COUNTRY == "HK") and TESTING_TYPE == "REGRESSION":

            print(" Case 5: Someone Else Collect + Discover card")
            checkout_pdp.test_checkout_spp_no_size_without_engraving()
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_discover_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                            login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                            login_logout.test_logout_from_my_account_logout()

            print(" Case 12: Someone Else Collect + Visa card > From the Payment page, Go back to the Delivery Page > Someone Else Collect + Union Pay card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_back_from_payment.test_go_back_to_delivery_from_payment_page()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                            login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                            login_logout.test_logout_from_my_account_logout()

            print(" Case 13: Someone Else Collect + Visa card > From the Payment page, Go back to the Delivery Page > Change delivery method to Premium Delivery + Union Pay card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_back_from_payment.test_go_back_to_delivery_from_payment_page()
            checkout_delivery.test_open_premium_delivery_tab()
            checkout_delivery.test_delivery_date_on_premium_delivery()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            checkout_payment.test_use_delivery_as_billing_address_checkbox()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                        login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                        login_logout.test_logout_from_my_account_logout()

            print(" Case 14: Someone Else Collect + Visa card > From the Payment page, Go back to the Delivery Page > Change delivery method to Self Collect + Union Pay card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_back_from_payment.test_go_back_to_delivery_from_payment_page()
            checkout_delivery.test_select_self_collect_checkbox()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                        login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                        login_logout.test_logout_from_my_account_logout()

            print(" Case 21: Someone Else Collect + Union Pay card > From the Review page, Go back to the Delivery Page > Someone Else Collect + Visa card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            checkout_payment.test_enter_change_billing_name_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_back_from_review.test_go_back_to_delivery_from_review_page()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                        login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                        login_logout.test_logout_from_my_account_logout()

            print(" Case 22: Someone Else Collect + Union Pay card > From the Review page, Go back to the Delivery Page > Change delivery method to Premium Delivery + Visa card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            checkout_payment.test_enter_change_billing_name_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_back_from_review.test_go_back_to_delivery_from_review_page()
            checkout_delivery.test_open_premium_delivery_tab()
            checkout_delivery.test_delivery_date_on_premium_delivery()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                        login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                        login_logout.test_logout_from_my_account_logout()

            print(" Case 23: Someone Else Collect + Union Pay card > From the Review page, Go back to the Delivery Page > Change delivery method to Self Collect + Visa card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_back_from_review.test_go_back_to_delivery_from_review_page()
            checkout_delivery.test_select_self_collect_checkbox()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                        login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                        login_logout.test_logout_from_my_account_logout()

            print(" Case 28: Someone Else Collect + Discover card > From the Review page, Go back to the Payment Page > Visa card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_discover_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_back_from_review.test_go_back_to_payment_from_review_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                        login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                        login_logout.test_logout_from_my_account_logout()

            print(" Case 35: Someone Else Collect + Union Pay card > From the Review page, Go back to the Cart Page > Someone Else Collect + Visa card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_back_from_review.test_go_back_to_shopping_cart_from_review_page()
            shopping_cart.test_continue_to_checkout_from_cart()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                        login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                        login_logout.test_logout_from_my_account_logout()

            print(" Case 36: Someone Else Collect + Union Pay card > From the Review page, Go back to the Cart Page > Change delivery method to Premium Delivery + Visa card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_back_from_review.test_go_back_to_shopping_cart_from_review_page()
            shopping_cart.test_continue_to_checkout_from_cart()
            checkout_delivery.test_open_premium_delivery_tab()
            checkout_delivery.test_delivery_date_on_premium_delivery()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                        login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                        login_logout.test_logout_from_my_account_logout()

            print(" Case 37: Someone Else Collect + Union Pay card > From the Review page, Go back to the Cart Page > Change delivery method to Self Collect + Visa card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            checkout_payment.test_enter_change_billing_name_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_back_from_review.test_go_back_to_shopping_cart_from_review_page()
            shopping_cart.test_continue_to_checkout_from_cart()
            checkout_delivery.test_select_self_collect_checkbox()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                        login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                        login_logout.test_logout_from_my_account_logout()

            print(" Case 42: Someone Else Collect + Discover card > From the Payment page, Go back to the Cart Page > Someone Else Collect + Visa card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_back_from_payment.test_go_back_to_shopping_cart_from_payment_page()
            shopping_cart.test_continue_to_checkout_from_cart()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_payment.test_enter_change_billing_name_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                        login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                        login_logout.test_logout_from_my_account_logout()

            print(" Case 43: Someone Else Collect + Union Pay card > From the Payment page, Go back to the Cart Page > Change delivery method to Premium Delivery + Visa card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            checkout_back_from_payment.test_go_back_to_shopping_cart_from_payment_page()
            shopping_cart.test_continue_to_checkout_from_cart()
            checkout_delivery.test_open_premium_delivery_tab()
            checkout_delivery.test_delivery_date_on_premium_delivery()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ENV in ["UAT", "QA"]:
                login_logout.test_logout_from_order_confirmation_page()
            elif ENV == "PROD":
                login_logout.test_logout_from_my_account_logout()

    elif (COUNTRY == "UK" or COUNTRY == "US" or COUNTRY == "HK") and TESTING_TYPE == "SMOKE":

            print(" Case 5: Someone Else Collect + Discover card")
            checkout_pdp.test_checkout_spp_no_size_without_engraving()
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_discover_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                            login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                            login_logout.test_logout_from_my_account_logout()

            print(" Case 12: Someone Else Collect + Visa card > From the Payment page, Go back to the Delivery Page > Someone Else Collect + Union Pay card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_back_from_payment.test_go_back_to_delivery_from_payment_page()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                            login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                            login_logout.test_logout_from_my_account_logout()

            print(" Case 21: Someone Else Collect + Union Pay card > From the Review page, Go back to the Delivery Page > Someone Else Collect + Visa card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            checkout_payment.test_enter_change_billing_name_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_back_from_review.test_go_back_to_delivery_from_review_page()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                        login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                        login_logout.test_logout_from_my_account_logout()

            print(" Case 28: Someone Else Collect + Discover card > From the Review page, Go back to the Payment Page > Visa card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_discover_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_back_from_review.test_go_back_to_payment_from_review_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                        login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                        login_logout.test_logout_from_my_account_logout()

            print(" Case 35: Someone Else Collect + Union Pay card > From the Review page, Go back to the Cart Page > Someone Else Collect + Visa card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_back_from_review.test_go_back_to_shopping_cart_from_review_page()
            shopping_cart.test_continue_to_checkout_from_cart()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ONETIME_LOGIN == "NO":
                    if ENV in ["UAT", "QA"]:
                        login_logout.test_logout_from_order_confirmation_page()
                    elif ENV == "PROD":
                        login_logout.test_logout_from_my_account_logout()

            print(" Case 42: Someone Else Collect + Discover card > From the Payment page, Go back to the Cart Page > Someone Else Collect + Visa card")
            checkout_pdp.test_checkout_spp_no_size_with_engraving()
            checkout_pdp.test_secure_checkout_from_minicart()
            checkout_login.test_checkout_as_registered_user()
            checkout_delivery.test_open_collect_in_store_tab()
            checkout_delivery.test_select_someone_else_collect_checkbox()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_enter_gift_message()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_union_pay_credit_card_details()
            if REFRESH == "YES":
                    checkout_review.test_page_refresh()
            checkout_back_from_payment.test_go_back_to_shopping_cart_from_payment_page()
            shopping_cart.test_continue_to_checkout_from_cart()
            checkout_delivery.test_enter_collector_details_in_store_collect()
            checkout_delivery.test_delivery_date_on_collect_in_store()
            checkout_delivery.test_continue_to_payment_from_delivery_page()
            checkout_payment.test_enter_visa_credit_card_details()
            checkout_payment.test_enter_change_billing_name_details()
            checkout_payment.test_continue_to_review_from_payment_page()
            checkout_review.test_place_an_order_from_order_review_page()
            if ENV in ["UAT", "QA"]:
                login_logout.test_logout_from_order_confirmation_page()
            elif ENV == "PROD":
                login_logout.test_logout_from_my_account_logout()

    elif COUNTRY == "FR":
        print(f"[{ENV}-{COUNTRY}] NO CASES RELATED TO THE COLLECT IN STORE TAB..")