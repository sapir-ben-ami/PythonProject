import time


class mcdonaldsItemPage():

    def __init__(self, page):
        self.page = page

    def press_order_button_in_item_page(self):
        order_button_in_item = self.page.locator("div.cmp-product-details-main__order-now >> text=Order McDelivery")
        order_button_in_item.click()
        time.sleep(2)

    def get_total_calories(self):
        total_calories_element = self.page.locator(".cmp-product-details-main__desktop-only .sr-only")
        total_calories_text = total_calories_element.text_content()
        total_calories_list = total_calories_text.split()
        total_calories_num = int(total_calories_list[2])
        return total_calories_num

    def sum_ingredients_calories(self):
        calories_sum = 0
        product_calories_list = self.page.query_selector_all(
            "[class = 'cmp-slick-carousel__caption cmp-slick-carousel__caption--ingredients']")
        for product in product_calories_list:
            print(f"calories sum is {calories_sum}")
            product_text = product.text_content()
            product_text_split = product_text.split()
            product_text_calories = product_text_split[3]
            product_calories_int = int(product_text_calories)
            calories_sum = calories_sum + product_calories_int
        return calories_sum