# validat all button in header menu in page "our plan fot change" using pytest parametrize
    # Entering "our plan fot change" page
    # clicking on all the buttons in the main menu
    # checking that the buttons lead to the correct pages



import time
from time import sleep

import pytest

from jb_60.oop_project_mcDonalds_UK.mcdonalds_pages.mcdonalds_find_restaurant_page import mcdonaldaFindReaturant
from jb_60.oop_project_mcDonalds_UK.mcdonalds_pages.mcdonalds_home_page import mcdonaldsHome


class TestMcdonaldsOurPlanForChange():

    def test_mcdonalds_our_plan_for_change(self, setup_mcdonalds):
        #get in McDonalds web
        page = setup_mcdonalds  #fixture activate

        #function instance
        mcdonals_home_page = mcdonaldsHome(page)

        #go to "our plan for change" page
        mcdonals_home_page.go_to_our_plan_for_chane_page_from_home()
        sleep(5)
        assert page.url == "https://www.mcdonalds.com/gb/en-gb/our-plan-for-change.html",\
            "Wrong url, the page is not 'our plan for change'"

    links_list = [["Planet Positive", "https://www.mcdonalds.com/gb/en-gb/our-plan-for-change/planet-positive.html"],
                  ["Great Food", "https://www.mcdonalds.com/gb/en-gb/our-plan-for-change/great-food.html"],
                  ["Great Restaurants", "https://www.mcdonalds.com/gb/en-gb/our-plan-for-change/great-restaurants.html"],
                  ["People Positive", "https://www.mcdonalds.com/gb/en-gb/our-plan-for-change/people-positive.html"],
                  ["Communities", "https://www.mcdonalds.com/gb/en-gb/our-plan-for-change/communities.html"]]

    test_names = ["validate_link_Planet_Positive", "validate_link_Great Food", "validate_link_Great Restaurants",
                  "validate_link_People Positive", "validate_link_Communities"]

    @pytest.mark.parametrize("menu_link", links_list, ids = test_names)
    def test_mcdonalds_plan_for_change_menu_links(self, setup_mcdonalds, menu_link):
        menu_link_name = menu_link[0]
        menu_link_url = menu_link[1]
        print(f"validating link {menu_link_name}")

        #get in McDonalds web
        page = setup_mcdonalds  #fixture activate

        #function instance
        mcdonals_home_page = mcdonaldsHome(page)

        #go to "out plan for change" page
        mcdonals_home_page.go_to_our_plan_for_chane_page_from_home()
        sleep(5)

        #go to link from the menu
        menu_link_button = page.get_by_role("link", name=menu_link_name)
        menu_link_button.click()
        time.sleep(5)
        assert page.url == menu_link_url, f"wrong page. \n expected url {menu_link_url}, \n got url: {page.url}"






