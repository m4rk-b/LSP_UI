from dotenv import load_dotenv
import os
from seleniumbase import BaseCase
from utils import utilities
from utils.utilities import Utils
from modules.settings import SettingsModule


class HomeTest(BaseCase):
    def setUp(self):
        super().setUp()

    def initialize_test(self):
        load_dotenv()
        url = os.getenv("LSP_URL")
        username = os.getenv("LSP_USERNAME")
        password = os.getenv("LSP_PASSWORD")

        self.maximize_window()
        self.open(url)
        self.send_keys("//input[@id='username']", username)
        self.send_keys("//input[@id='pass']", password)
        self.click("//button[@title = 'Sign in']")

    def select_ae_to_test(self, accounting_entity):
        self.click("//div[@data-mgcompname = 'AEDroplist']//div[@aria-label = 'Open']")
        self.click(f"//div[@data-mgcompname = 'AEDroplist']//ul/table//td[contains(text(), '{accounting_entity}')]", "xpath")

    def settings_contact_master(self, test_text):
        self.utils.switch_to_cards_frame()

        self.click("//div//h4[contains(text(), 'Contact Master')]")

        self.utils.switch_to_main_frame()
        self.utils.wait_for_loading_invisible()
        #ADD
        self.utils.click_button("AddButton")
        self.utils.input_text("NameChildFormEdit", test_text)
        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")
        #MODIFY
        self.utils.table(test_text)
        self.utils.click_button("ModifyButton")
        self.utils.clear_input("NameChildFormEdit")
        self.utils.input_text("NameChildFormEdit", f"MOD{test_text}")
        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")
        #DELETE
        self.utils.click_button("DeleteButton")
        self.utils.table(f"MOD{test_text}")
        self.utils.message_box("OK")
        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")

        self.utils.close_settings_form("Contacts Maintenance")

    def default_einvoice_type(self):
        print("No script added yet")

    def dte_default_code(self):
        print("No script added yet")

    def export_invoices_customs_information(self, test_text):
        self.utils.switch_to_cards_frame()

        self.click("//div//h4[contains(text(), 'Export Invoices - Customs Information')]")

        self.utils.switch_to_main_frame()
        self.utils.wait_for_loading_invisible()
        self.utils.user_control_buttons("add-button")
        self.utils.switch_to_main_frame()

        #For combobox inputs
        button_click = "save-button"
        combobox_value = self.utils.combobox_input("FormCollectionGrid", "InvoiceIDComboBox")
        if combobox_value == "":
            button_click = "cancel-button"
        self.utils.user_control_buttons(button_click)
        #end----------------

        self.utils.close_settings_form("Export Invoices - Customs Information")

    def settings_page(self):
        # Menu
        self.utils.switch_to_menu_frame()
        self.click("//ul[@id = 'accordion2']//a[contains(text(), 'Settings')]", "xpath", 5)

        self.settings_contact_master("TESTNAME")
        self.export_invoices_customs_information("TEST")


    def test_home_page(self):
        self.initialize_test()

        self.utils = Utils(self)

        self.utils.switch_to_main_frame()
        self.utils.wait_for_loading_invisible()

        self.select_ae_to_test("CL_M3")

        self.settings_page()


