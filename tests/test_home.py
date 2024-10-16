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
        # username = os.getenv("LSP_USERNAME")
        # password = os.getenv("LSP_PASSWORD")

        self.maximize_window()
        self.open(url)
        # self.send_keys("//input[@id='username']", username)
        # self.send_keys("//input[@id='pass']", password)
        # self.click("//button[@title = 'Sign in']")

    def test_1_login(self):
        # load_dotenv()
        self.initialize_test()
        username = os.getenv("LSP_USERNAME")
        password = os.getenv("LSP_PASSWORD")
        self.send_keys("//input[@id='username']", username)
        self.send_keys("//input[@id='pass']", password)
        self.click("//button[@title = 'Sign in']")

    def select_ae_to_test(self):
        ae = os.getenv("ACCOUNTING_ENTITY")
        self.click("//div[@data-mgcompname = 'AEDroplist']//div[@aria-label = 'Open']")
        self.click(f"//div[@data-mgcompname = 'AEDroplist']//ul/table//td[contains(text(), '{ae}')]")

    def contact_master(self, test_text):
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

    def export_invoices_customs_information(self, test_text=""):
        self.utils.switch_to_cards_frame()

        self.click("//div//h4[contains(text(), 'Export Invoices - Customs Information')]")

        self.utils.switch_to_main_frame()
        self.utils.wait_for_loading_invisible()

        #ADD
        self.utils.user_control_buttons("add-button")
        self.utils.switch_to_main_frame()
        #For combobox input
        button_click = "save-button"
        combobox_value = self.utils.combobox_input("FormCollectionGrid", "InvoiceIDComboBox")
        if combobox_value == "":
            button_click = "cancel-button"
        self.utils.user_control_buttons(button_click)
        self.utils.message_box("OK")
        #end----------------

        #MODIFY
        self.utils.switch_to_main_frame()
        if combobox_value != "":
            self.utils.table(combobox_value)
            self.utils.user_control_buttons("modify-button")
            self.utils.switch_to_main_frame()
            shipping_port_code = self.utils.combobox_input("FormCollectionGrid", "ShippingPortCodeComboBox")
            self.utils.user_control_buttons("save-button")
            self.utils.message_box("OK")

        #DELETE
        self.utils.switch_to_main_frame()
        if combobox_value != "":
            self.utils.table(combobox_value)
            self.utils.user_control_buttons("delete-button")
            self.utils.switch_to_main_frame()
            self.utils.message_box("OK")
            self.utils.user_control_buttons("save-button")
            self.utils.switch_to_main_frame()
            self.utils.message_box("OK")

        self.utils.close_settings_form("Export Invoices - Customs Information")

    def industry_maintenance(self, test_text):
        self.utils.switch_to_cards_frame()

        self.click("//div//h4[contains(text(), 'Industry Maintenance')]")

        self.utils.switch_to_main_frame()
        self.utils.wait_for_loading_invisible()

        #ADD
        self.utils.click_button("AddButton")
        self.utils.input_text("IdentifierEdit", test_text)
        type_edit = self.utils.combobox_input("CarrierDriverInformationGrid", "TypeEdit")
        self.utils.input_text("IndustryEdit", test_text)
        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")

        #MODIFY
        self.utils.table(test_text)
        self.utils.click_button("ModifyButton")
        self.utils.clear_input("IdentifierEdit")
        self.utils.input_text("IdentifierEdit", f"MOD{test_text}")
        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")

        #DELETE
        self.utils.table(f"MOD{test_text}")
        self.utils.click_button("DeleteButton")
        self.utils.message_box("OK")
        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")

        self.utils.close_settings_form("Industry Maintenance")

    def invoice_translation_maintenance(self, test_text):
        self.utils.switch_to_cards_frame()

        self.click("//div//h4[contains(text(), 'Invoice Translation Maintenance')]")

        self.utils.switch_to_main_frame()
        self.utils.wait_for_loading_invisible()

        self.utils.translation_maintenance_combobox("Documentos Tributarios Electronicos (DTE)", "Tax Code")

        #ADD
        self.utils.click_button("AddButton")
        self.utils.input_text("ERPCodeEdit", test_text)
        standard_code = self.utils.combobox_input("StandardCodeGrid", "StandardCodeComboBox")
        self.utils.message_box("YES")
        standard_code = self.utils.combobox_input("StandardCodeGrid", "StandardCodeComboBox")

        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")

        #MODIFY
        self.utils.table(test_text)
        self.utils.click_button("ModifyButton")
        self.utils.input_textarea("SubscriberCodeDescriptionEdit", f"MOD{test_text}")
        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")

        #DELETE
        self.utils.table(test_text)
        self.utils.click_button("DeleteButton")
        self.utils.message_box("OK")
        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")

        self.utils.close_settings_form("", "LCSTranslationMaintenanceGroup")

    def supplementary_data_setup(self):
        print("No scenarios yet")

    def supplementary_data_old(self):
        print("No scenarios yet")

    def test_settings_page(self):
        self.initialize_test()

        self.utils = Utils(self)

        self.utils.switch_to_main_frame()
        self.utils.wait_for_loading_invisible()

        self.select_ae_to_test()
        # Menu
        self.utils.switch_to_menu_frame()
        self.click("//ul[@id = 'accordion2']//a[contains(text(), 'Settings')]", "xpath", 5)

        self.contact_master("TESTNAME")
        self.export_invoices_customs_information()
        self.industry_maintenance("TESTINDUSTRY")
        self.invoice_translation_maintenance("TESTSUBCODE")

    def home_page(self):
        self.initialize_test()

        self.utils = Utils(self)

        self.utils.switch_to_main_frame()
        self.utils.wait_for_loading_invisible()

        self.select_ae_to_test()

        self.settings_page()


