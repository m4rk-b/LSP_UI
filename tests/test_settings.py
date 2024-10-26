from unittest import skip
from dotenv import load_dotenv
import os
from seleniumbase import BaseCase
from utils import utilities
from utils.utilities import Utils
from modules.settings import SettingsModule


class HomeTest(BaseCase):
    def setUp(self):
        super().setUp()

    def test_1_login(self):
        self.utils = Utils(self)
        self.utils.initialize_test()
        username = os.getenv("LSP_USERNAME")
        password = os.getenv("LSP_PASSWORD")
        self.send_keys("//input[@id='username']", username)
        self.send_keys("//input[@id='pass']", password)
        self.click("//button[@title = 'Sign in']")
        self.utils.wait_for_home_to_load()

    @skip
    def test_contact_master(self, test_text="TESTNAME"):
        settings_card_title = "Contact Master"
        modified_text = f"MOD{test_text}"
        self.settings_page()

        self.utils.click_settings_card(settings_card_title)

        self.utils.switch_to_main_frame()
        self.utils.wait_for_loading_invisible()
        #ADD
        self.utils.click_button("AddButton")
        self.utils.input_text(settings_card_title, "name", test_text)
        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")

        #MODIFY
        self.utils.table(test_text)
        self.utils.click_button("ModifyButton")
        # self.utils.clear_input("NameChildFormEdit")
        # self.utils.input_text("NameChildFormEdit", f"MOD{test_text}")
        self.utils.input_text(settings_card_title, "name", modified_text)
        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")

        #DELETE
        self.utils.click_button("DeleteButton")
        self.utils.table(modified_text)
        self.utils.message_box("OK")
        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")

        self.utils.close_settings_form("Contacts Maintenance")

    @skip
    def default_einvoice_type(self):
        print("No script added yet")

    @skip
    def dte_default_code(self):
        print("No script added yet")

    @skip
    def test_export_invoices_customs_information(self):
        self.settings_page()
        settings_card_title = "Export Invoices - Customs Information"
        self.utils.click_settings_card(settings_card_title)

        self.utils.switch_to_main_frame()
        self.utils.wait_for_loading_invisible()

        #ADD
        self.utils.user_control_buttons("add-button")
        self.utils.switch_to_main_frame()
        #For combobox input
        button_click = "save-button"
        combobox_value = self.utils.input_text(settings_card_title, "invoice_id")
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
            shipping_port_code = self.utils.input_text(settings_card_title, "shipping_port_code")
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

    # @skip
    def test_industry_maintenance(self, test_text="TESTIND"):
        self.settings_page()
        settings_card_title = "Industry Maintenance"
        self.utils.click_settings_card(settings_card_title)

        self.utils.switch_to_main_frame()
        self.utils.wait_for_loading_invisible()

        #ADD
        self.utils.click_button("AddButton")
        # self.utils.input_text("IdentifierEdit", test_text)
        # self.utils.input_text(settings_card_title)
        # type_edit = self.utils.combobox_input("CarrierDriverInformationGrid", "TypeEdit")
        self.utils.input_text(settings_card_title, "identifier")
        self.utils.input_text(settings_card_title, "type")
        self.utils.input_text(settings_card_title, "industry")
        # self.utils.input_text("IndustryEdit", test_text)
        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")

        #MODIFY
        self.utils.table(test_text)
        self.utils.click_button("ModifyButton")
        # self.utils.clear_input("IdentifierEdit")
        # self.utils.input_text("IdentifierEdit", f"MOD{test_text}")
        self.utils.input_text(settings_card_title, "identifier", f"MOD{test_text}")
        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")

        #DELETE
        self.utils.table(f"MOD{test_text}")
        self.utils.click_button("DeleteButton")
        self.utils.message_box("OK")
        self.utils.click_button("SaveButton")
        self.utils.message_box("OK")

        self.utils.close_settings_form("Industry Maintenance")

    # @skip
    # def test_invoice_translation_maintenance(self, test_text="TESTTAX"):
    #     self.settings_page()
    #     self.utils.click_settings_card("Invoice Translation Maintenance")
    #
    #     self.utils.switch_to_main_frame()
    #     self.utils.wait_for_loading_invisible()
    #
    #     self.utils.translation_maintenance_combobox("Documentos Tributarios Electronicos (DTE)", "Tax Code")
    #
    #     #ADD
    #     self.utils.click_button("AddButton")
    #     self.utils.input_text("ERPCodeEdit", test_text)
    #     standard_code = self.utils.combobox_input("StandardCodeGrid", "StandardCodeComboBox")
    #     self.utils.message_box("YES")
    #     standard_code = self.utils.combobox_input("StandardCodeGrid", "StandardCodeComboBox")
    #
    #     self.utils.click_button("SaveButton")
    #     self.utils.message_box("OK")
    #
    #     #MODIFY
    #     self.utils.table(test_text)
    #     self.utils.click_button("ModifyButton")
    #     self.utils.input_textarea("SubscriberCodeDescriptionEdit", f"MOD{test_text}")
    #     self.utils.click_button("SaveButton")
    #     self.utils.message_box("OK")
    #
    #     #DELETE
    #     self.utils.table(test_text)
    #     self.utils.click_button("DeleteButton")
    #     self.utils.message_box("OK")
    #     self.utils.click_button("SaveButton")
    #     self.utils.message_box("OK")
    #
    #     self.utils.close_settings_form("", "LCSTranslationMaintenanceGroup")

    # @skip
    # def test_supplementary_data_setup(self, test_text="TESTSD"):
    #     self.settings_page()
    #     self.utils.click_settings_card("Supplementary Data Setup")
    #
    #     self.utils.switch_to_main_frame()
    #     self.utils.wait_for_loading_invisible()
    #
    #     #ADD
    #     self.utils.click_button("AddButton")
    #     self.utils.input_text("NameEdit", test_text)
    #     version = "1.0"
    #     self.utils.input_text("VersionEdit", version)
    #     self.utils.upload_file("TEST.xsl")
    #     self.utils.click_button("SaveButton")
    #     self.utils.message_box("OK")
    #
    #     #ADD User Defined Fields
    #     self.utils.table(test_text, "AddendaGrid")
    #     user_defined = "TestUDF"
    #     self.utils.click_button("AddUserDefinedButton")
    #     self.utils.input_text("UserDefinedFieldEdit", user_defined)
    #     self.utils.click_button("SaveButton")
    #
    #     #MODIFY User Defined Fields
    #     self.utils.table(test_text, "AddendaGrid")
    #     self.utils.table(user_defined, "UserDefinedGrid")
    #     self.utils.click_button("ModifyUserDefinedButton")
    #     self.utils.clear_input("UserDefinedFieldEdit")
    #     self.utils.input_text("UserDefinedFieldEdit", f"MOD{user_defined}")
    #     self.utils.message_box("YES")
    #     self.utils.click_button("SaveButton")
    #
    #     #DELETE User Defined Fields
    #     self.utils.table(test_text, "AddendaGrid")
    #     self.utils.table(f"MOD{user_defined}", "UserDefinedGrid")
    #     self.utils.click_button("UserDefinedButton")
    #     self.utils.message_box("OK")
    #     self.utils.click_button("SaveButton")
    #
    #     #MODIFY
    #     self.utils.table(test_text, "AddendaGrid")
    #     self.utils.click_button("ModifyButton")
    #     self.utils.clear_input("NameEdit")
    #     self.utils.input_text("NameEdit", f"MOD{test_text}")
    #     self.utils.click_button("SaveButton")
    #     self.utils.message_box("OK")
    #
    #     #DELETE
    #     self.utils.table(f"MOD{test_text}", "AddendaGrid")
    #     self.utils.click_button("UserDefinedButton")
    #     self.utils.message_box("OK")
    #     self.utils.click_button("SaveButton")
    #
    #     self.utils.table(f"MOD{test_text}", "AddendaGrid")
    #     self.utils.click_button("DeleteButton")
    #     self.utils.message_box("OK")
    #     self.utils.click_button("SaveButton")

    # @skip
    # def test_supplementary_data_old(self, test_text="TESTSU"):
    #     self.settings_page()
    #     self.utils.click_settings_card("Supplementary Data")
    #
    #     self.utils.switch_to_main_frame()
    #     self.utils.wait_for_loading_invisible()
    #
    #     #ADD
    #     self.utils.click_button("AddButton")
    #     self.utils.input_text("CustomerIDEdit", test_text)
    #     self.utils.combobox_input("AddendaGrid", "AddendaNameVersionComboBox")
    #     self.utils.click_button("SaveButton")
    #
    #     #MODIFY
    #
    #     #DELETE
    #     self.utils.table(test_text, "AddendaGrid")
    #     self.utils.click_button("DeleteButton")
    #     self.utils.message_box("OK")
    #     self.utils.click_button("SaveButton")

    def settings_page(self):
        self.utils = Utils(self)
        self.utils.initialize_test()

        self.utils.switch_to_main_frame()
        # self.utils.wait_for_home_to_load()
        self.utils.wait_for_loading_invisible()

        self.utils.select_ae_to_test()
        # Menu
        self.utils.switch_to_menu_frame()
        self.utils.select_menu("Settings")


