# validat that mcdonalds restaurant in page "find reataraunt" is sorted from nearest to far.
    # Retrieving all restaurants in a specific area
    # creating a list of the distances of the results
    # checking that the results on the page are sorted from the closest restaurant to the furthest

import time
from jb_60.oop_project_mcDonalds_UK.mcdonalds_pages.mcdonalds_find_restaurant_page import mcdonaldaFindReaturant
from jb_60.oop_project_mcDonalds_UK.mcdonalds_pages.mcdonalds_home_page import mcdonaldsHome


class TestMcdonaldRestaraunts():

    def test_mcdonalds_restaraunt_sorted_by_distance(self, setup_mcdonalds):
        page = setup_mcdonalds

        mcdonals_home_page = mcdonaldsHome(page)
        mcdonalds_find_restaraunt = mcdonaldaFindReaturant(page)

        #get in 'find a restaurant' page
        mcdonals_home_page.go_to_find_restaurant_from_home_page()

        #search address in "find reataurant" page
        address = "SW1A 1AA"
        mcdonalds_find_restaraunt.fill_address(address)

        #check that mcdonalds restaurant sorted by distance
        time.sleep(5)  # sleep due delay in site

        #extract distance for each restaurant
        list_of_distances_float = mcdonalds_find_restaraunt.extract_distance_for_each_restaurant()

        #valitad that distances in the site are sorted from small to big
        sorted_list_of_distances_float = sorted(list_of_distances_float)
        print(f"original list_of_distances_float: {list_of_distances_float} \n"
              f"sorted list_of_distances_float: {sorted_list_of_distances_float}")

        assert list_of_distances_float == sorted_list_of_distances_float, \
            ("bug: distances in the site are not sorted from small to big \n"
             "original list_of_distances_float: {list_of_distances_float} \n"
             "sorted list_of_distances_float: {sorted_list_of_distances_float}")

        print("end")


