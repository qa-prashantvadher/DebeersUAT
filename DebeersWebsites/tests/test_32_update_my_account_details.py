from pages.login_pages import Login_Page
from pages.update_my_account_details import Update_My_Account_Page


def test_update_my_account_details_functionality(page):

    login_logout = Login_Page(page)
    update_my_account_details = Update_My_Account_Page(page)
    print("----> TEST CASE 1 OF 2")
    login_logout.test_login_from_header()
    update_my_account_details.test_open_edit_my_account_page()
    update_my_account_details.test_update_my_account_details()
    print("----> TEST CASE 2 OF 2")
    update_my_account_details.test_open_address_book()
    update_my_account_details.test_remove_all_saved_addresses()
    login_logout.test_logout_from_my_account_logout()
