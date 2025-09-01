import time
from time import sleep


class mcdonaldsHome():

    def __init__(self, page):
        self.page = page

    def go_to_find_restaurant_from_home_page(self):
        find_restaurant_button = self.page.get_by_role("link", name = "Find Your Restaurant")
        find_restaurant_button.click()

    def go_to_our_plan_for_chane_page_from_home(self):
        self.page.keyboard.press("End")
        time.sleep(1)
        our_plan_for_change_button = self.page.get_by_role("link", name="Our Plan for Change")
        our_plan_for_change_button.click()


    def go_to_item_menu(self, item_name):
        menu_button = self.page.locator("button.primary-menu[aria-controls='ourMenuSubItemsList_desktop']", has_text="Menu")
        menu_button.click()
        time.sleep(2)
        item_button = self.page.get_by_role("link", name=item_name)
        item_button.click()
        time.sleep(5)


    def go_to_order_menu_from_home_page(self):
        order_menu_button = self.page.locator("[id = 'button-ordernow']")
        order_menu_button.click()





        print("done")