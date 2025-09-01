class mcdonaldaFindReaturant():

    def __init__(self, page):
        self.page = page

    def fill_address(self, address):
        self.page.fill("#form-text-1673594539", address)
        self.page.keyboard.press("Enter")

    def extract_distance_for_each_restaurant(self):
        mcdonalds_restaraunts_distance_list = self.page.query_selector_all(
            "[class='cmp-restaurant-locator__restaurant-list-item-details-distance']")
        list_of_distances_float = []
        for testarount_distance in mcdonalds_restaraunts_distance_list:
            testarount_distance_text = testarount_distance.text_content()
            testarount_distance_text_split = testarount_distance_text.split()
            distance = float(testarount_distance_text_split[1])
            print(f"float distance is {distance}")
            list_of_distances_float.append(distance)
        return list_of_distances_float

