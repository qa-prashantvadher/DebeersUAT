from pages.brilliant_spp_multiple_size import BB_SPP_Multiple_Size
from pages.hj_spp_multiple_size import HJ_SPP_Multiple_Size
from pages.shopping_cart_page import Open_Shopping_Cart_Page


def test_add_to_bag_for_spp_multiple_size_all_templates(page):

    bb_spp_multiple_size = BB_SPP_Multiple_Size(page)
    hj_spp_multiple_size = HJ_SPP_Multiple_Size(page)
    shopping_bag = Open_Shopping_Cart_Page(page)

    # BB SPP WITH MULTIPLE SIZE PDP: ADD PRODUCT TO THE CART WITH AND WITHOUT ENGRAVING
    print("----> TEST CASE 1 OF 2")
    bb_spp_multiple_size.test_bb_spp_multiple_size_with_engraving()
    bb_spp_multiple_size.test_bb_spp_multiple_size_without_engraving()

    # BB SPP WITH MULTIPLE SIZE PDP: REMOVE 2 PRODUCTS FROM THE CART
    shopping_bag.test_open_shopping_cart_page()
    product_counter = 1
    while shopping_bag.test_get_cart_products_count() > 0:
        shopping_bag.test_remove_product_from_cart(product_counter)
        product_counter += 1

    # HJ SPP WITH MULTIPLE SIZE PDP: ADD PRODUCT TO THE CART WITHOUT ENGRAVING
    print("----> TEST CASE 2 OF 2")
    hj_spp_multiple_size.test_hj_spp_multiple_size_with_engraving()
    hj_spp_multiple_size.test_hj_spp_multiple_size_without_engraving()

    # HJ SPP WITH MULTIPLE SIZE PDP: REMOVE 2 PRODUCTS FROM THE CART
    shopping_bag.test_open_shopping_cart_page()
    product_counter = 1
    while shopping_bag.test_get_cart_products_count() > 0:
        shopping_bag.test_remove_product_from_cart(product_counter)
        product_counter += 1


    #https://development.debeers.co.uk/en-gb/db-classic-pear-shaped-diamond-pendant/N102152.html [HJ UPP SINGLE without E]
    #https://development.debeers.co.uk/en-gb/db-classic-simple-shank-radiant-square-cut-diamond-ring/R102133.html [HJ UPP SINGLE with E]
    #https://development.debeers.co.uk/en-gb/diamond-polishing-wipes-%28box-of-50%29/A1021110000.html [OLD SPP]
    #https://development.debeers.co.uk/en-gb/talisman-cocktail-medallion-in-white-gold/N103489.html [HJ SPP SINGLE]
    #https://development.debeers.co.uk/en-gb/talisman-cocktail-ring-in-yellow-gold/R103731.html [HJ SPP Multiple]
    #https://development.debeers.co.uk/en-gb/portraits-of-nature-butterfly-earrings-in-white-gold/E103343.html [HJ SPP no size]
    #https://development.debeers.co.uk/en-gb/arpeggia-three-line-earrings-in-white-gold/E102155.html
    #https://development.debeers.co.uk/en-gb/arpeggia-five-line-earrings-in-rose-gold/E102156.html
    #https://development.debeers.co.uk/en-gb/arpeggia-five-line-earrings-in-white-gold/E102157.html
    #https://development.debeers.co.uk/en-gb/db-classic-eternity-line-round-brilliant-diamond-bracelet/B102127.html




