from pages.login_pages import Login_Page


def test_login_logout_functionality(page):

    login_logout = Login_Page(page)

    login_logout.test_login_from_header()
    login_logout.test_logout_from_my_account_logout()
    login_logout.test_login_from_cart()
    login_logout.test_logout_from_my_account_not_you()
    login_logout.test_login_from_register()
    login_logout.test_logout_from_my_account_logout()
    login_logout.test_login_from_wishlist()
    login_logout.test_logout_from_my_account_not_you()

