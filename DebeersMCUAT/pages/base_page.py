class BasePage:
    def __init__(self, page):
        self.page = page

    def select_option(self, locator: object, text: object):
        self.page.locator(locator).select_option(text)

    def navigate(self, url):
        self.page.goto(url)

    def inner_text(self, locator):
        return self.page.locator(locator).inner_text()

    def click(self, locator):
        self.page.locator(locator).click()

    def check(self, locator):
        self.page.locator(locator).check()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def is_checked(self, locator):
        return self.page.locator(locator).is_checked()

    def is_not_visible(self, locator):
        return self.page.locator(locator).is_not_visible()

    def press(self, locator, text):
        return self.page.locator(locator).press(text)

    def keyboard_press(self, text):
        return self.page.keyboard_press(text)

    def wait_for_element(self, locator, timeout):
        return self.page.locator(locator).wait_for_element(timeout)

    def timeout(self, timeout):
        return self.page.wait_for_timeout(timeout)

    def select_value(self,locator, text):
        return self.page.locator(locator).select_option(text)

    def scroll_down(self, locator):
        return self.page.locator(locator).scroll_into_view_if_needed()