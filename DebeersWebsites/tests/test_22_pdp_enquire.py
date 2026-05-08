from pages.client_services_page import Client_Services_Page
from pages.pdp_enquire_appointment import PDP_Enquire_Book_Appointment
from dotenv import load_dotenv
import os

load_dotenv(override=True)
ENV = os.getenv("ENVIRONMENT").upper()
COUNTRY = os.getenv("LOCALE").upper()

def test_pdp_enquire_cta(page):

    pdp_enquire_appointment = PDP_Enquire_Book_Appointment(page)
    client_service = Client_Services_Page(page)

    # ENQUIRE ONLINE/ENQUIRE/EMAIL US OPTIONS ON THE PDP PAGE
    print("----> TEST CASE 1 OF 5")
    pdp_enquire_appointment.test_enquire_old_master_level()
    if ENV != "PROD":
        client_service.test_email_us_form()
        client_service.test_open_call_request_form_email_call()
        client_service.test_callback_form()
        client_service.test_close_callback_form()

    print("----> TEST CASE 2 OF 5")
    pdp_enquire_appointment.test_contact_us_old_master_level()

    print("----> TEST CASE 3 OF 5")
    pdp_enquire_appointment.test_enquire_hj_master_level()

    print("----> TEST CASE 4 OF 5")
    pdp_enquire_appointment.test_enquire_online_bb_upp_variant_level()
    if ENV != "PROD":
        client_service.test_email_us_form()
        client_service.test_open_call_request_form_email_call()
        client_service.test_callback_form()
        client_service.test_open_faq_from_email_call()

    print("----> TEST CASE 5 OF 5")
    pdp_enquire_appointment.test_email_us_bb_contact_us()
    client_service.test_open_book_an_appointment_from_email_call()
