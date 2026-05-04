from pages.pdp_enquire_appointment import PDP_Enquire_Book_Appointment
from pages.book_appointment import Book_Appointment
from dotenv import load_dotenv
import os
load_dotenv(override=True)

ENV = os.getenv("ENVIRONMENT").upper()
COUNTRY = os.getenv("LOCALE").upper()


def test_book_appointment_cta_from_pdp(page):

    pdp_enquire_appointment = PDP_Enquire_Book_Appointment(page)
    book_appointment = Book_Appointment(page)

    # BOOK APPOINTMENT CTA AND BOOK IN STORE/VIRTUAL APPOINTMENT OPTIONS ON THE PDP PAGE
    pdp_enquire_appointment.test_book_appointment_hj_master_level()

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
        pdp_enquire_appointment.test_book_appointment_hj_master_level()
        book_appointment.test_virtual_appointment_type()
        book_appointment.test_step1_select_date_time()
        book_appointment.test_click_on_continue_cta()
        book_appointment.test_step2_enter_contact_details()
        book_appointment.test_click_on_continue_cta()
        book_appointment.test_step3_enter_additional_information()
        book_appointment.test_step3_select_checkboxes()
        if ENV == "QA" or ENV == "UAT":
            book_appointment.test_click_on_submit_cta()

    pdp_enquire_appointment.test_in_store_appointment_bb_contact_us()
    book_appointment.test_bb_in_store_appointment_type()
    book_appointment.test_step1_select_date_time()
    book_appointment.test_click_on_continue_cta()
    book_appointment.test_step2_enter_contact_details()
    book_appointment.test_click_on_continue_cta()
    book_appointment.test_step3_enter_additional_information()
    book_appointment.test_step3_select_checkboxes()
    if ENV == "QA" or ENV == "UAT":
        book_appointment.test_click_on_submit_cta()

    if (ENV == "QA") and (COUNTRY == "UK" or COUNTRY == "US"):
        pdp_enquire_appointment.test_virtual_appointment_bb_contact_us()
        book_appointment.test_bb_virtual_appointment_type()
        book_appointment.test_step1_select_date_time()
        book_appointment.test_click_on_continue_cta()
        book_appointment.test_step2_enter_contact_details()
        book_appointment.test_click_on_continue_cta()
        book_appointment.test_step3_enter_additional_information()
        book_appointment.test_step3_select_checkboxes()
        if ENV == "QA" or ENV == "UAT":
            book_appointment.test_click_on_submit_cta()
