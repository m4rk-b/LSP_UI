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

    # def add(self):
    #     self.utils.click_button()

    @skip
    def test_contact_master(self, test_text="TESTNAME"):
        settings_card_title = self.settings_page("Contact Master")
        modified_text = f"MOD{test_text}"

        # ADD
        self.utils.find_button_and_click("Add")
        self.utils.input_text(settings_card_title, "name", test_text)
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        # MODIFY
        self.utils.table(test_text)
        self.utils.find_button_and_click("Modify")
        self.utils.input_text(settings_card_title, "name", modified_text)
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        # DELETE
        self.utils.find_button_and_click("Delete")
        self.utils.table(modified_text)
        self.utils.message_box("OK")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        self.utils.close_settings_form("Contacts Maintenance")

    @skip
    def test_default_einvoice_type(self, input_text=None):
        settings_card_title = self.settings_page("Default eInvoice Type")

        self.utils.find_button_and_click("MODIFY")
        self.utils.input_text(settings_card_title, "einvoice_type")
        self.utils.find_button_and_click("Save")

    @skip
    def dte_default_code(self):
        print("No script added yet")

    @skip
    def test_export_invoices_customs_information(self):
        settings_card_title = self.settings_page("Export Invoices - Customs Information")

        # ADD
        # self.utils.user_control_buttons("add-button")
        self.utils.find_button_and_click("Add")
        self.utils.switch_to_main_frame()
        # For combobox input
        button_click = "Save"
        combobox_value = self.utils.input_text(settings_card_title, "invoice_id")
        if combobox_value == "":
            button_click = "Cancel"
        # self.utils.user_control_buttons(button_click)
        self.utils.find_button_and_click(button_click)
        self.utils.message_box("OK")
        # end----------------

        # MODIFY
        self.utils.switch_to_main_frame()
        if combobox_value != "":
            self.utils.table(combobox_value)
            # self.utils.user_control_buttons("modify-button")
            self.utils.find_button_and_click("Modify")
            self.utils.switch_to_main_frame()
            shipping_port_code = self.utils.input_text(settings_card_title, "shipping_port_code")
            # self.utils.user_control_buttons("save-button")
            self.utils.find_button_and_click("Save")
            self.utils.message_box("OK")

        # DELETE
        self.utils.switch_to_main_frame()
        if combobox_value != "":
            self.utils.table(combobox_value)
            # self.utils.user_control_buttons("delete-button")
            self.utils.find_button_and_click("Delete")
            self.utils.switch_to_main_frame()
            self.utils.message_box("OK")
            # self.utils.user_control_buttons("save-button")
            self.utils.find_button_and_click("Save")
            self.utils.switch_to_main_frame()
            self.utils.message_box("OK")

        self.utils.close_settings_form("Export Invoices - Customs Information")

    @skip
    def test_industry_maintenance(self, test_text="TESTIND"):
        settings_card_title = self.settings_page("Industry Maintenance")

        # ADD
        # self.utils.click_button("AddButton")
        self.utils.find_button_and_click("Add")
        self.utils.input_text(settings_card_title, "identifier")
        self.utils.input_text(settings_card_title, "type")
        self.utils.input_text(settings_card_title, "industry")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        # MODIFY
        self.utils.table(test_text)
        # self.utils.click_button("ModifyButton")
        self.utils.find_button_and_click("Modify")
        self.utils.input_text(settings_card_title, "identifier", f"MOD{test_text}")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        # DELETE
        self.utils.table(f"MOD{test_text}")
        # self.utils.click_button("DeleteButton")
        self.utils.find_button_and_click("Delete")
        self.utils.message_box("OK")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        self.utils.close_settings_form("Industry Maintenance")

    @skip
    def test_invoice_translation_maintenance(self, test_text="TESTTAX"):
        settings_card_title = self.settings_page("Invoice Translation Maintenance")

        self.utils.translation_maintenance_combobox("Documentos Tributarios Electronicos (DTE)", "Tax Code")

        # ADD
        # self.utils.click_button("AddButton")
        self.utils.find_button_and_click("Add")
        tax_code = self.utils.input_text(settings_card_title, "user_tax_code")
        # self.utils.message_box("YES")
        self.utils.input_text(settings_card_title, "standard_tax_code")

        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        # MODIFY
        self.utils.table(tax_code)
        # self.utils.click_button("ModifyButton")
        self.utils.find_button_and_click("Modify")
        # self.utils.input_textarea("SubscriberCodeDescriptionEdit", f"MOD{test_text}")
        description = self.utils.input_text(settings_card_title, "standard_code_description")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("save")
        self.utils.message_box("OK")

        # DELETE
        self.utils.table(description)
        # self.utils.click_button("DeleteButton")
        self.utils.find_button_and_click("Delete")
        self.utils.message_box("OK")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("save")
        self.utils.message_box("OK")

        self.utils.close_settings_form("", "LCSTranslationMaintenanceGroup")

    @skip
    def test_supplementary_data_setup(self):
        settings_card_title = self.settings_page("Supplementary Data Setup")

        # ADD
        self.utils.find_button_and_click("Add")
        sd_name = self.utils.input_text(settings_card_title, "supplementary_data_name")
        self.utils.input_text(settings_card_title, "version")
        self.utils.upload_file(settings_card_title, "TEST.xsl")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        # ADD User Defined Fields
        self.utils.table(sd_name, "AddendaGrid")
        self.utils.find_button_and_click("Add", "sd")
        user_defined = self.utils.input_text(settings_card_title, "user_define_field")
        self.utils.click_button("SaveButton")

        # MODIFY User Defined Fields
        self.utils.table(sd_name, "AddendaGrid")
        self.utils.table(user_defined, "UserDefinedGrid")
        self.utils.find_button_and_click("Modify", "sd")
        mod_user_defined = self.utils.input_text(settings_card_title, "user_define_field", f"MOD{user_defined}")
        self.utils.message_box("YES")
        self.utils.find_button_and_click("Save")

        # DELETE User Defined Fields
        self.utils.table(sd_name, "AddendaGrid")
        self.utils.table(mod_user_defined, "UserDefinedGrid")
        self.utils.find_button_and_click("Delete", "sd")
        self.utils.message_box("OK")
        self.utils.find_button_and_click("Save")

        # MODIFY
        self.utils.table(sd_name, "AddendaGrid")
        self.utils.find_button_and_click("Modify")
        mod_sd_name = self.utils.input_text(settings_card_title, "supplementary_data_name", f"MOD{sd_name}")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        # DELETE
        self.utils.table(mod_sd_name, "AddendaGrid")
        self.utils.find_button_and_click("Delete")
        self.utils.message_box("OK")
        self.utils.find_button_and_click("Save")

    @skip
    def test_supplementary_data_old(self):
        settings_card_title = self.settings_page("Supplementary Data")

        # ADD
        self.utils.find_button_and_click("Add")
        customer_id = self.utils.input_text(f"{settings_card_title}_old", "customer_id")
        self.utils.input_text(f"{settings_card_title}_old", "supplementary_data_name_and_version")
        self.utils.find_button_and_click("Save")

        # MODIFY

        # DELETE
        self.utils.table(customer_id, "AddendaGrid")
        self.utils.find_button_and_click("Delete")
        self.utils.message_box("OK")
        self.utils.find_button_and_click("Save")

    @skip
    def test_non_stock_maintenance(self):
        settings_card_title = self.settings_page("Non-Stock Maintenance")

        # ADD
        # self.utils.click_button("AddButton")
        self.utils.find_button_and_click("Add")
        item_id = self.utils.input_text(settings_card_title, "item_id")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        # MODIFY
        self.utils.table(item_id)
        # self.utils.click_button("ModifyButton")
        self.utils.find_button_and_click("Modify")
        item_description = self.utils.input_text(settings_card_title, "item_description")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        # DELETE
        self.utils.table(item_description)
        # self.utils.click_button("DeleteButton")
        self.utils.find_button_and_click("Delete")
        self.utils.message_box("OK")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

    @skip
    def test_ar_default_language_code(self):
        settings_card_name = self.settings_page("AR Default Language Code")

        # MODIFY
        # self.utils.click_button("ModifyButton")
        self.utils.find_button_and_click("Modify")
        self.utils.input_text(settings_card_name, "language_code")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("Save")

    @skip
    def test_einvoice_type_translation(self):
        settings_card_name = self.settings_page("eInvoice Type Translation")

        # ADD
        # self.utils.click_button("AddButton")
        self.utils.find_button_and_click("Add")
        user_einvoice_type = self.utils.input_text(settings_card_name, "user_einvoice_type")
        standard_einvoice_type = self.utils.input_text(settings_card_name, "standard_einvoice_type")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        # MODIFY
        self.utils.table(user_einvoice_type, "InvoiceTypeGrid")
        self.utils.message_box("OK")
        # self.utils.click_button("ModifyButton")
        self.utils.find_button_and_click("Modify")
        user_einvoice_type_description = self.utils.input_text(settings_card_name, "user_einvoice_type_description",
                                                               f"MOD{user_einvoice_type}")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        # DELETE
        self.utils.table(user_einvoice_type_description, "InvoiceTypeGrid")
        # self.utils.click_button("DeleteButton")
        self.utils.find_button_and_click("Delete")
        self.utils.message_box("OK")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

    @skip
    def test_customer_einvoice_maintenance(self):
        settings_card_name = self.settings_page("Customer eInvoice Maintenance")

        # ADD
        # self.utils.click_button("AddButton")
        self.utils.find_button_and_click("Add")
        party_id = self.utils.input_text(settings_card_name, "party_id")
        self.utils.input_text(settings_card_name, "einvoice_type")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        # MODIFY
        self.utils.table(party_id, "PartyOutputTypeGrid")
        # self.utils.click_button("ModifyButton")
        self.utils.find_button_and_click("Modify")
        self.utils.input_text(settings_card_name, "einvoice_type")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        # DELETE
        self.utils.table(party_id, "PartyOutputTypeGrid")
        # self.utils.click_button("DeleteButton")
        self.utils.find_button_and_click("Delete")
        self.utils.message_box("OK")
        # self.utils.click_button("SaveButton")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

    #@skip
    def test_customer_long_name(self):
        settings_card_name = self.settings_page("Customer Long Name")

        #ADD
        self.utils.find_button_and_click("Add")
        customer_id = self.utils.input_text(settings_card_name, "customer_id")
        self.utils.input_text(settings_card_name, "customer_long_name")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        #MODIFY
        self.utils.table(customer_id, "JournalDescGrid")
        self.utils.find_button_and_click("Modify")
        description_modified = self.utils.input_text(settings_card_name, "customer_long_name", "Modified")
        # self.utils.find_button_and_click("Save")
        # self.utils.message_box("Yes")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

        #DELETE
        self.utils.table(description_modified, "JournalDescGrid")
        self.utils.find_button_and_click("Delete")
        self.utils.message_box("OK")
        self.utils.find_button_and_click("Save")
        self.utils.message_box("OK")

    def settings_page(self, settings_form):
        self.utils = Utils(self)
        self.utils.initialize_test()

        self.utils.switch_to_main_frame()
        # self.utils.wait_for_home_to_load()
        self.utils.wait_for_loading_invisible()

        self.utils.select_ae_to_test()
        # Menu
        self.utils.switch_to_menu_frame()
        self.utils.select_menu("Settings")

        settings_card_title = settings_form
        self.utils.click_settings_card(settings_card_title)

        self.utils.switch_to_main_frame()
        self.utils.wait_for_loading_invisible()

        return settings_card_title
