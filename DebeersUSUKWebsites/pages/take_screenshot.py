import time
import os
from pages.base_page import BasePage
from dotenv import load_dotenv
load_dotenv(override=True)

ENV = os.getenv("ENVIRONMENT")

class PageScreenshot(BasePage):
    date_folder = time.strftime('%d%m%Y')

    if ENV == "UAT":
        base_path = r"D:\Python Code\Screenshots\DB-UAT\US"
    elif ENV == "PROD":
        base_path = r"D:\Python Code\Screenshots\DB-PROD\US"
    elif ENV == "QA":
        base_path = r"D:\Python Code\Screenshots\DB-QA\US"

    order_sub_folder = "ORDERS"
    other_sub_folder = "OTHERS"


    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def take_page_screenshot(self, keyword):
        timestamp = time.strftime('%d-%m-%Y_%H-%M')
        other_screenshot_full_path = os.path.join(self.base_path, self.other_sub_folder, self.date_folder)
        os.makedirs(other_screenshot_full_path, exist_ok=True)
        filename = os.path.join(other_screenshot_full_path, f'{keyword}_{timestamp}.png')
        self.page.screenshot(path=filename)

    def take_order_page_screenshot(self, keyword):
        timestamp = time.strftime('%d-%m-%Y_%H-%M')
        order_screenshot_full_path = os.path.join(self.base_path, self.order_sub_folder, self.date_folder)
        os.makedirs(order_screenshot_full_path, exist_ok=True)
        filename = os.path.join(order_screenshot_full_path, f'{keyword}_{timestamp}.png')
        self.page.screenshot(path=filename,full_page=True)
