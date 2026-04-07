from pages.client_services_page import Client_Services_Page
from pages.pdp_enquire_appointment import PDP_Enquire_Book_Appointment

def test_pdp_enquire_cta(page):

    pdp_enquire_appointment = PDP_Enquire_Book_Appointment(page)
    client_service = Client_Services_Page(page)

    # ENQUIRE ONLINE/ENQUIRE/EMAIL US OPTIONS ON THE PDP PAGE
    # EMAIL US AND CALL REQUEST FORMS ON THE CLIENT SERVICES PAGE
    pdp_enquire_appointment.test_enquire_old_master_level()
    client_service.test_email_us_form()
    client_service.test_open_call_request_form_email_call()
    client_service.test_callback_form()
    client_service.test_close_callback_form()

    pdp_enquire_appointment.test_contact_us_old_master_level()

    pdp_enquire_appointment.test_enquire_hj_master_level()

    pdp_enquire_appointment.test_enquire_online_bb_upp_variant_level()
    client_service.test_email_us_form()
    client_service.test_open_call_request_form_email_call()
    client_service.test_callback_form()
    client_service.test_open_faq_from_email_call()

    pdp_enquire_appointment.test_email_us_bb_contact_us()
    client_service.test_open_book_an_appointment_from_email_call()
