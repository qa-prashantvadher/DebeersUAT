from pages.search_slp_pdp import SearchSKU

'''
TEST SCENARIOS:

AREA COVERED: SEARCH MODAL AND SLP PAGE.

- SEARCH MODAL
    - Open Client Services page.
- SLP:    
    - Search with SKU and select product from the suggested list to open PDP.
    - Search with keywords to view SLP page without results.
    - Search with keywords to view SLP page with results.
        - Apply Sorting: Price ascending and Price descending
        - Apply Filters.
        - Clear all Filters.
'''

def test_search_modal_slp_page(page):

    search = SearchSKU(page)

    # SEARCH PRODUCTS BY SKU AND KEYWORDS. APPLY-CLEAR FILTERS AND APPLY SORTING ON THE SLP PAGE.
    search.test_open_contact_us_page_from_search()

    search.test_search_with_sku("B103218")

    search.test_search_with_keyword("Testing")

    search.test_search_with_keyword("Anneaux")
    search.test_apply_sorting_on_slp()
    search.test_apply_filter_on_slp()
    search.test_clear_filter_on_slp()

    search.test_search_with_keyword("Haute Joaillerie")
    search.test_apply_sorting_on_slp()
    search.test_apply_filter_on_slp()
    search.test_clear_filter_on_slp()
