from pages.menu_header_options import Open_Menu_Header_Options
from pages.wishlist_add_remove import AddRemoveWishlist
from pages.search_slp_pdp import SearchSKU
from pages.open_plp_page import Open_EngagementRings_PLP_Page


def test_add_remove_wishlist_page(page):

    menu_header_option = Open_Menu_Header_Options(page)
    wishlist=AddRemoveWishlist(page)
    engagement_rings_plp = Open_EngagementRings_PLP_Page(page)
    search = SearchSKU(page)

    #ADD-REMOVE WISHLIST FROM THE PLP, SLP, PDP AND MY ACCOUNT>WISHLIST PAGES.
    print("----> TEST CASE 1 OF 4")
    engagement_rings_plp.test_open_engagement_rings_plp_page()
    wishlist.test_add_wishlist_plp_slp()
    search.test_search_with_keyword("R102205")
    wishlist.test_remove_wishlist_plp_slp()

    print("----> TEST CASE 2 OF 4")
    search.test_search_with_sku("R102205")
    wishlist.test_add_wishlist_pdp()
    engagement_rings_plp.test_open_engagement_rings_plp_page()
    wishlist.test_remove_wishlist_plp_slp()

    print("----> TEST CASE 3 OF 4")
    search.test_search_with_keyword("R102205")
    wishlist.test_add_wishlist_plp_slp()
    search.test_search_with_sku("R102205")
    wishlist.test_remove_wishlist_pdp()

    print("----> TEST CASE 4 OF 4")
    search.test_search_with_keyword("R102205")
    wishlist.test_add_wishlist_plp_slp()
    menu_header_option.test_open_wishlist_page_header()
    wishlist.test_remove_wishlist_from_my_account_wishlist_page()
