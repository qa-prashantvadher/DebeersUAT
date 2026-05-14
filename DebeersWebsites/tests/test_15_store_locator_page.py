from pages.store_locator import Search_Locator_Page
from pages.book_appointment import Book_Appointment
from dotenv import load_dotenv
import os

load_dotenv(override=True)
ENV = os.getenv("ENVIRONMENT").upper()
COUNTRY = os.getenv("LOCALE").upper()

def test_store_locator_page(page):

    store_locator = Search_Locator_Page(page)
    book_appointment = Book_Appointment(page)

    # STORE LOCATOR PAGE
    print("----> TEST CASE 1 OF 8")
    store_locator.test_open_store_locator_page_from_header()
    store_locator.test_show_all_show_list_store()

    store_locator.test_search_store_by_keyword("UNITED KINGDOM")
    store_locator.test_click_close_london_marker_in_map()

    print("----> TEST CASE 2 OF 8")
    store_locator.test_search_store_by_keyword("US")

    print("----> TEST CASE 3 OF 8")
    store_locator.test_search_store_by_keyword("INVALID KEYWORD")

    print("----> TEST CASE 4 OF 8")
    store_locator.test_search_store_by_keyword("PARIS")
    store_locator.test_open_paris_store_detail_page()
    store_locator.test_click_close_paris_flagship_in_map()
    store_locator.test_book_an_appointment_cta_store_detail_page()

    print("----> TEST CASE 5 OF 8")
    store_locator.test_open_store_locator_page_from_header()
    store_locator.test_search_store_by_keyword("HONG KONG")

    print("----> TEST CASE 6 OF 8")
    store_locator.test_search_store_by_keyword("LONDON")
    store_locator.test_click_close_london_marker_in_map()
    store_locator.test_open_london_store_detail_page()
    store_locator.test_click_close_london_marker_in_map()

    if COUNTRY != "MO":
        store_locator.test_book_an_appointment_cta_store_detail_page()
        book_appointment.test_in_store_appointment_type()
        book_appointment.test_step1_select_date_time()
        book_appointment.test_click_on_continue_cta()
        book_appointment.test_step2_enter_contact_details()
        book_appointment.test_click_on_continue_cta()
        book_appointment.test_step3_enter_additional_information()
        book_appointment.test_step3_select_checkboxes()
        if ENV == "QA" or ENV == "UAT":
            book_appointment.test_click_on_submit_cta()

        if (ENV == "QA") and (COUNTRY == "UK" or COUNTRY == "US"):
            book_appointment.test_virtual_appointment_type()
            book_appointment.test_step1_select_date_time()
            book_appointment.test_click_on_continue_cta()
            book_appointment.test_step2_enter_contact_details()
            book_appointment.test_click_on_continue_cta()
            book_appointment.test_step3_enter_additional_information()
            book_appointment.test_step3_select_checkboxes()
            if ENV == "QA" or ENV == "UAT":
                book_appointment.test_click_on_submit_cta()

    print("----> TEST CASE 7 OF 8")
    store_locator.test_open_store_locator_page_from_header()

    store_locator.test_search_store_by_keyword("10065")
    store_locator.test_open_new_york_store_detail_page()
    store_locator.test_click_close_new_york_madison_avenue_in_map()
    if COUNTRY != "MO":
        store_locator.test_book_an_appointment_cta_store_detail_page()

    print("----> TEST CASE 8 OF 8")
    store_locator.test_open_store_locator_page_from_header()
    store_locator.test_close_store_locator_page()
