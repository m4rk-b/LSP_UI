import random

import pytest
from dotenv import load_dotenv
import os
import json
import re
from selenium.webdriver.common.keys import Keys


class Utils:
    def __init__(self, util):
        self.util = util

    def read_json_data(self, settings_form, input_field_name):
        settings_form = re.sub(r'[^a-zA-Z0-9]+', '_', settings_form).strip('_')
        settings_form = settings_form.lower()
        input_field_name = input_field_name.lower()
        with open('../settings/component_names.json') as json_file:
            datas = json.load(json_file)

        json_outputs = []
        for data in datas['settings']:
            if settings_form in data:
                for component in data[settings_form]:
                    if input_field_name in component:
                        json_outputs.append(component[input_field_name])

        return json_outputs

    def read_button_components_json(self, button_name):
        with open('../settings/button_components.json') as json_file:
            button_components = json.load(json_file)

        button_compnames = button_components.get('buttons', [])
        buttons = None

        for button_component in button_compnames:
            buttons = button_component.get(f'{button_name}', [])

        return buttons

    def initialize_test(self):
        load_dotenv()
        url = os.getenv("LSP_URL")
        self.util.maximize_window()
        self.util.open(url)

    def switch_to_main_frame(self):
        load_dotenv()
        url = os.getenv("LSP_URL")
        uuid = url.split("/")[-1]
        self.util.switch_to_default_content()
        self.util.switch_to_frame(f"LSP_31_{uuid}")
        self.util.wait(2)

    def switch_to_menu_frame(self):
        self.util.switch_to_default_content()
        self.switch_to_main_frame()
        iframe_name = "mg_frame" + self.util.get_attribute("//div[@data-mgcompname = 'AccordionUserControl']", "id")
        self.util.switch_to_frame(iframe_name)

    def switch_to_cards_frame(self):
        self.util.switch_to_default_content()
        self.switch_to_main_frame()
        iframe_name = "mg_frame" + self.util.get_attribute("//div[@data-mgcompname = 'SubscriptionListUserControl']",
                                                           "id")
        self.util.switch_to_frame(iframe_name)

    def switch_to_user_control_button_frame(self):
        self.util.switch_to_default_content()
        self.switch_to_main_frame()
        iframe_xpath = "//div[@data-mgcompname = 'maintenanceToolbarUserControl']"
        is_exist = self.util.is_element_present(iframe_xpath)
        if is_exist:
            iframe_name = "mg_frame" + self.util.get_attribute(iframe_xpath, "id")
            self.util.switch_to_frame(iframe_name)

        return is_exist

    def wait_for_home_to_load(self):
        self.util.wait(10)
        self.wait_for_loading_invisible()
        self.switch_to_main_frame()
        # iframe_name = "mg_frame" + self.util.get_attribute("//div[@data-mgcompname = 'AccordionUserControl']", "id")
        is_sidebar_loaded = False
        while not is_sidebar_loaded:
            is_sidebar_loaded = self.util.is_element_visible("//div[@data-mgcompname = 'AccordionUserControl']")
            self.util.wait(0.2)

    def wait_for_loading_invisible(self):
        is_loading = True
        while is_loading:
            loading_element = self.util.is_element_visible(
                "//div[@class = 'mg-busy mg-busy-wait' and @style='display: block;']")
            if not loading_element:
                is_loading = False
                self.util.wait(5)

    def message_box(self, button_name):
        self.util.switch_to_default_content()
        self.switch_to_main_frame()
        is_message_box_element = self.util.is_element_present(
            "//div[@data-mgcompname = 'MG.MessageBox' and @aria-hidden = 'false']")
        if is_message_box_element:
            self.util.click(
                f"//div[@data-mgcompname = 'MG.MessageBox' and @aria-hidden = 'false']//a[@data-mgcompnamevalue = '{button_name}']")
            self.util.wait(0.5)

    # Note: The button_for arg is for buttons with duplicate name, example are the ADD, MODIFY, and DELETE buttons in Supplementary Data Setup form
    def find_button_and_click(self, button_name, button_for=None):
        # button_for = button_for.lower()
        button_name = button_name.lower()
        button_compnames = self.read_button_components_json(button_name)
        compname = None
        selector = None
        button_type = None
        for button_compname in button_compnames:
            if button_compname['button_for'] == button_for:
                compname = button_compname['compname']
                selector = button_compname['selector']
                button_type = button_compname['type']

            match button_type:
                case "default":
                    self.switch_to_main_frame()
                    button_xpath = f"//div[@{selector} = '{compname}']//button"
                    is_button_exist = self.util.is_element_visible(button_xpath)
                    if is_button_exist:
                        button_index = self.util.find_elements(button_xpath)
                        self.util.click(f"//div[@{selector} = '{compname}' and {len(button_index)}]//button")
                case "user_component":
                    is_iframe = self.switch_to_user_control_button_frame()
                    if is_iframe:
                        button_xpath = f"//div[@class = 'buttonset']//button[@{selector}='{compname}']"
                        is_button_present = self.util.is_element_present(button_xpath)
                        if is_button_present:
                            is_button_exist = self.util.is_element_visible(button_xpath)
                            if is_button_exist:
                                self.util.click(button_xpath)
        self.util.wait(1)

    def click_button(self, mg_compname):
        button_index = self.util.find_elements(f"//div[@data-mgcompname = '{mg_compname}']//button")
        self.util.wait_for_element_clickable(
            f"//div[@data-mgcompname = '{mg_compname}' and {len(button_index)}]//button")
        self.util.click(f"//div[@data-mgcompname = '{mg_compname}' and {len(button_index)}]//button")
        self.util.wait(1)

    def user_control_buttons(self, button_id):
        self.switch_to_user_control_button_frame()
        self.util.click(f"//div[@class = 'buttonset']//button[@id='{button_id}']")
        self.util.wait(1)

    def input_text(self, settings_form, input_name_field, input_text=None):
        self.util.wait(0.5)
        select_value = None
        input_elements = self.read_json_data(settings_form, input_name_field)
        for input_element in input_elements:
            compname = input_element['compname']
            selector = input_element['selector']
            role = input_element['role']
            required = input_element['required']
            editable = input_element['editable']
            reference = input_element['reference']
            if input_text is None:
                input_text = input_element['default']
            size = input_element['size']
            input_index = self.util.find_elements(f"//input[@{selector} = '{compname}']")
            textarea_index = self.util.find_elements(f"//textarea[@{selector} = '{compname}' and @aria-readonly = 'false']")
            if len(input_index) != 0 or len(textarea_index) != 0:
                input_xpath = f"//input[@{selector} = '{compname}' and {len(input_index)}]"
                textarea_xpath = f"//textarea[@{selector} = '{compname}' and @aria-readonly = 'false']"
                is_present = self.util.is_element_present(input_xpath)
                if (compname == "uploadedfileinput" and is_present) or self.util.is_element_visible(input_xpath) or self.util.is_element_visible(textarea_xpath):
                    if role == 'checkbox':
                        input_id = self.util.get_attribute(input_xpath, "componentid")
                        self.util.click(f"//span[@id = '{input_id}-displayEl']")
                    if role == 'combobox':
                        combobox_trigger_picker_xpath = f"//div[@data-mgcompname = '{compname}']//div[@aria-label = 'Open']"
                        if self.util.is_element_visible(combobox_trigger_picker_xpath):
                            self.util.click(combobox_trigger_picker_xpath)
                            self.util.wait(1)
                            combobox_values = self.util.find_elements(
                                f"//div[@data-mgcompname = '{compname}']//ul//td")
                            combobox_values_dict = [combobox_element_value.text for combobox_element_value in combobox_values]
                            if reference is not None:
                                grid_element_id = self.util.get_attribute(f"//div[@data-mgcompname = '{reference}']", "id")
                                grid_element_values = self.util.find_elements(f"//div[@id = '{grid_element_id}-normal-body']//td/div")
                                grid_values_dict = [grid_element_value.text for grid_element_value in grid_element_values]

                                for combobox_value in combobox_values:
                                    if combobox_value.text not in grid_values_dict:
                                        select_value = combobox_value.text
                                        break
                            else:
                                if len(combobox_values) == 0:
                                    select_value = input_text
                                    self.util.send_keys(input_xpath, select_value)
                                elif len(combobox_values) > 0 and input_text is None:
                                    is_no_electronic_invoice = True
                                    while is_no_electronic_invoice:
                                        select_value = random.choice(combobox_values_dict)
                                        if select_value != "No Electronic Invoice":
                                            is_no_electronic_invoice = False
                                elif len(combobox_values) > 0 and input_text is not None:
                                    select_value = input_text
                            self.util.click(
                                f"//div[@data-mgcompname = '{compname}']//ul//td[contains(text(), '{select_value}')]")
                    if role == 'textbox':
                        select_value = input_text
                        if editable:
                            # self.util.clear(input_xpath)
                            # self.util.update_text(input_xpath, select_value)
                            self.util.update_text(input_xpath, select_value + Keys.ENTER)
                        else:
                            self.util.send_keys(input_xpath, select_value)
                    if role == 'textarea':
                        select_value = input_text
                        # if editable:
                        #     # self.util.update_text(textarea_xpath, select_value + Keys.ENTER)
                        #     self.util.clear(textarea_xpath)
                        self.util.send_keys(textarea_xpath, select_value)

            self.util.wait(0.1)
        self.util.wait(1)
        return select_value

    def input_textarea(self, mg_compname, input_text):
        self.util.send_keys(f"//div[@data-mgcompname = '{mg_compname}']//textarea[@aria-readonly = 'false']",
                            input_text)

    def translation_maintenance_combobox(self, output_type, translations):
        self.util.click("//div[@data-mgcompname = 'OutputTypeComboBox']//div[@aria-label = 'Open']")
        self.util.click(f"//div[@data-mgcompname = 'OutputTypeComboBox']//td[contains(text(), '{output_type}')]")
        translations_combobox_index = self.util.find_elements(
            "//div[@data-mgcompname = 'TranslationsComboBox']//div[@aria-label = 'Open']")
        self.util.click(
            f"//div[@data-mgcompname = 'TranslationsComboBox' and {len(translations_combobox_index)}]//div[@aria-label = 'Open']")
        self.util.click(f"//div[@data-mgcompname = 'TranslationsComboBox']//td[contains(text(), '{translations}')]")

    def close_settings_form(self, form_header_text="", mg_compname=""):
        self.switch_to_main_frame()
        if form_header_text == "" and mg_compname == "":
            self.util.fail("Should have at least 1 selector.")
        else:
            if form_header_text != "":
                close_window_index = self.util.find_elements(
                    f"//div[@aria-label = '{form_header_text}']//div[@aria-label = 'Close Window']")
                xpath = f"//div[@aria-label = '{form_header_text}' and {len(close_window_index)}]//div[@aria-label = 'Close Window']"
            elif mg_compname != "":
                close_window_index = self.util.find_elements(
                    f"//div[@data-mgcompname = '{mg_compname}']//div[@aria-label = 'Close Window']")
                xpath = f"//div[@data-mgcompname = '{mg_compname}' and {len(close_window_index)}]//div[@aria-label = 'Close Window']"

            self.util.click(xpath)

    def table(self, text_to_search, mg_compname="MainGrid"):
        is_text_exist = self.util.is_element_present(
            f"//div[@data-mgcompname = '{mg_compname}']//td/div[contains(text(), '{text_to_search}')]")
        if is_text_exist:
            self.util.click(f"//div[@data-mgcompname = '{mg_compname}']//td/div[contains(text(), '{text_to_search}')]")
            self.util.wait(0.2)

    def upload_file(self, form_name, file_to_upload):
        self.switch_to_main_frame()
        path = os.path.normpath(os.path.join(os.path.dirname(__file__), f"../files/{file_to_upload}"))
        self.click_button("XSLTUploadButton")
        # self.input_text("uploadedfileinput", path, "name")
        self.input_text(form_name, "select_file", path)
        self.util.click("//a[@aria-disabled = 'false']//span[contains(text(), 'Upload')]")

    def select_ae_to_test(self):
        load_dotenv()
        ae = os.getenv("ACCOUNTING_ENTITY")
        self.util.click("//div[@data-mgcompname = 'AEDroplist']//div[@aria-label = 'Open']")
        self.util.wait(0.5)
        is_ae_exist = self.util.is_element_present(
            f"//div[@data-mgcompname = 'AEDroplist']//ul/table//td[contains(text(), '{ae}')]")
        if is_ae_exist:
            self.util.click("//div[@data-mgcompname = 'AEDroplist']//div[@aria-label = 'Open']")
            self.util.click(f"//div[@data-mgcompname = 'AEDroplist']//ul/table//td[contains(text(), '{ae}')]")
        else:
            self.util.fail(f"You're not subscribe to {ae}.")

    def select_menu(self, menu_name):
        is_menu_exist = self.util.is_element_present(f"//ul[@id = 'accordion2']//a[contains(text(), '{menu_name}')]")
        if is_menu_exist:
            self.util.click(f"//ul[@id = 'accordion2']//a[contains(text(), '{menu_name}')]", "xpath", 5)
        else:
            self.util.fail(f"Cannot find {menu_name} in the accordion.")

    def click_settings_card(self, settings_name):
        self.switch_to_cards_frame()
        is_settings_exist = self.util.is_element_present(f"//div//h4[contains(text(), '{settings_name}')]")
        if is_settings_exist:
            self.util.click(f"//div//h4[contains(text(), '{settings_name}')]")
        else:
            pytest.skip(f"{settings_name} is not available.")
