from pages.store_locator import Search_Locator_Page
from pages.book_appointment import Book_Appointment
from dotenv import load_dotenv
import os

load_dotenv(override=True)
ENV = os.getenv("ENVIRONMENT")


def test_store_locator_page(page):

    store_locator = Search_Locator_Page(page)
    book_appointment = Book_Appointment(page)

    # STORE LOCATOR PAGE
    store_locator.test_open_store_locator_page_from_header()
    store_locator.test_show_all_show_list_store()

    store_locator.test_search_store_by_keyword("UNITED KINGDOM")
    store_locator.test_click_close_london_marker_in_map()

    store_locator.test_search_store_by_keyword("US")
    store_locator.test_search_store_by_keyword("INVALID KEYWORD")

    store_locator.test_search_store_by_keyword("PARIS")
    store_locator.test_open_paris_store_detail_page()
    store_locator.test_click_close_paris_flagship_in_map()
    store_locator.test_book_an_appointment_cta_store_detail_page()

    store_locator.test_open_store_locator_page_from_header()

    store_locator.test_search_store_by_keyword("LONDON")
    store_locator.test_click_close_london_marker_in_map()
    store_locator.test_open_london_store_detail_page()
    store_locator.test_click_close_london_marker_in_map()
    if ENV == "PROD":
        store_locator.test_book_an_appointment_cta_store_detail_page()
        book_appointment.test_in_store_appointment_type()
    else:
        store_locator.test_book_an_appointment_cta_store_detail_page()
        book_appointment.test_in_store_appointment_type()
        book_appointment.test_virtual_appointment_type()

    store_locator.test_open_store_locator_page_from_header()

    store_locator.test_search_store_by_keyword("10065")
    store_locator.test_open_new_york_store_detail_page()
    store_locator.test_click_close_new_york_madison_avenue_in_map()
    store_locator.test_book_an_appointment_cta_store_detail_page()


    store_locator.test_open_store_locator_page_from_header()
    store_locator.test_close_store_locator_page()
