from datetime import datetime
import random

from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
from pages.store_locator import Search_Locator_Page
from dotenv import load_dotenv
import os
import logging

load_dotenv(override=True)
logger = logging.getLogger(__name__)

class Book_Appointment(BasePage):
    COUNTRY = os.getenv("LOCALE").upper()
    ENV = os.getenv("ENVIRONMENT").upper()
    EMAIL = os.getenv("USERNAME")

    #Appointment Types
    in_store_appointment_type= "//label[@for='input-inStore']"
    virtual_appointment_type= "//label[@for='input-virtual']"

    #Services List
    service_list = "//div[@id='collapseTwo']//label[not(contains(@class,'d-none'))]"

    #Service Details List:
    service_detail_list = "//div[@id='collapseThree']//label[not(contains(@class,'d-none'))]"

    #Stores
    search_store_input = "#clientservices-store-address"
    book_appointment_first_store = "(//div[contains(@class,'closest-addresses')]//label)[1]"

    #Calendar
    available_date = "td.day.selectable"
    selected_date = "#selectedDate"
    available_timeslot = "#timeslots label.timeslots__time"
    selected_timeslot = "//ul[@id='timeslots']//label[contains(@class,'selectedOption')]"
    go_to_next_month = "(//i[@class='dbicon-chevron-right'])[1]"

    #Next, Back and Submit Buttons
    appointment_continue_cta = "//*[@id='nextBtn']"
    appointment_submit_cta = "//*[@id='confirmBtn']"
    appointment_back_cta = "//*[@id='backBtn']"

    #Checkboxes
    appointment_terms_checkbox = "//*[@id='termsCheckBox']"
    appointment_subscribe_checkbox = "//*[@id='subscribeCheckBox']"

    #Additional Information
    appointment_product_questions_input = "//*[@id='productQuestions']"
    appointment_questions_input = "//*[@id='questions']"

    #Step-2 page Appointment Contact details
    appointment_title_dropdown = "//*[@id='appointmentTitle']"
    appointment_title_value = "mr."
    appointment_first_name_input = "//*[@id='appointmentFirstName']"
    appointment_last_name_input = "//*[@id='appointmentLastName']"
    appointment_mobile_input = "//*[@id='appointmentPhone']"
    appointment_email_input = "//*[@id='appointmentEmail']"

    appointment_mobile_text = "8989089890"
    appointment_email_text = EMAIL

    #Edit Option
    edit_step1 = "//*[@id='editStep1']"
    edit_step2 = "//*[@id='editStep2']"
    active_step_number = "//li[contains(@class,'progress__item--active')]//div[@class='progress-indicator']"


    #Success Message Text
    success_message_text = "//*[@id='successBookingMsg']/div[1]"

    #Error Message Text
    error_message_text = "//*[@id='user-errors']"

    #Summary Info
    appointment_summary = ".appointmentSummary__info"
    user_summary = "#userSummary"
    product_question_summary = "#productQuestionsReadOnly"
    question_summary = "#questionsReadOnly"

    if COUNTRY == "US" or COUNTRY == "UK":
        # Delivery and Collector Name
        appointment_first_name_list = ["Oliver", "Jack", "Harry", "Jacob", "Charlie", "Thomas", "George", "James", "Robert"]
        appointment_last_name_list = ["Smith", "Taylor", "Brown", "Williams", "Wilson", "Evans", "Robinson", "Walker", "Thompson", "Brook"]
        appointment_product_question_text = "[THIS IS A TESTING RECORD. PLEASE IGNORE] I would like to request additional information about High Jewellery products offered by De Beers."
        appointment_question_text = "[THIS IS A TESTING RECORD. PLEASE IGNORE] I would like to request additional information about other products offered by De Beers."

    elif COUNTRY == "FR":
        # Delivery and Collector Name
        appointment_first_name_list = ["Gabriel", "Raphaël", "Louis", "Arthur", "Léon", "Léo", "Oscar", "Adam", "Noah"]
        appointment_last_name_list = ["Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Michel", "Roux", "Laurent", "Garcia"]
        appointment_product_question_text = "[THIS IS A TESTING RECORD. PLEASE IGNORE] Je souhaite obtenir des informations complémentaires sur les produits de Haute Joaillerie proposés par De Beers."
        appointment_question_text = "[THIS IS A TESTING RECORD. PLEASE IGNORE] Je souhaite obtenir des informations complémentaires sur les autres produits proposés par De Beers."

    elif COUNTRY == "HK" or COUNTRY == "TW" or COUNTRY == "MO":
        # Delivery and Collector Name
        appointment_first_name_list = ["Yan", "Yee", "Wah", "Ming", "Mei", "Man", "Kwong", "Kei", "Ho"]
        appointment_last_name_list = ["Chan", "Wong", "Lee", "Leung", "Ho", "Cheung", "Lam", "Lau", "Tang", "Yeung"]
        appointment_product_question_text = "[THIS IS A TESTING RECORD. PLEASE IGNORE] 我想了解更多关于戴比尔斯高级珠宝产品的信息."
        appointment_question_text = "[THIS IS A TESTING RECORD. PLEASE IGNORE] 我想了解一下戴比尔斯公司提供的其他产品信息."


    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)
        self.store_locator = Search_Locator_Page(page)


    def test_in_store_appointment_type(self):
        try:
            step_number = self.page.locator(self.active_step_number).inner_text().strip()
            logger.info(f"CURRENT ACTIVE STEP: {step_number}")
            self.timeout(2000)
            self.scroll_down(self.in_store_appointment_type)
            self.click(self.in_store_appointment_type)
            self.timeout(2000)
            service = self.page.locator(self.service_list)
            service.nth(random.randrange(service.count())).click()
            self.timeout(2000)
            service_detail = self.page.locator(self.service_detail_list)
            service_detail.nth(random.randrange(3)).click()  # Select anyone service from first 3 records
            self.timeout(2000)
            if self.COUNTRY == "US":
                self.fill(self.search_store_input, "")
                self.fill(self.search_store_input, "New York")
                self.press(self.search_store_input, "Enter")
                self.timeout(2000)
                self.scroll_down(self.store_locator.new_york_madison_avenue_map_marker)
                self.store_locator.test_click_close_new_york_madison_avenue_in_map()
            elif self.COUNTRY == "UK":
                self.scroll_down(self.store_locator.london_old_bond_street_map_marker)
                self.store_locator.test_click_close_london_marker_in_map()
            elif self.COUNTRY == "FR":
                self.scroll_down(self.store_locator.paris_flagship_store_map_marker)
                self.store_locator.test_click_close_paris_flagship_in_map()
            self.timeout(2000)
            self.click(self.book_appointment_first_store)
            logger.info("[IN STORE APPOINTMENT] ALL OPTIONS ARE SELECTED..")
        except:
            logger.error("*****[IN STORE APPOINTMENT] ALL OPTIONS ARE NOT SELECTED..*****")

    def test_bb_in_store_appointment_type(self):
        try:
            step_number = self.page.locator(self.active_step_number).inner_text().strip()
            logger.info(f"CURRENT ACTIVE STEP: {step_number}")
            self.timeout(2000)
            service = self.page.locator(self.service_list)
            service.nth(random.randrange(service.count())).click()
            self.timeout(2000)
            service_detail = self.page.locator(self.service_detail_list)
            service_detail.nth(random.randrange(3)).click() # Select anyone service from first 3 records
            self.timeout(2000)
            if self.COUNTRY == "US":
                self.fill(self.search_store_input, "")
                self.fill(self.search_store_input, "New York")
                self.press(self.search_store_input, "Enter")
                self.scroll_down(self.store_locator.new_york_madison_avenue_map_marker)
                self.store_locator.test_click_close_new_york_madison_avenue_in_map()
            elif self.COUNTRY == "UK":
                self.scroll_down(self.store_locator.london_old_bond_street_map_marker)
                self.store_locator.test_click_close_london_marker_in_map()
            elif self.COUNTRY == "FR":
                self.scroll_down(self.store_locator.paris_flagship_store_map_marker)
                self.store_locator.test_click_close_paris_flagship_in_map()
            self.timeout(2000)
            self.click(self.book_appointment_first_store)
            logger.info("[BB IN STORE APPOINTMENT] ALL OPTIONS ARE SELECTED..")
        except:
            logger.error("*****[BB IN STORE APPOINTMENT] ALL OPTIONS ARE NOT SELECTED..*****")


    def test_virtual_appointment_type(self):
        try:
            step_number = self.page.locator(self.active_step_number).inner_text().strip()
            logger.info(f"CURRENT ACTIVE STEP: {step_number}")
            self.timeout(2000)
            self.scroll_down(self.virtual_appointment_type)
            self.click(self.virtual_appointment_type)
            self.timeout(2000)
            service = self.page.locator(self.service_list)
            service.nth(random.randrange(service.count())).click()
            self.timeout(2000)
            service_detail = self.page.locator(self.service_detail_list)
            service_detail.nth(random.randrange(3)).click() # Select anyone service from first 3 records
            self.timeout(2000)
            if self.COUNTRY == "US":
                self.fill(self.search_store_input, "")
                self.fill(self.search_store_input, "New York")
                self.press(self.search_store_input, "Enter")
                self.timeout(2000)
                self.scroll_down(self.store_locator.new_york_madison_avenue_map_marker)
                self.store_locator.test_click_close_new_york_madison_avenue_in_map()
            elif self.COUNTRY == "UK":
                self.scroll_down(self.store_locator.london_old_bond_street_map_marker)
                self.store_locator.test_click_close_london_marker_in_map()
            elif self.COUNTRY == "FR":
                self.scroll_down(self.store_locator.paris_flagship_store_map_marker)
                self.store_locator.test_click_close_paris_flagship_in_map()
            self.timeout(2000)
            self.click(self.book_appointment_first_store)

            logger.info("[VIRTUAL APPOINTMENT] ALL OPTIONS ARE SELECTED..")
        except:
            logger.error("*****[VIRTUAL APPOINTMENT] ALL OPTIONS ARE NOT SELECTED..*****")

    def test_bb_virtual_appointment_type(self):
        try:
            step_number = self.page.locator(self.active_step_number).inner_text().strip()
            logger.info(f"CURRENT ACTIVE STEP: {step_number}")
            self.timeout(2000)
            service = self.page.locator(self.service_list)
            service.nth(random.randrange(service.count())).click()
            self.timeout(2000)
            service_detail = self.page.locator(self.service_detail_list)
            service_detail.nth(random.randrange(3)).click()  # Select anyone service from first 3 records
            self.timeout(2000)
            if self.COUNTRY == "US":
                self.fill(self.search_store_input, "")
                self.fill(self.search_store_input, "New York")
                self.press(self.search_store_input, "Enter")
                self.scroll_down(self.store_locator.new_york_madison_avenue_map_marker)
                self.store_locator.test_click_close_new_york_madison_avenue_in_map()
            elif self.COUNTRY == "UK":
                self.scroll_down(self.store_locator.london_old_bond_street_map_marker)
                self.store_locator.test_click_close_london_marker_in_map()
            elif self.COUNTRY == "FR":
                self.scroll_down(self.store_locator.paris_flagship_store_map_marker)
                self.store_locator.test_click_close_paris_flagship_in_map()
            self.timeout(2000)
            self.click(self.book_appointment_first_store)
            logger.info("[BB VIRTUAL APPOINTMENT] ALL OPTIONS ARE SELECTED..")
        except:
            logger.error("*****[BB VIRTUAL APPOINTMENT] ALL OPTIONS ARE NOT SELECTED..*****")

    def test_step1_select_date_time(self):
        try:
            if datetime.now().day > 20: # Go to next month if today's date is more than 20
                self.click(self.go_to_next_month)
                self.timeout(3000)
            dates = self.page.locator(self.available_date)
            total = dates.count()
            for i in range(total):
                date = dates.nth(i)
                # Scroll + click
                date.scroll_into_view_if_needed()
                date.click()
                self.timeout(2000)
                selected_date_text = self.get_text(self.selected_date).strip()
                logger.info(f"[{self.ENV}-{self.COUNTRY}] SELECTED DATE: {selected_date_text.upper()}")

                self.timeout(2000)

                # Check if "no slots" message is visible
                if self.page.locator("#noSlots:not(.d-none)").is_visible():
                    logger.warning(f"[{self.ENV}-{self.COUNTRY}] NO TIME SLOTS FOUND FOR THE SELECTED DATE: {selected_date_text.upper()}, RETRYING NEXT..")
                    continue  # try next date

                # Get available timeslots
                timeslots = self.page.locator(self.available_timeslot)

                if timeslots.count() > 0:
                    timeslots.first.click()
                    self.timeout(2000)
                    selected_timeslot_text = self.get_text(self.selected_timeslot).strip()
                    logger.info(f"[{self.ENV}-{self.COUNTRY}] SELECTED TIME: {selected_timeslot_text}")
                    return True

                # Safety fallback (rare case)
                logger.error(f"[{self.ENV}-{self.COUNTRY}] NO TIME SLOTS FOUND FOR THE SELECTED DATE: {selected_date_text.upper()}, RETRYING NEXT..")

                self.timeout(2000)

                # If loop completes
            raise Exception(f"*****[{self.ENV}-{self.COUNTRY}] NO AVAILABLE DATES WITH TIME SLOTS FOUND..*****")
        except Exception as e:
            logger.error(e)

    def test_step2_enter_contact_details(self):
        try:
            self.timeout(1000)
            appointment_first_name_text = random.choice(self.appointment_first_name_list)
            appointment_last_name_text = random.choice(self.appointment_last_name_list)
            self.select_option(self.appointment_title_dropdown, self.appointment_title_value)
            self.fill(self.appointment_first_name_input, appointment_first_name_text)
            self.fill(self.appointment_last_name_input, appointment_last_name_text)
            self.fill(self.appointment_mobile_input, self.appointment_mobile_text)
            self.fill(self.appointment_email_input, self.appointment_email_text)
            logger.info("[APPOINTMENT-STEP2] CONTACT DETAILS ARE ENTERED..")
        except:
            logger.error("*****[APPOINTMENT-STEP2] NOT ABLE TO ENTER CONTACT DETAILS..*****")

    def test_step3_enter_additional_information(self):
        try:
            self.timeout(1000)
            self.fill(self.appointment_product_questions_input, self.appointment_product_question_text)
            self.fill(self.appointment_questions_input, self.appointment_question_text)
            logger.info("[APPOINTMENT-STEP3] ADDITIONAL INFORMATION DETAILS ARE ENTERED..")
        except:
            logger.error("*****[APPOINTMENT-STEP3] NOT ABLE TO ENTER ADDITIONAL INFORMATION DETAILS..*****")

    def test_step3_select_checkboxes(self):
        try:
            self.timeout(1000)
            if self.is_checked(self.appointment_subscribe_checkbox):
                logger.info("[APPOINTMENT-STEP3] NEWSLETTER SUBSCRIPTION CHECKBOX IS ALREADY SELECTED..")
                if self.is_checked(self.appointment_terms_checkbox):
                    logger.info("[APPOINTMENT-STEP3] TERMS AND CONDITIONS CHECKBOX IS ALREADY SELECTED..")
                else:
                    self.click(self.appointment_terms_checkbox)
                    logger.info("[APPOINTMENT-STEP3] TERMS AND CONDITIONS CHECKBOX IS NOW CHECKED..")
            else:
                self.click(self.appointment_subscribe_checkbox)
                logger.info("[APPOINTMENT-STEP3] NEWSLETTER SUBSCRIPTION CHECKBOX IS NOW CHECKED..")
                if self.is_checked(self.appointment_terms_checkbox):
                    logger.info("[APPOINTMENT-STEP3] TERMS AND CONDITIONS CHECKBOX IS ALREADY SELECTED..")
                else:
                    self.click(self.appointment_terms_checkbox)
                    logger.info("[APPOINTMENT-STEP3] TERMS AND CONDITIONS CHECKBOX IS NOW CHECKED..")
        except:
            logger.error("*****[APPOINTMENT-STEP3] NEWSLETTER SUBSCRIPTION AND TERMS CHECKBOXES ARE NOT CHECKED..*****")

    def test_click_on_continue_cta(self):
        try:
            self.timeout(1000)
            self.click(self.appointment_continue_cta)
            self.timeout(3000)
            logger.info(f"[{self.ENV}-{self.COUNTRY}] USER IS NAVIGATED TO THE NEXT STEP..")
            appointment_summary_text = self.get_text(self.appointment_summary)

            clean_appointment_summary_text = "\n".join(
                line.replace("\n", " ").strip()
                for line in appointment_summary_text.splitlines()
                if line.strip()
            )
            step_number = self.page.locator(self.active_step_number).inner_text().strip()
            logger.info(f"[{self.ENV}-{self.COUNTRY}] CURRENT ACTIVE STEP: {step_number}")
            logger.info(f"[{self.ENV}-{self.COUNTRY}] APPOINTMENT SUMMARY:\n{clean_appointment_summary_text.upper()}")

        except Exception as e:
            logger.error(e)

    def test_click_on_submit_cta(self):
        try:
            self.timeout(1000)
            self.click(self.appointment_submit_cta)
            self.timeout(5000)
            if self.is_visible(self.error_message_text):
                error_message = self.get_text(self.error_message_text).strip()
                logger.warning(
                    f"##### [APPOINTMENT-ERROR] {error_message.upper()}"
                )
                return

            if self.is_visible(self.success_message_text):
                success_message = self.get_text(self.success_message_text).strip()
                logger.info(f"##### [APPOINTMENT-SUCCESS] {success_message.upper()}")
                appointment_summary_text = self.get_text(self.appointment_summary)

                clean_appointment_summary_text = "\n".join(
                    line.replace("\n", " ").strip()
                    for line in appointment_summary_text.splitlines()
                    if line.strip()
                )
                user_summary_text = self.get_text(self.user_summary)

                clean_user_summary_text = "\n".join(
                    line.replace("\n", " ").strip()
                    for line in user_summary_text.splitlines()
                    if line.strip()
                )
                clean_user_summary_text = clean_user_summary_text.replace("\n", " ")

                product_question_summary_text = self.get_text(self.product_question_summary).strip()
                question_summary_text = self.get_text(self.question_summary).strip()

                logger.info(f"##### [{self.ENV}-{self.COUNTRY}] APPOINTMENT SUMMARY:\n{clean_appointment_summary_text.upper()}")
                logger.info(f"##### [{self.ENV}-{self.COUNTRY}] USER SUMMARY:\n{clean_user_summary_text.upper()}")
                logger.info(f"##### [{self.ENV}-{self.COUNTRY}] PRODUCT QUESTION: {product_question_summary_text.upper()}")
                logger.info(f"##### [{self.ENV}-{self.COUNTRY}] OTHER QUESTION: {question_summary_text.upper()}")
        except Exception as e:
            logger.error(e)

    def test_go_back_to_step_1_with_edit_icon(self):
        try:
            self.timeout(1000)
            self.click(self.edit_step1)
            self.timeout(3000)
            logger.info("[APPOINTMENT] USER IS REDIRECTED TO THE STEP-1 USING EDIT ICON..")
        except Exception as e:
            logger.error(e)

    def test_go_back_to_step_1_with_back_button(self):
        try:
            self.timeout(3000)
            self.click(self.appointment_back_cta)
            self.timeout(1000)
            logger.info("[APPOINTMENT] USER IS REDIRECTED TO THE STEP-1 USING BACK BUTTON..")
        except Exception as e:
            logger.error(e)

    def test_go_back_to_step_2_with_edit_icon(self):
        try:
            self.timeout(1000)
            self.click(self.edit_step2)
            self.timeout(3000)
            logger.info("[APPOINTMENT] USER IS REDIRECTED TO THE STEP-2 USING EDIT ICON..")
        except Exception as e:
            logger.error(e)

    def test_go_back_to_step_2_with_back_button(self):
        try:
            self.timeout(3000)
            self.click(self.appointment_back_cta)
            self.timeout(1000)
            logger.info("[APPOINTMENT] USER IS REDIRECTED TO THE STEP-2 USING BACK BUTTON..")
        except Exception as e:
            logger.error(e)
