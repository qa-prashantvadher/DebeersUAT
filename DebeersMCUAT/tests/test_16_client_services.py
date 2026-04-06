from pages.client_services_page import Client_Services_Page
from pages.book_appointment import Book_Appointment
from pages.menu_header_options import Open_Menu_Header_Options


'''
- Header Section
    - Open Client Services page.   
'''
def test_client_services_page(page):

    client_service = Client_Services_Page(page)
    menu_header_option = Open_Menu_Header_Options(page)
    book_appointment = Book_Appointment(page)

    # EMAIL US FORM ON THE CLIENT SERVICES PAGE
    menu_header_option.test_open_contact_us_from_header()
    client_service.test_open_email_us_form_from_client_services()
    client_service.test_email_us_form()
    client_service.test_open_call_request_form_email_call()
    client_service.test_callback_form()
    client_service.test_close_callback_form()

    client_service.test_open_email_us_form_from_client_services()
    client_service.test_open_call_request_form_email_call()
    client_service.test_callback_form()
    client_service.test_close_callback_form()

    client_service.test_open_email_us_form_from_client_services()
    client_service.test_open_book_an_appointment_from_email_call()
    book_appointment.test_in_store_appointment_type()

    menu_header_option.test_open_contact_us_from_header()
    client_service.test_open_email_us_form_from_client_services()
    client_service.test_open_faq_from_email_call()
    menu_header_option.test_open_contact_us_from_header()

    # CALL REQUEST FORM ON THE CLIENT SERVICES PAGE
    client_service.test_open_callback_form_from_client_services()
    client_service.test_callback_form()
    client_service.test_open_email_us_form_from_email_call()
    client_service.test_email_us_form()
    client_service.test_close_email_us_form()

    client_service.test_open_callback_form_from_client_services()
    client_service.test_open_email_us_form_from_email_call()
    client_service.test_email_us_form()
    client_service.test_close_email_us_form()

    client_service.test_open_callback_form_from_client_services()
    client_service.test_open_book_an_appointment_from_email_call()
    book_appointment.test_in_store_appointment_type()

    menu_header_option.test_open_contact_us_from_header()
    client_service.test_open_callback_form_from_client_services()
    client_service.test_open_faq_from_email_call()
    menu_header_option.test_open_contact_us_from_header()