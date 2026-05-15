from pages.login_pages import Login_Page
from pages.book_appointment import Book_Appointment
from pages.menu_header_options import Open_Menu_Header_Options

from dotenv import load_dotenv
import os
load_dotenv(override=True)

ENV = os.getenv("ENVIRONMENT").upper()
COUNTRY = os.getenv("LOCALE").upper()

def test_login_logout_functionality(page):

    login_logout = Login_Page(page)
    book_appointment = Book_Appointment(page)
    menu_header_option = Open_Menu_Header_Options(page)

    print("----> TEST CASE 1 OF 5")
    login_logout.test_login_from_header()
    login_logout.test_logout_from_my_account_logout()
    print("----> TEST CASE 2 OF 5")
    login_logout.test_login_from_cart()
    login_logout.test_logout_from_my_account_not_you()
    print("----> TEST CASE 3 OF 5")
    login_logout.test_login_from_register()
    login_logout.test_logout_from_my_account_logout()
    print("----> TEST CASE 4 OF 5")
    login_logout.test_login_from_wishlist()
    login_logout.test_logout_from_my_account_not_you()
    print("----> TEST CASE 5 OF 5")
    if COUNTRY != "MO" and COUNTRY != "CA":
        menu_header_option.test_open_book_appointment_page_from_menu()
        book_appointment.test_in_store_appointment_type()
        book_appointment.test_step1_select_date_time()
        book_appointment.test_click_on_continue_cta()
        login_logout.test_login_from_book_appointment()
        book_appointment.test_click_on_continue_cta()
        book_appointment.test_step3_enter_additional_information()
        book_appointment.test_step3_select_checkboxes()
        if ENV == "QA" or ENV == "UAT":
            book_appointment.test_click_on_submit_cta()
        login_logout.test_logout_from_my_account_not_you()

