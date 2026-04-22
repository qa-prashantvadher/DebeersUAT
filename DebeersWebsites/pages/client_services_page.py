from pages.base_page import BasePage
from pages.take_screenshot import PageScreenshot
import os
from dotenv import load_dotenv
load_dotenv(override=True)

class Client_Services_Page(BasePage):
    ENV = os.getenv("ENVIRONMENT").upper()
    COUNTRY = os.getenv("LOCALE").upper()

    first_name_text = "Prashant"
    last_name_text = "Vadher"
    phone_number_text = "8989089890"
    #country_code_text = "44"
    email_address_text = os.getenv("USERNAME")


    client_service_email_cta = "a[data-bs-target='#contactUsModal']"
    client_service_request_call_cta = "//*[@id='requestCall']"
    client_service_region_dropdown = "//select[@class='csCountrySelector form-element__select services-country-selector__select']"
    client_service_quick_links = "//[class='services-quick-links service-quick-links']"
    region = ['AU', 'AT', 'BE', 'CA', 'CN', 'FR', 'DE', 'GR', 'HK', 'IT', 'MO', 'NL', 'SE', 'TW', 'GB', 'US']

    close_chat = "//*[@id='headerCloseButton-42']"

    #Email US
    email_title_dropdown = "//*[@id='contactus-select-title']"
    email_title_value = 'mr.'
    email_first_name = "//*[@id='contactus-form-firstname']"
    email_last_name = "//*[@id='contactus-form-lastname']"
    email_country_code = "//*[@id='contactus-form-countryCodePhone']"
    email_phone_number = "//*[@id='contactus-form-contactnumber']"
    email_email_address = "//*[@id='contactUsEmailAddress']"
    email_reason_dropdown = "#reasonForContact"
    email_appointment_reason = "appointment"
    email_message = "//*[@id='productQuestions']"
    email_submit = "//*[@id='recaptchaContactUsSubmit']"
    email_close = "//div[@id='contactUsModal']//i[@class='close-icon dbicon-close']"

    #Call Request
    call_request_title_dropdown = "//*[@id='callRequestTitle']"
    call_request_title_value = 'mr.'
    callback_first_name="//*[@id='callback-form-firstname']"
    callback_last_name="//*[@id='callback-form-lastname']"
    callback_country_code="//*[@id='callback-form-countryCodePhone']"
    callback_phone_number="//*[@id='callback-form-contactnumber']"
    callback_reason_dropdown = "#reasonForContact"
    callback_appointment_reason = "appointment"
    callback_submit = "//*[@id='recaptchaCallBackSubmit']"
    callback_close = "//div[@id='callBackModal']//i[@class='close-icon dbicon-close']"

    email_call_email_us_button = "(//*[@id='contactUsButton'])[1]"
    email_call__call_request_button = "(//*[@id='callback'])[1]"
    email__call_book_appointment_button = "//*[@id='arrangeViewingButton']"
    email_call_faq_button = "(//*[@id='FAQButton'])[1]"


    def __init__(self, page):
        super().__init__(page)
        self.screenshot = PageScreenshot(page)

    def test_change_region_client_service(self):

        for region_value in self.region:
            try:
                self.select_option(self.client_service_region_dropdown, region_value)
                self.timeout(3000)
                print(f"[CLIENT SERVICE] PAGE IS DISPLAYED WITH THE SELECTED REGION = {region_value}")
                #self.screenshot.take_Page_screenshot(f"CLIENT_SERVICE_CHANGE_REGION_{region_value}")
            except:
                print("*****[CLIENT SERVICE] NOT ABLE TO CHANGE REGION DETAILS..*****")

    def test_open_email_us_form_from_client_services(self):
        try:
            self.click(self.client_service_email_cta)
            self.timeout(2000)
            print("[CLIENT SERVICES] EMAIL US POPUP IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("EMAIL_US")
        except:
            print("*****[CLIENT SERVICES] NOT ABLE TO CLICK EMAIL US CTA..*****")

    def test_open_callback_form_from_client_services(self):
        try:
            self.click(self.client_service_request_call_cta)
            self.timeout(2000)
            print("[CLIENT SERVICES] CALL REQUEST POPUP IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("CALL_REQUEST")
        except:
            print("*****[CLIENT SERVICES] NOT ABLE TO CLICK REQUEST A CALL CTA..*****")

    def test_open_call_request_form_email_call(self):
        try:
            self.click(self.email_call__call_request_button)
            self.timeout(2000)
            print("[EMAIL/CALL REQUEST] CALL REQUEST POPUP IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("EMAIL_CALl_FORM_CALL_REQUEST")
        except:
            print("*****[EMAIL/CALL REQUEST] NOT ABLE TO CLICK REQUEST A CALL CTA..*****")

    def test_open_email_us_form_from_email_call(self):
        try:
            self.click(self.email_call_email_us_button)
            self.timeout(2000)
            print("[EMAIL/CALL REQUEST] EMAIL US POPUP IS NOW VISIBLE..")
            #self.screenshot.take_Page_screenshot("EMAIL_CALl_FORM__EMAIL_US")
        except:
            print("*****[EMAIL/CALL REQUEST] NOT ABLE TO CLICK CONTACT US CTA..*****")

    def test_open_book_an_appointment_from_email_call(self):
        try:
            self.click(self.email__call_book_appointment_button)
            self.timeout(2000)
            print("[EMAIL/CALL REQUEST] USER IS REDIRECTED TO THE BOOK AN APPOINTMENT PAGE..")
            #self.screenshot.take_Page_screenshot("EMAIL_CALl_FORM_BOOK_APPOINTMENT")
        except:
            print("*****[EMAIL/CALL REQUEST] USER IS NOT REDIRECTED TO THE BOOK AN APPOINTMENT PAGE..*****")

    def test_open_faq_from_email_call(self):
        try:
            self.click(self.email_call_faq_button)
            self.timeout(2000)
            print("[EMAIL/CALL REQUEST] USER IS REDIRECTED TO THE FAQ PAGE..")
            #self.screenshot.take_Page_screenshot("EMAIL_CALl_FORM_FAQ")
        except:
            print("*****[EMAIL/CALL REQUEST] USER IS NOT REDIRECTED TO THE BOOK AN APPOINTMENT PAGE..*****")


    def test_email_us_form(self):
        try:
            self.select_option(self.email_title_dropdown,self.email_title_value)
            self.fill(self.email_first_name,self.first_name_text)
            self.fill(self.email_last_name, self.last_name_text)
            #self.fill(self.email_country_code, self.country_code_text)
            self.fill(self.email_phone_number, self.phone_number_text)
            self.fill(self.email_email_address, self.email_address_text)
            self.select_option(self.email_reason_dropdown, self.email_appointment_reason)
            if self.COUNTRY == "FR":
                self.fill(self.email_message,f"[{self.COUNTRY}-{self.ENV}] [TESTING RECORD] JE SUIS INTÉRESSÉ PAR LA CRÉATION D'UNE BAGUE DE FIANÇAILLES PERSONNALISÉE ET JE SOUHAITE OBTENIR UN DEVIS. JE RECHERCHE UNE FORME XXXXX, PIERRE CENTRALE, ENVIRON X,XX CARATS...")
            elif self.COUNTRY == "HK":
                self.fill(self.email_message,f"[{self.COUNTRY}-{self.ENV}] [測試記錄] 我有興趣製作客製化訂婚戒指並希望獲得報價。我正在尋找 XXXXX 形狀的主石，大約 X.XX 克拉......")
            else:
                self.fill(self.email_message,f"[{self.COUNTRY}-{self.ENV}] [TESTING RECORD] I AM INTERESTED IN CREATING A CUSTOM ENGAGEMENT RING AND WOULD LIKE TO GET A QUOTE. I AM LOOKING FOR AN XXXXX SHAPE, CENTER STONE, APPROXIMATELY X.XX CARATS...")
            self.timeout(1000)
            #self.screenshot.take_Page_screenshot("EMAIL_US_BEFORE_SUBMIT")
            self.click(self.email_submit)
            self.timeout(2000)
            print("[EMAIL US] FORM IS SUCCESSFULLY SUBMITTED..")
            self.screenshot.take_page_screenshot("EMAIL_US_SUBMIT")
        except:
            print("*****[EMAIL US] NOT ABLE TO SUBMIT EMAIL US FORM..")

    def test_close_email_us_form(self):
        try:
            self.timeout(2000)
            self.click(self.email_close)
            print("[EMAIL US] FORM IS NOW CLOSED..")
            #self.screenshot.take_Page_screenshot("EMAIL_US_CLOSE")
        except:
            print("*****[EMAIL US] NOT ABLE TO CLOSE EMAIL US FORM..*****")

    def test_callback_form(self):
        try:
            self.select_option(self.call_request_title_dropdown,self.call_request_title_value)
            self.fill(self.callback_first_name, self.first_name_text)
            self.fill(self.callback_last_name, self.last_name_text)
            #self.fill(self.callback_country_code, self.country_code_text)
            self.fill(self.callback_phone_number, self.phone_number_text)
            self.select_option(self.callback_reason_dropdown, self.callback_appointment_reason)
            self.timeout(1000)
            #self.screenshot.take_Page_screenshot("CALL_REQUEST_BEFORE_SUBMIT")
            self.click(self.callback_submit)
            self.timeout(2000)
            print("[CALL REQUEST] FORM IS SUCCESSFULLY SUBMITTED..")
            self.screenshot.take_page_screenshot("CALL_REQUEST_SUBMIT")
        except:
            print("*****[CALL REQUEST] NOT ABLE TO SUBMIT CALL REQUEST FORM..*****")


    def test_close_callback_form(self):
        try:
            self.timeout(2000)
            self.click(self.callback_close)
            print("[CALL REQUEST] FORM IS NOW CLOSED..")
            #self.screenshot.take_Page_screenshot("CALL_REQUEST_CLOSE")

        except:
            print("[CALL REQUEST] NOT ABLE TO CLOSE CALL REQUEST FORM..")