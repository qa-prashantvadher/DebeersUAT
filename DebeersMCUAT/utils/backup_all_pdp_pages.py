from pages.brilliant_spp_no_size import BB_SPP_No_Size
from pages.brilliant_spp_single_size import BB_SPP_Single_Size
from pages.brilliant_spp_multiple_size import BB_SPP_Multiple_Size
from pages.brilliant_upp_multiple_variant import BB_UPP_Multiple_Variant
from pages.hj_upp_multiple_variant import HJ_UPP_Multiple_Variant
from pages.hj_upp_single_variant import HJ_UPP_Single_Variant
from pages.hj_spp_single_size import HJ_SPP_Single_Size
from pages.hj_spp_multiple_size import HJ_SPP_Multiple_Size
from pages.hj_spp_no_size import HJ_SPP_No_Size
from pages.old_spp_no_size import OLD_SPP_No_Size
from pages.shopping_cart_page import Open_Shopping_Cart_Page
from pages.upp_multiple_variant_filter import UPP_Multiple_Variant_Filter


def test_add_to_bag_for_all_product_types_and_templates(page):

    bb_spp_no_size = BB_SPP_No_Size(page)
    bb_spp_single_size = BB_SPP_Single_Size(page)
    bb_spp_multiple_size = BB_SPP_Multiple_Size(page)
    bb_upp_multiple_variant = BB_UPP_Multiple_Variant(page)
    hj_upp_multiple_variant = HJ_UPP_Multiple_Variant(page)
    hj_upp_single_variant = HJ_UPP_Single_Variant(page)
    hj_spp_single_size = HJ_SPP_Single_Size(page)
    hj_spp_multiple_size = HJ_SPP_Multiple_Size(page)
    hj_spp_no_size = HJ_SPP_No_Size(page)
    old_spp_no_size = OLD_SPP_No_Size(page)
    shopping_bag = Open_Shopping_Cart_Page(page)
    upp_variant_filter = UPP_Multiple_Variant_Filter(page)

    # BB SPP WITHOUT SIZE PDP: ADD PRODUCT TO THE CART WITH AND WITHOUT ENGRAVING
    bb_spp_no_size.test_bb_spp_no_size_with_engraving()
    bb_spp_no_size.test_bb_spp_no_size_without_engraving()

    # BB SPP WITHOUT SIZE PDP: REMOVE 2 PRODUCTS FROM THE CART
    shopping_bag.test_open_shopping_cart_page()
    cart_products = shopping_bag.test_get_cart_products_count()
    if cart_products > 0:
       for cart_products in range(1, cart_products + 1):
           shopping_bag.test_remove_product_from_cart()


    # BB SPP WITH SINGLE SIZE PDP: ADD PRODUCT TO THE CART WITH AND WITHOUT ENGRAVING
    bb_spp_single_size.test_bb_spp_single_size_with_engraving()
    bb_spp_single_size.test_bb_spp_single_size_without_engraving()

    # BB SPP WITH SINGLE SIZE PDP: REMOVE 2 PRODUCTS FROM THE CART
    shopping_bag.test_open_shopping_cart_page()
    cart_products = shopping_bag.test_get_cart_products_count()
    if cart_products > 0:
        for cart_products in range(1, cart_products + 1):
            shopping_bag.test_remove_product_from_cart()


    # BB SPP WITH MULTIPLE SIZE PDP: ADD PRODUCT TO THE CART WITH AND WITHOUT ENGRAVING
    bb_spp_multiple_size.test_bb_spp_multiple_size_with_engraving()
    bb_spp_multiple_size.test_bb_spp_multiple_size_without_engraving()

    # BB SPP WITH MULTIPLE SIZE PDP: REMOVE 2 PRODUCTS FROM THE CART
    shopping_bag.test_open_shopping_cart_page()
    cart_products = shopping_bag.test_get_cart_products_count()
    if cart_products > 0:
        for cart_products in range(1, cart_products + 1):
            shopping_bag.test_remove_product_from_cart()


    # BB UPP WITH MULTIPLE VARIANTS PDP: ADD PRODUCT TO THE CART WITH AND WITHOUT ENGRAVING
    bb_upp_multiple_variant.test_bb_upp_multiple_variant_with_engraving()
    bb_upp_multiple_variant.test_bb_upp_multiple_variant_without_engraving()

    # BB UPP WITH MULTIPLE VARIANTS PDP: REMOVE 2 PRODUCTS FROM THE CART
    shopping_bag.test_open_shopping_cart_page()
    cart_products = shopping_bag.test_get_cart_products_count()
    if cart_products > 0:
        for cart_products in range(1, cart_products + 1):
            shopping_bag.test_remove_product_from_cart()

    # HJ UPP WITH MULTIPLE VARIANTS PDP: ADD PRODUCT TO THE CART WITH AND WITHOUT ENGRAVING
    hj_upp_multiple_variant.test_hj_upp_multiple_variant_with_engraving()
    hj_upp_multiple_variant.test_hj_upp_multiple_variant_without_engraving()

    # HJ UPP WITH MULTIPLE VARIANTS PDP: REMOVE 2 PRODUCTS FROM THE CART
    shopping_bag.test_open_shopping_cart_page()
    cart_products = shopping_bag.test_get_cart_products_count()
    if cart_products > 0:
        for cart_products in range(1, cart_products + 1):
            shopping_bag.test_remove_product_from_cart()


    # HJ UPP WITH SINGLE VARIANT PDP: ADD PRODUCT TO THE CART WITH AND WITHOUT ENGRAVING
    hj_upp_single_variant.test_hj_upp_single_variant_with_engraving()
    hj_upp_single_variant.test_hj_upp_single_variant_without_engraving()

    # HJ UPP WITH SINGLE VARIANT PDP: REMOVE 2 PRODUCTS FROM THE CART
    shopping_bag.test_open_shopping_cart_page()
    cart_products = shopping_bag.test_get_cart_products_count()
    if cart_products > 0:
        for cart_products in range(1, cart_products + 1):
            shopping_bag.test_remove_product_from_cart()


    # HJ SPP WITH SINGLE SIZE PDP: ADD PRODUCT TO THE CART WITHOUT ENGRAVING
    hj_spp_single_size.test_hj_spp_single_size_without_engraving()
    hj_spp_single_size.test_hj_spp_single_size_without_engraving()

    # HJ SPP WITH SINGLE SIZE PDP: REMOVE 2 PRODUCTS FROM THE CART
    shopping_bag.test_open_shopping_cart_page()
    cart_products = shopping_bag.test_get_cart_products_count()
    if cart_products > 0:
        for cart_products in range(1, cart_products + 1):
            shopping_bag.test_remove_product_from_cart()


    # HJ SPP WITH MULTIPLE SIZE PDP: ADD PRODUCT TO THE CART WITHOUT ENGRAVING
    hj_spp_multiple_size.test_hj_spp_multiple_size_without_engraving()
    hj_spp_multiple_size.test_hj_spp_multiple_size_without_engraving()

    # HJ SPP WITH MULTIPLE SIZE PDP: REMOVE 2 PRODUCTS FROM THE CART
    shopping_bag.test_open_shopping_cart_page()
    cart_products = shopping_bag.test_get_cart_products_count()
    if cart_products > 0:
        for cart_products in range(1, cart_products + 1):
            shopping_bag.test_remove_product_from_cart()


    # HJ SPP WITHOUT SIZE PDP: ADD PRODUCT TO THE CART WITHOUT ENGRAVING
    hj_spp_no_size.test_hj_spp_no_size_without_engraving()
    hj_spp_no_size.test_hj_spp_no_size_without_engraving()

    # HJ SPP WITHOUT SIZE PDP: REMOVE 2 PRODUCTS FROM THE CART
    shopping_bag.test_open_shopping_cart_page()
    cart_products = shopping_bag.test_get_cart_products_count()
    if cart_products > 0:
        for cart_products in range(1, cart_products + 1):
            shopping_bag.test_remove_product_from_cart()


    # OLD SPP WITHOUT SIZE PDP: ADD PRODUCT TO THE CART WITHOUT ENGRAVING
    old_spp_no_size.test_old_spp_no_size_without_engraving()
    old_spp_no_size.test_old_spp_no_size_without_engraving()

    # OLD SPP WITHOUT SIZE PDP: REMOVE 2 PRODUCTS FROM THE CART
    shopping_bag.test_open_shopping_cart_page()
    cart_products = shopping_bag.test_get_cart_products_count()
    if cart_products > 0:
        for cart_products in range(1, cart_products + 1):
            shopping_bag.test_remove_product_from_cart()


    #UPP MULTIPLE VARIANTS PDP: APPLY FILTER IN THE VARIANT SECTION
    upp_variant_filter.test_bb_upp_variant_filter()
    upp_variant_filter.test_bb_clear_all_filters()
    upp_variant_filter.test_hj_upp_variant_filter()
    upp_variant_filter.test_hj_clear_all_filters()

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




