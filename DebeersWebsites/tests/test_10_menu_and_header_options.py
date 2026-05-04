from pages.client_services_page import Client_Services_Page
from pages.book_appointment import Book_Appointment
from pages.store_locator import Search_Locator_Page
from pages.menu_header_options import Open_Menu_Header_Options
from dotenv import load_dotenv
import os

load_dotenv(override=True)
ENV = os.getenv("ENVIRONMENT").upper()
COUNTRY = os.getenv("LOCALE").upper()

def test_menu_and_header_option_pages(page):

    menu_header_option = Open_Menu_Header_Options(page)
    store_locator = Search_Locator_Page(page)
    client_service = Client_Services_Page(page)
    book_appointment = Book_Appointment(page)

    #OPEN MENU OPTIONS
    menu_header_option.test_open_locate_a_store_page_from_menu()
    store_locator.test_close_store_locator_page()

    menu_header_option.test_open_book_appointment_page_from_menu()
    book_appointment.test_in_store_appointment_type()
    # Step-1
    book_appointment.test_step1_select_date_time()
    book_appointment.test_click_on_continue_cta()
    # Step-2
    book_appointment.test_step2_enter_contact_details()
    book_appointment.test_go_back_to_step_1_with_edit_icon()
    # Step-1
    book_appointment.test_click_on_continue_cta()
    # Step-2
    book_appointment.test_click_on_continue_cta()
    # Step-3
    book_appointment.test_step3_enter_additional_information()
    book_appointment.test_step3_select_checkboxes()
    book_appointment.test_go_back_to_step_2_with_back_button()
    # Step-2
    book_appointment.test_go_back_to_step_1_with_back_button()
    # Step-1
    book_appointment.test_click_on_continue_cta()
    # Step -2
    book_appointment.test_click_on_continue_cta()
    # Step-3
    book_appointment.test_go_back_to_step_2_with_edit_icon()
    # Step-2
    book_appointment.test_click_on_continue_cta()
    # Step-3
    book_appointment.test_go_back_to_step_1_with_edit_icon()
    # Step-1
    book_appointment.test_click_on_continue_cta()
    # Step-2
    book_appointment.test_click_on_continue_cta()
    # Step-3
    if ENV == "QA" or ENV == "UAT":
        book_appointment.test_click_on_submit_cta()


    if (ENV == "QA") and (COUNTRY == "UK" or COUNTRY == "US"):
        menu_header_option.test_open_book_appointment_page_from_menu()
        book_appointment.test_virtual_appointment_type()
        # Step-1
        book_appointment.test_step1_select_date_time()
        book_appointment.test_click_on_continue_cta()
        # Step-2
        book_appointment.test_step2_enter_contact_details()
        book_appointment.test_go_back_to_step_1_with_edit_icon()
        # Step-1
        book_appointment.test_click_on_continue_cta()
        # Step-2
        book_appointment.test_click_on_continue_cta()
        # Step-3
        book_appointment.test_step3_enter_additional_information()
        book_appointment.test_step3_select_checkboxes()
        book_appointment.test_go_back_to_step_2_with_back_button()
        # Step-2
        book_appointment.test_go_back_to_step_1_with_back_button()
        # Step-1
        book_appointment.test_click_on_continue_cta()
        #Step -2
        book_appointment.test_click_on_continue_cta()
        # Step-3
        book_appointment.test_go_back_to_step_2_with_edit_icon()
        # Step-2
        book_appointment.test_click_on_continue_cta()
        # Step-3
        book_appointment.test_go_back_to_step_1_with_edit_icon()
        # Step-1
        book_appointment.test_click_on_continue_cta()
        # Step-2
        book_appointment.test_click_on_continue_cta()
        # Step-3
        if ENV == "QA" or ENV == "UAT":
            book_appointment.test_click_on_submit_cta()

    menu_header_option.test_open_delivery_returns_page_from_menu()
    menu_header_option.test_open_contact_us_from_menu()
    client_service.test_change_region_client_service()
    menu_header_option.test_change_language_menu()
    menu_header_option.test_change_country_menu()
