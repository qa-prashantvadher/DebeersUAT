import time
import os
from pages.base_page import BasePage



class PageScreenshot(BasePage):
    Screenshot_Path = "D:\Python Code\Screenshots\DB-UAT\OTHERS"
    Order_Screenshot_Path = "D:\Python Code\Screenshots\DB-UAT\ORDERS"

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def take_page_screenshot(self, keyword):
        timestamp = time.strftime('%d-%m-%Y_%H-%M')
        filename = os.path.join(self.Screenshot_Path, f'{keyword}_{timestamp}.png')
        os.makedirs(self.Screenshot_Path, exist_ok=True)
        self.page.screenshot(path=filename)

    def take_order_page_screenshot(self, keyword):
        timestamp = time.strftime('%d-%m-%Y_%H-%M')
        filename = os.path.join(self.Order_Screenshot_Path, f'{keyword}_{timestamp}.png')
        os.makedirs(self.Screenshot_Path, exist_ok=True)
        self.page.screenshot(path=filename,full_page=True)   
