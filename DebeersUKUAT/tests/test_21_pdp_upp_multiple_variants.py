from pages.brilliant_upp_multiple_variant import BB_UPP_Multiple_Variant
from pages.hj_upp_multiple_variant import HJ_UPP_Multiple_Variant
from pages.shopping_cart_page import Open_Shopping_Cart_Page
from pages.upp_multiple_variant_filter import UPP_Multiple_Variant_Filter


def test_add_to_bag_for_all_product_types_and_templates(page):

    bb_upp_multiple_variant = BB_UPP_Multiple_Variant(page)
    hj_upp_multiple_variant = HJ_UPP_Multiple_Variant(page)
    shopping_bag = Open_Shopping_Cart_Page(page)
    upp_variant_filter = UPP_Multiple_Variant_Filter(page)


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




