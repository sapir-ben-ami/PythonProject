# Checking the calorie calculation in site
# Comparing between the total calories of the product and the sum of the calories of its ingredients.
    # get the total calories of the product.
    # get the calories of its ingredients
    # sum the calories of the ingredients
    # compare between the total calories of the product and the sum calories of its ingredients .


import time

from jb_60.oop_project_mcDonalds_UK.mcdonalds_pages.mcdonalds_home_page import mcdonaldsHome
from jb_60.oop_project_mcDonalds_UK.mcdonalds_pages.mcdonalds_item_page import mcdonaldsItemPage


class TestMcdonaldsCaloriesSum():
    def test_mcdonalds_calories_sum(self, setup_mcdonalds):
        page = setup_mcdonalds
        mcdonalds_item_page = mcdonaldsItemPage(page)
        mcdonals_home_page = mcdonaldsHome(page)

        # go to item from home page
        item_name = "Burgers"
        mcdonals_home_page.go_to_item_menu(item_name)

        sub_item = "Big Arch®"
        sub_item_button = page.locator(".cmp-category__item-name",
                                        has_text=sub_item)
        sub_item_button.click()
        time.sleep(2)

        # get total calories
        total_calories_num = mcdonalds_item_page.get_total_calories()
        print(f"total calories is {total_calories_num}")

        # Sum ingredients calories
        calories_sum = mcdonalds_item_page.sum_ingredients_calories()

        print(f"total calories in site is {total_calories_num} \n"
              f"Sum of calories of ingredients is {calories_sum}")

        assert total_calories_num == calories_sum, (f"bug: The sum of the calories of the product ({total_calories_num}) "
                                                    f"is not equal to the sum of the calories of its components ({calories_sum})")





