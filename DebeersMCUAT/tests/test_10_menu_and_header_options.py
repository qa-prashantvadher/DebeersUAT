from pages.open_website import OpenHomePage
from pages.client_services_page import Client_Services_Page
from pages.book_appointment import Book_Appointment
from pages.store_locator import Search_Locator_Page
from pages.menu_header_options import Open_Menu_Header_Options

'''
TEST SCENARIOS:

AREA COVERED: MEGA MENU AND HEADER SECTION.

- Open Debeers UK Website.
- Open Mega Menu
    - Open and then Close Store Locator page.
    - Open Book an Appointment page.
        - Select all options with In Store Appointment type.
        - Select all options with Virtual Appointment type.
    - Open Delivery & Returns page.
    - Open Client Services page.
        - Select all regions.
    - Open Location and Language section.
        - Change Languages.
        - Change Locations.    
'''

def test_menu_and_header_option_pages(page):

    menu_header_option = Open_Menu_Header_Options(page)
    store_locator = Search_Locator_Page(page)
    client_service = Client_Services_Page(page)
    book_appointment = Book_Appointment(page)
    home_page = OpenHomePage(page)

    # OPEN DEBEERS WEBSITE
    home_page.test_navigate_to_url()
    home_page.test_cookie_consent()
    home_page.test_country_selector()
    home_page.test_email_subscription_popup()

'''
    #OPEN MENU OPTIONS
    menu_header_option.test_open_locate_a_store_page_from_menu()
    store_locator.test_close_store_locator_page()
    menu_header_option.test_open_delivery_returns_page_from_menu()
    menu_header_option.test_open_contact_us_from_menu()
    client_service.test_change_region_client_service()
    menu_header_option.test_change_country_menu()
'''