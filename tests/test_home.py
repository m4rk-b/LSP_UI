from seleniumbase import BaseCase
from utils import utilities
from utils.utilities import Utils
from modules.settings import SettingsModule


class HomeTest(BaseCase):
    def setUp(self):
        super().setUp()

    def initialize_test(self):
        self.maximize_window()
        self.open("https://mingle-cqa-portal.cqa.inforcloudsuite.com/v2/LCLQA_AX1/59b159d4-4a16-422e-bedf-d57a5b0f139c")
        self.send_keys("//input[@id='username']", "")
        self.send_keys("//input[@id='pass']", "")
        self.click("//button[@title = 'Sign in']")

    def select_ae_to_test(self, accounting_entity):
        self.click("//div[@data-mgcompname = 'AEDroplist']//div[@aria-label = 'Open']")
        self.click(f"//div[@data-mgcompname = 'AEDroplist']//ul/table//td[contains(text(), '{accounting_entity}')]", "xpath")

    def test_settings_page(self):
        # Menu
        self.utils.switch_to_menu_frame()
        self.click("//ul[@id = 'accordion2']//a[contains(text(), 'Settings')]", "xpath", 5)

        self.utils.switch_to_cards_frame()

        self.click("//div//h4[contains(text(), 'Contact Master')]")

        self.switch_to_default_content()
        self.switch_to_frame("LSP_31_59b159d4-4a16-422e-bedf-d57a5b0f139c")
        self.utils.wait_for_loading_invisible()
        self.utils.click_button("AddButton")

        self.utils.input_text("NameChildFormEdit", "TESTNAME")

        self.utils.click_button("SaveButton")

    def test_home_page(self):
        self.initialize_test()

        self.utils = Utils(self)

        self.utils.switch_to_main_frame()
        self.utils.wait_for_loading_invisible()

        self.select_ae_to_test("CL_M3")

        self.test_settings_page()


