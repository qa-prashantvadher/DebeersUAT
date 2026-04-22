import time
import os
from pages.base_page import BasePage
from dotenv import load_dotenv

load_dotenv()

class PageScreenshot(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.ENV = os.getenv("ENVIRONMENT").upper()
        self.COUNTRY = os.getenv("LOCALE").upper()
        self.date_folder = time.strftime('%d%m%Y')

        screenshot_path = r"D:\Debeers Videos and Screenshots\Screenshots"
        env_map = {
            "UAT": "DB-UAT",
            "PROD": "DB-PROD",
            "QA": "DB-QA"
        }

        if self.ENV not in env_map:
            raise ValueError(f"Invalid Environment: {self.ENV}")

        if self.COUNTRY not in ["UK", "US", "FR", "HK"]:
            raise ValueError(f"Invalid Country: {self.COUNTRY}")

        self.base_path = os.path.join(screenshot_path, env_map[self.ENV], self.COUNTRY)
        self.order_sub_folder = "ORDERS"
        self.other_sub_folder = "OTHERS"

    # Common method (DRY)
    def _take_screenshot(self, sub_folder, keyword, full_page=False):
        '''
        timestamp = time.strftime('%d-%m-%Y_%H-%M-%S')
        folder_path = os.path.join(self.base_path, sub_folder, self.date_folder)
        os.makedirs(folder_path, exist_ok=True)
        filename = os.path.join(folder_path, f'{keyword}_{timestamp}.png')
        print(f"==> [{self.ENV}-{self.COUNTRY}] FILE: {keyword}_{timestamp}.png")
        self.page.screenshot(path=filename, full_page=full_page)
        '''
    # Public methods
    def take_page_screenshot(self, keyword):
        self._take_screenshot(self.other_sub_folder, keyword)

    def take_order_page_screenshot(self, keyword):
        self._take_screenshot(self.order_sub_folder, keyword, full_page=True)