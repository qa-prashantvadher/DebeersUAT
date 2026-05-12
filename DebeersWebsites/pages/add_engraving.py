from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
import os
from dotenv import load_dotenv
import logging

load_dotenv(override=True)
logger = logging.getLogger(__name__)

class AddEngraving(BasePage):

    URL = os.getenv("BASE_URL")
    COUNTRY = os.getenv("LOCALE").upper()

    engraving_input = "//*[@id='engravingText']"
    if COUNTRY == "FR":
        new_engraving_text = "Les diamants durent"
        update_engraving_text = "De Beers is Forever"
    elif COUNTRY == "HK" or COUNTRY == "TW" or COUNTRY == "MO":
        new_engraving_text = "鑽石恆久遠"
        update_engraving_text = "戴比爾斯是永恆的"
    else:
        new_engraving_text = "A Diamond is Forever"
        update_engraving_text = "De Beers is Forever"
    monotype_font = "//*[@id='Monotype-Corsiva']"
    arial_font = "//*[@id='Arial']"
    submit_button = "//*[@id='pdpEngraving']/div[3]/div/div[2]/div[2]/button[1]"
    update_button = "//*[@id='pdpEngraving']/div[3]/div/div[2]/div[2]/button[2]"
    close_icon = "button[class='btn-close']"
    back_button = "button.btn.btn-outlined.w-100"

    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)

    def test_add_engraving(self):
        try:
            self.timeout(2000)
            self.click(self.engraving_input)
            self.fill(self.engraving_input, self.new_engraving_text)
            self.click(self.monotype_font)
            #self.screenshot.take_Page_screenshot("ENGRAVING_BEFORE_SUBMIT")
            self.click(self.submit_button)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("ENGRAVING_AFTER_SUBMIT")
        except:
            logger.error(f"*****[{self.COUNTRY}-PDP] NOT ABLE TO ADD PRODUCT WITH ENGRAVING..*****")

    def test_update_engraving(self):
        try:
            self.timeout(2000)
            self.click(self.engraving_input)
            self.fill(self.engraving_input, self.update_engraving_text)
            self.click(self.arial_font)
            #self.screenshot.take_Page_screenshot("ENGRAVING_BEFORE_UPDATE")
            self.click(self.update_button)
            self.timeout(2000)
            #self.screenshot.take_Page_screenshot("ENGRAVING_AFTER_UPDATE")
        except:
            logger.error(f"*****[{self.COUNTRY}-PDP] NOT ABLE TO UPDATE ENGRAVING TEXT..*****")

    def test_close_engraving_screen(self):
        try:
            self.timeout(2000)
            self.click(self.engraving_input)
            self.click(self.close_icon)
            self.timeout(2000)
            logger.info(f"[{self.COUNTRY}-PDP] ENGRAVING MODAL IS CLOSED SUCCESSFULLY..")
            #self.screenshot.take_Page_screenshot("ENGRAVING_CLOSE")
        except:
            logger.error("*****[PDP] NOT ABLE TO CLOSE ENGRAVING MODAL..*****")

    def test_back_button_engraving_screen(self):
        try:
            self.timeout(2000)
            self.click(self.engraving_input)
            self.click(self.back_button)
            self.timeout(2000)
            logger.info(f"[{self.COUNTRY}-PDP] ENGRAVING MODAL IS CLOSED SUCCESSFULLY..")
            #self.screenshot.take_Page_screenshot("ENGRAVING_BACK")
        except:
            logger.error("*****[PDP] NOT ABLE TO CLICK BACK BUTTON ON THE ENGRAVING SCREEN..*****")

