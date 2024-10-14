class Utils:
    def __init__(self, util):
        self.util = util

    def switch_to_main_frame(self):
        self.util.switch_to_default_content()
        self.util.switch_to_frame("LSP_31_59b159d4-4a16-422e-bedf-d57a5b0f139c")
        self.util.wait(2)

    def switch_to_menu_frame(self):
        self.util.switch_to_default_content()
        self.util.switch_to_frame("LSP_31_59b159d4-4a16-422e-bedf-d57a5b0f139c")
        iframe_name = "mg_frame" + self.util.get_attribute("//div[@data-mgcompname = 'AccordionUserControl']", "id")
        self.util.switch_to_frame(iframe_name)

    def switch_to_cards_frame(self):
        self.util.switch_to_default_content()
        self.util.switch_to_frame("LSP_31_59b159d4-4a16-422e-bedf-d57a5b0f139c")
        iframe_name = "mg_frame" + self.util.get_attribute("//div[@data-mgcompname = 'SubscriptionListUserControl']", "id")
        self.util.switch_to_frame(iframe_name)

    def switch_to_user_control_button_frame(self):
        self.util.switch_to_default_content()
        self.util.switch_to_frame("LSP_31_59b159d4-4a16-422e-bedf-d57a5b0f139c")
        iframe_name = "mg_frame" + self.util.get_attribute("//div[@data-mgcompname = 'maintenanceToolbarUserControl']", "id")
        self.util.switch_to_frame(iframe_name)

    def wait_for_loading_invisible(self):
        is_loading = True
        while is_loading:
            loading_element = self.util.is_element_visible("//div[@class = 'mg-busy mg-busy-wait' and @style='display: block;']")
            if not loading_element:
                is_loading = False
                self.util.wait(5)

    def message_box(self, button_name):
        is_message_box_element = self.util.is_element_present("//div[@data-mgcompname = 'MG.MessageBox' and @aria-hidden = 'false']")
        if is_message_box_element:
            self.util.click(f"//div[@data-mgcompname = 'MG.MessageBox' and @aria-hidden = 'false']//a[@data-mgcompnamevalue = '{button_name}']")
            self.util.wait(0.5)

    def click_button(self, mg_compname):
        self.util.click(f"//div[@data-mgcompname = '{mg_compname}']//button")
        self.util.wait(1)

    def user_control_buttons(self, button_id):
        self.switch_to_user_control_button_frame()
        self.util.click(f"//div[@class = 'buttonset']//button[@id='{button_id}']")
        self.util.wait(1)

    def input_text(self, mg_compname, input_text):
        self.util.send_keys(f"//div[@data-mgcompname = '{mg_compname}']//input", input_text)
        self.util.wait(0.5)

    def combobox_input(self, table_mg_compname, combobox_mg_compname):
        self.util.click(f"//div[@data-mgcompname = '{combobox_mg_compname}']//div[@aria-label = 'Open']")
        self.util.wait(1)
        table_element_id = self.util.get_attribute(f"//div[@data-mgcompname = '{table_mg_compname}']", "id")
        table_element_values = self.util.find_elements(f"//div[@id = '{table_element_id}-normal-body']//td/div")
        combobox_values = self.util.find_elements(f"//div[@data-mgcompname = '{combobox_mg_compname}']//ul//td")
        select_value = ""
        table_texts = [table_element_value.text for table_element_value in table_element_values]

        for combobox_value in combobox_values:
            if combobox_value.text not in table_texts:
                select_value = combobox_value.text
                break
        self.util.click(f"//div[@data-mgcompname = '{combobox_mg_compname}']//ul//td[contains(text(), '{select_value}')]")
        #TODO: Add a condition if combobox is nullable, if yes, add custom text if no value is available in the combobox, if no, skip add, edit, and delete.

    def clear_input(self, mg_compname):
        self.util.clear(f"//div[@data-mgcompname = '{mg_compname}']//input")
        self.util.wait(0.5)

    def close_settings_form(self, form_header_text):
        self.util.click(f"//div[@aria-label = '{form_header_text}']//div[@aria-label = 'Close Window']")

    def table(self, text_to_search):
        is_text_exist = self.util.is_element_present(f"//div[@data-mgcompname = 'MainGrid']//td/div[contains(text(), '{text_to_search}')]")
        if is_text_exist:
            self.util.click(f"//div[@data-mgcompname = 'MainGrid']//td/div[contains(text(), '{text_to_search}')]")
            self.util.wait(0.5)