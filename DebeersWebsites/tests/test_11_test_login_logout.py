from pages.login_pages import Login_Page


def test_login_logout_functionality(page):

    login_logout = Login_Page(page)

    print("----> TEST CASE 1 OF 4")
    login_logout.test_login_from_header()
    login_logout.test_logout_from_my_account_logout()
    print("----> TEST CASE 2 OF 4")
    login_logout.test_login_from_cart()
    login_logout.test_logout_from_my_account_not_you()
    print("----> TEST CASE 3 OF 4")
    login_logout.test_login_from_register()
    login_logout.test_logout_from_my_account_logout()
    print("----> TEST CASE 4 OF 4")
    login_logout.test_login_from_wishlist()
    login_logout.test_logout_from_my_account_not_you()

