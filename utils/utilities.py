class Utils:
    def __init__(self, util):
        self.util = util

    def switch_to_main_frame(self):
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

    def wait_for_loading_invisible(self):
        is_loading = True
        while is_loading:
            loading_element = self.util.is_element_visible("//div[@class = 'mg-busy mg-busy-wait' and @style='display: block;']")
            if not loading_element:
                is_loading = False
                self.util.wait(5)

    def click_button(self, mg_compname):
        self.util.click(f"//div[@data-mgcompname = '{mg_compname}']//button")
        self.util.wait(1)

    def input_text(self, mg_companame, input_text):
        self.util.send_keys(f"//div[@data-mgcompname = '{mg_companame}']//input", input_text)
        self.util.wait(1)