from dotenv import load_dotenv
import os


class Utils:
    def __init__(self, util):
        self.util = util

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
        iframe_name = "mg_frame" + self.util.get_attribute("//div[@data-mgcompname = 'maintenanceToolbarUserControl']",
                                                           "id")
        self.util.switch_to_frame(iframe_name)

    def wait_for_home_to_load(self):
        self.util.wait(10)
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

    def click_button(self, mg_compname):
        button_index = self.util.find_elements(f"//div[@data-mgcompname = '{mg_compname}']//button")
        self.util.wait_for_element_clickable(f"//div[@data-mgcompname = '{mg_compname}' and {len(button_index)}]//button")
        self.util.click(f"//div[@data-mgcompname = '{mg_compname}' and {len(button_index)}]//button")
        self.util.wait(1)

    def user_control_buttons(self, button_id):
        self.switch_to_user_control_button_frame()
        self.util.click(f"//div[@class = 'buttonset']//button[@id='{button_id}']")
        self.util.wait(1)

    def input_text(self, mg_compname, input_text, selector="data-mgcompnamevalue"):
        input_index = self.util.find_elements(f"//input[@{selector} = '{mg_compname}']", input_text)
        if self.util.get_attribute(f"//input[@{selector} = '{mg_compname}' and {len(input_index)}]",
                                   "role") == "checkbox":
            input_id = self.util.get_attribute(f"//input[@{selector} = '{mg_compname}' and {len(input_index)}]",
                                               "componentid")
            self.util.click(f"//span[@id = '{input_id}-displayEl']")
        else:
            self.util.send_keys(f"//input[@{selector} = '{mg_compname}' and {len(input_index)}]", input_text)
        self.util.wait(1)

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

    def combobox_input(self, table_mg_compname, combobox_mg_compname, is_customizable=False, input_text=""):
        self.util.click(f"//div[@data-mgcompname = '{combobox_mg_compname}']//div[@aria-label = 'Open']")
        self.util.wait(1)
        table_element_id = self.util.get_attribute(f"//div[@data-mgcompname = '{table_mg_compname}']", "id")
        table_element_values = self.util.find_elements(f"//div[@id = '{table_element_id}-normal-body']//td/div")
        combobox_values = self.util.find_elements(f"//div[@data-mgcompname = '{combobox_mg_compname}']//ul//td")
        select_value = ""
        table_texts = [table_element_value.text for table_element_value in table_element_values]
        return_value = ""

        for combobox_value in combobox_values:
            if combobox_value.text not in table_texts:
                select_value = combobox_value.text
                break
        if select_value == "":
            if is_customizable:
                self.util.send_keys(f"//div[@data-mgcompname = '{combobox_mg_compname}']//input", input_text)
                return_value = input_text
            else:
                return_value = ""
        else:
            self.util.click(
                f"//div[@data-mgcompname = '{combobox_mg_compname}']//ul//td[contains(text(), '{select_value}')]")
            return_value = select_value

        return return_value

    def clear_input(self, mg_compname):
        self.util.clear(f"//div[@data-mgcompname = '{mg_compname}']//input")
        self.util.wait(0.5)

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

    def upload_file(self, file_to_upload):
        self.switch_to_main_frame()
        path = os.path.normpath(os.path.join(os.path.dirname(__file__), f"../files/{file_to_upload}"))
        self.click_button("XSLTUploadButton")
        self.input_text("uploadedfileinput", path, "name")
        self.util.click("//a[@aria-disabled = 'false']//span[contains(text(), 'Upload')]")
