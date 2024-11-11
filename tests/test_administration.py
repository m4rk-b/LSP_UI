from unittest import skip
from dotenv import load_dotenv
import os
from seleniumbase import BaseCase
from utils import utilities
from utils.utilities import Utils
from modules.settings import SettingsModule

class AdminTest(BaseCase):
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

    def test_accounting_entity(self):
        #Todo: Add script
        # print("Test")
        self.admin_page("Accounting Entity Maintenance")
        self.utils.find_button_and_click("Add")
        self.utils.switch_to_main_frame()
        self.utils.input_text("Accounting Entity Maintenance", "accounting_entity", "administration")
        self.wait(10)

    def admin_page(self, admin_submenu_name):
        self.utils = Utils(self)
        self.utils.initialize_test()

        self.utils.switch_to_main_frame()
        # self.utils.wait_for_home_to_load()
        self.utils.wait_for_loading_invisible()

        # self.utils.select_ae_to_test()
        # Menu
        self.utils.switch_to_menu_frame()
        # self.utils.select_menu("Settings")
        self.utils.select_admin_menu(admin_submenu_name)

        # settings_card_title = settings_form
        # self.utils.click_settings_card(settings_card_title)

        self.utils.switch_to_main_frame()
        self.utils.wait_for_loading_invisible()

        # return settings_card_title