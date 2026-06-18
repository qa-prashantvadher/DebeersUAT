from pages.store_locator import Search_Locator_Page
from pages.footer_page import Footer_Page
from pages.faq_page import FAQ_Page
from dotenv import load_dotenv
import os

load_dotenv(override=True)
ENV = os.getenv("ENVIRONMENT").upper()
COUNTRY = os.getenv("LOCALE").upper()

'''
TEST SCENARIOS:

AREA COVERED: FOOTER SECTION.

- Footer > Client Services
    - Open and then Close Store Locator page.
    - Open Book an Appointment page.
    - Open Delivery & Returns page.
    - Open Client Services page.
    - Open FAQ page.
    - Open Location dropdown and Change Locations.
    - Open Language dropdown and Change Languages.
'''
def test_footer_section(page):

    store_locator = Search_Locator_Page(page)
    footer_section = Footer_Page(page)
    faq_section  = FAQ_Page(page)

    if COUNTRY == "MO" or COUNTRY == "CA":
        print("----> TEST CASE 1 OF 6")
        footer_section.test_delivery_returns_link_from_footer()
        print("----> TEST CASE 2 OF 6")
        footer_section.test_contact_us_link_from_footer()
        print("----> TEST CASE 3 OF 6")
        footer_section.test_faq_link_from_footer()
        faq_section.test_all_faq_categories()
        print("----> TEST CASE 4 OF 6")
        footer_section.test_news_letter_from_footer()
        print("----> TEST CASE 5 OF 6")
        footer_section.test_select_country_records_from_location_footer()
        print("----> TEST CASE 6 OF 6")
        footer_section.test_select_language_records_from_language_footer()
    else:
        # FOOTER SECTION
        print("----> TEST CASE 1 OF 8")
        footer_section.test_locate_a_store_link_from_footer()
        store_locator.test_close_store_locator_page()
        print("----> TEST CASE 2 OF 8")
        footer_section.test_book_an_appointment_link_from_footer()
        print("----> TEST CASE 3 OF 8")
        footer_section.test_delivery_returns_link_from_footer()
        print("----> TEST CASE 4 OF 8")
        footer_section.test_contact_us_link_from_footer()
        print("----> TEST CASE 5 OF 8")
        footer_section.test_faq_link_from_footer()
        faq_section.test_all_faq_categories()
        print("----> TEST CASE 6 OF 8")
        footer_section.test_news_letter_from_footer()
        print("----> TEST CASE 7 OF 8")
        #footer_section.test_select_country_records_from_location_footer()
        print("----> TEST CASE 8 OF 8")
        #footer_section.test_select_language_records_from_language_footer()