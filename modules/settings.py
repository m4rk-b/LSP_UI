from seleniumbase import BaseCase
from utils.utilities import Utils

class SettingsModule(BaseCase):
    # def __init__(self, settings):
    #     self.settings = settings

    def setUp(self):
        super().setUp()

    def test_contact_master(self):
        self.util = Utils(self)

        self.click("//div//h4[contains(text(), 'Contact Master')]")

        self.switch_to_frame("LSP_31_59b159d4-4a16-422e-bedf-d57a5b0f139c")
        self.util.click_button("AddButton")

        self.util.input_text("NameChildFormEdit", "TESTNAME")

        self.util.click_button("SaveButton")