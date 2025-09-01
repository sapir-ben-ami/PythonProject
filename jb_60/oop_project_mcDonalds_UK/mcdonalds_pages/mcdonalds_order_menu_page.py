class mcdonaldsOrderMenuPage():

    def __init__(self, page):
        self.page = page

    def go_to_pay_with_mecdonalds_app(self):
        pay_in_mcdonalds_app_button = self.page.locator("[id = 'downloadAppLinkDesktop']")
        pay_in_mcdonalds_app_button.click()