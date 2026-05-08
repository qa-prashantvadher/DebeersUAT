from pages.open_plp_page import Open_EngagementRings_PLP_Page


def test_engagement_rings_plp_page(page):
    engagement_rings_plp = Open_EngagementRings_PLP_Page(page)

    # GO TO ENGAGEMENT RINGS PLP PAGE. APPLY FILTER AND SORTING.
    print("----> TEST CASE 1 OF 1")
    engagement_rings_plp.test_open_engagement_rings_plp_page()
    engagement_rings_plp.test_apply_sorting_on_plp()
    engagement_rings_plp.test_apply_filter_on_plp()
    engagement_rings_plp.test_clear_filter_on_plp()
