import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config


class TestLandingPageHeader:
    PAGE_TITLE = 'Top-Rated Contact Center Software | Built For Your Favorite CRM'
    SOLUTIONS_BUTTON = '//*[@id="header-menu"]/ul/li[1]/a'
    FEATURES_BUTTON = '//*[@id="header-menu"]/ul/li[2]/a'
    INTEGRATIONS_BUTTON = '//*[@id="header-menu"]/ul/li[3]/a'
    PRICING_BUTTON = '//*[@id="header-menu"]/ul/li[4]/a'
    COMPARE_US_BUTTON = '//*[@id="header-menu"]/ul/li[5]/a'
    RESOURCES_BUTTON = '//*[@id="header-menu"]/ul/li[6]/a'
    HEADER_BUTTON_LINKS = {
        SOLUTIONS_BUTTON: (
            f'{Config.BASE_LP_URL}/solution/',
            'Solutions - Aloware'
        ),
        FEATURES_BUTTON: (
            f'{Config.BASE_LP_URL}/features/',
            'Features - Aloware'
        ),
        INTEGRATIONS_BUTTON: (
            f'{Config.BASE_LP_URL}/integrations/',
            'Integrations - Aloware'
        ),
        PRICING_BUTTON: (
            f'{Config.BASE_LP_URL}/pricing/',
            'Pricing - Aloware'
        ),
        COMPARE_US_BUTTON: (
            f'{Config.BASE_LP_URL}/#',
            PAGE_TITLE
        ),
        RESOURCES_BUTTON: (
            f'{Config.BASE_LP_URL}/#',
            PAGE_TITLE
        )
    }

    def setup(self):
        options = ChromeOptions()
        # options.add_argument('--no-sandbox')
        # options.add_argument('--incognito')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--disable-extensions")
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(options=options)
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )

    def test_header_buttons(self):
        tab_num = 0
        for button_locator, button_info in self.HEADER_BUTTON_LINKS.items():
            url, title = button_info
            self.driver.get(Config.BASE_LP_URL)
            self.driver.find_element(By.XPATH, button_locator).click()
            time.sleep(5)
            if 'solution' not in url:
                tab_num += 1
                self.driver.switch_to.window(self.driver.window_handles[tab_num])
            WebDriverWait(self.driver, 10).until(
                EC.title_contains(title)
            )
            assert url == self.driver.current_url

    def tear_down(self):
        self.driver.close()
