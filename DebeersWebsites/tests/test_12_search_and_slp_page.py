from pages.search_slp_pdp import SearchSKU
from dotenv import load_dotenv
import os

load_dotenv(override=True)

ENV = os.getenv("ENVIRONMENT").upper()
COUNTRY = os.getenv("LOCALE").upper()


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
    print("----> TEST CASE 1 OF 5")
    search.test_open_contact_us_page_from_search()

    print("----> TEST CASE 2 OF 5")
    search.test_search_with_sku("B103218")

    print("----> TEST CASE 3 OF 5")
    search.test_search_with_keyword("Testing")

    print("----> TEST CASE 4 OF 5")
    if COUNTRY == "UK" or COUNTRY == "US":
        search.test_search_with_keyword("Rings")
    elif COUNTRY == "FR":
        search.test_search_with_keyword("Anneaux")
    elif COUNTRY == "HK" or COUNTRY == "TW" or COUNTRY == "MO":
        search.test_search_with_keyword("戒指")
    search.test_apply_sorting_on_slp()
    search.test_apply_filter_on_slp()
    search.test_clear_filter_on_slp()

    print("----> TEST CASE 5 OF 5")
    if COUNTRY == "UK" or COUNTRY == "US":
        search.test_search_with_keyword("High Jewellery")
    elif COUNTRY == "FR":
        search.test_search_with_keyword("Haute Joaillerie")
    elif COUNTRY == "HK" or COUNTRY == "TW" or COUNTRY == "MO":
        search.test_search_with_keyword("首飾")
    search.test_apply_sorting_on_slp()
    search.test_apply_filter_on_slp()
    search.test_clear_filter_on_slp()
