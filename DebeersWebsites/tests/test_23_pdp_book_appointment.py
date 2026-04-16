from pages.pdp_enquire_appointment import PDP_Enquire_Book_Appointment
from pages.book_appointment import Book_Appointment
from dotenv import load_dotenv
import os
load_dotenv(override=True)

ENV = os.getenv("ENVIRONMENT")
COUNTRY = os.getenv("LOCALE")


def test_book_appointment_cta_from_pdp(page):

    pdp_enquire_appointment = PDP_Enquire_Book_Appointment(page)
    book_appointment = Book_Appointment(page)

    # BOOK APPOINTMENT CTA AND BOOK IN STORE/VIRTUAL APPOINTMENT OPTIONS ON THE PDP PAGE
    pdp_enquire_appointment.test_book_appointment_hj_master_level()

    if ENV == "PROD" or COUNTRY == "FR" or COUNTRY == "HK":
        book_appointment.test_in_store_appointment_type()
        pdp_enquire_appointment.test_book_appointment_hj_master_level()
        book_appointment.test_in_store_appointment_type()
        pdp_enquire_appointment.test_in_store_appointment_bb_contact_us()
        book_appointment.test_bb_in_store_appointment_type()
    else:
        book_appointment.test_in_store_appointment_type()
        pdp_enquire_appointment.test_book_appointment_hj_master_level()
        book_appointment.test_virtual_appointment_type()
        pdp_enquire_appointment.test_in_store_appointment_bb_contact_us()
        book_appointment.test_bb_in_store_appointment_type()
        pdp_enquire_appointment.test_virtual_appointment_bb_contact_us()
        book_appointment.test_bb_virtual_appointment_type()
