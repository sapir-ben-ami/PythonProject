# Checking the order menu and "order button" on the home page and within the products
    # Test 1 - Checking order menu - cheacking payment with McDonald's app
    # Test 2 - Checking order menu - cheacking payment with McDonald's partners, using pytest parametrize
    # Test 3 - Checking the order button on the home page
    # Test 4 - Checking the order button under one of the items leads to the order menu

import time

import pytest
from playwright.async_api import expect

from jb_60.oop_project_mcDonalds_UK.mcdonalds_pages.mcdonalds_home_page import mcdonaldsHome
from jb_60.oop_project_mcDonalds_UK.mcdonalds_pages.mcdonalds_item_page import mcdonaldsItemPage
from jb_60.oop_project_mcDonalds_UK.mcdonalds_pages.mcdonalds_order_menu_page import mcdonaldsOrderMenuPage


class TestMcdonaldsordermenu():


# Test 1 - Checking payment with the McDonald's app:
    #   Entering the payment menu using the button on the home page
    #   selecting payment in the app
    #   checking that the McDonald's app QR code appears

    def test_mcdonalds_order_menu_order_in_mcdonalds_app(self, setup_mcdonalds):
        # get in McDonalds web
        page = setup_mcdonalds  # fixture activate

        # function instance
        mcdonals_home_page = mcdonaldsHome(page)
        mcdonalds_order_menu_page = mcdonaldsOrderMenuPage(page)

        # get in order menu
        mcdonals_home_page.go_to_order_menu_from_home_page()

        # check order by McDonalds app (assert by McDonalds app QR code)
        mcdonalds_order_menu_page.go_to_pay_with_mecdonalds_app()
        mcdonalds_app_qr_code_img = page.locator('img[src="/content/dam/sites/uk/nfl/order-delivery/qr-code-downloadapp.png"]')
        mcdonalds_app_qr_code_img_visible_validation = mcdonalds_app_qr_code_img.count()
        qr_visible_validation = ""
        if mcdonalds_app_qr_code_img_visible_validation == 0:
            qr_visible_validation = "not"
        print(f"QR is {qr_visible_validation} visible")

        assert mcdonalds_app_qr_code_img_visible_validation > 0, "bug: QR McDonalds App code is not visible in site"



#   Test 2 - Checking order menu - cheacking payment with McDonald's partners
    #   Entering the payment menu using the button on the home page
    #   clicking on each of the payment options using pytest parametrize
    #   checking that the relevant page opens

    Payment_options_list = [
            ["UberEats", "https://www.ubereats.com/?utm_source=ext_McD&utm_campaign=ext-mcdonalds-McDeliveryWebsite-OrderNow"],
            ["Just Eat", "https://www.just-eat.co.uk/takeaway/brands/mcdonalds?utm_source=mcdonalds&utm_medium=referral&utm_campaign=mcdelivery__;!!JZ0iVwK7KX4!X0OwiQ5YsYGIXbw0i8jPrWc96mxOnb8OkhMhkS1fWXpVnc-jiPjWehbSv47bLEz_InU$"],
            ["Deliveroo", "https://deliveroo.co.uk/brands/mcdonalds-uk?utm_source=mcdonalds&utm_medium=web&utm_campaign=referral&utm_content=a"]]

    test_names = ["validate_paying_with_uberEats", "validate_paying_with_Just_Eat", "validate_paying_with_deliveroo"]

    @pytest.mark.parametrize("Payment_options", Payment_options_list, ids=test_names)
    def test_mcdonalds_order_menu_order_with_mcdonalds_delivery_partners(self, setup_mcdonalds, Payment_options):
        page = setup_mcdonalds
        mcdonals_home_page = mcdonaldsHome(page)

        # get in order menu
        mcdonals_home_page.go_to_order_menu_from_home_page()

        # check that the costumer can order through partners mcdonalds delivery partners
        payment_option_name = Payment_options[0]
        payment_option_url_page = Payment_options[1]

        payment_option_button = page.locator("a.cmp-order-delivery-modal__partners-list-item", has_text=payment_option_name)
        payment_option_button.click()


        with page.expect_popup() as popup_info:
            continue_button = page.locator("[id = 'cmp-legal-bumper__button--continue-link']")
            continue_button.click()
            new_page = popup_info.value
            new_page.wait_for_load_state("load")
            new_page_url = new_page.url
        print(f"New tab URL: {new_page_url}")

        assert new_page_url == payment_option_url_page, \
            "Bug: Unable to pay through the company. Clicking on the payment page does not open the payment page"

        new_page.close()


# Test 3 - Checking the order button on the home page
    #   Entering the home page
    #   Checking that the order button on the home page leads to the order menu

    def test_mcdonalds_order_button_in_home_page(self, setup_mcdonalds):
        # get in McDonalds web
        page = setup_mcdonalds  # fixture activate

        # function instance
        mcdonals_home_page = mcdonaldsHome(page)

        # click on order button in home page
        mcdonals_home_page.go_to_order_menu_from_home_page()

        page_title = page.locator("[id = 'cmp-order-delivery-modal__title']")
        page_title_text = page_title.text_content()
        print(f"page title is {page_title_text}")

        assert "Order McDelivery® through our app to earn Rewards Points" in page_title_text, \
            "Bug in the order button on the home page: the order menu does not open from the home page"


# Test 4 - Checking the order button under one of the items leads to the order menu
    #   Entering to ine of the items in the menu
    #   Checking that the order button on the item leads to the order menu

    def test_mcdonalds_order_button_in_itam(self, setup_mcdonalds):
        page = setup_mcdonalds
        mcdonals_home_page = mcdonaldsHome(page)
        mcdonalds_item_page = mcdonaldsItemPage(page)

         # go to item from home page
        item_name = "Burgers"
        mcdonals_home_page.go_to_item_menu(item_name)

        sub_item = "Big Arch®"
        sub_item_button = page.locator(".cmp-category__item-name",
                                        has_text=sub_item)
        sub_item_button.click()
        time.sleep(2)

        # check order button in item page
        mcdonalds_item_page.press_order_button_in_item_page()

        page_title = page.locator("[id = 'cmp-order-delivery-modal__title']")
        page_title_text = page_title.text_content()
        print(f"page title is {page_title_text}")

        assert "Order McDelivery® through our app to earn Rewards Points" in page_title_text, \
            "Bug in the order button on the home page: the order menu does not open from the home page"


