import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config


class TestLandingPageHeader:
    SOLUTIONS_BUTTON = '//*[@id="header-menu"]/ul/li[1]/a'
    FEATURES_BUTTON = '//*[@id="header-menu"]/ul/li[2]/a'
    INTEGRATIONS_BUTTON = '//*[@id="header-menu"]/ul/li[3]/a'
    PRICING_BUTTON = '//*[@id="header-menu"]/ul/li[4]/a'
    COMPARE_US_BUTTON = '//*[@id="header-menu"]/ul/li[5]/a'
    RESOURCES_BUTTON = '//*[@id="header-menu"]/ul/li[6]/a'
    HEADER_BUTTON_LINKS = {
        SOLUTIONS_BUTTON: f'{Config.BASE_LP_URL}/solution/',
        FEATURES_BUTTON: f'{Config.BASE_LP_URL}/features/',
        INTEGRATIONS_BUTTON: f'{Config.BASE_LP_URL}/integrations/',
        PRICING_BUTTON: f'{Config.BASE_LP_URL}/pricing/',
        COMPARE_US_BUTTON: f'{Config.BASE_LP_URL}/#',
        RESOURCES_BUTTON: f'{Config.BASE_LP_URL}/#'
    }

    def setup(self):
        options = ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--incognito')
        self.driver = webdriver.Chrome(options=options)

    def test_header_buttons(self):
        tab_num = 0
        for button_locator, url in self.HEADER_BUTTON_LINKS.items():
            title_input = f'{url.split("/")[-2].capitalize()}'
            self.driver.get(Config.BASE_LP_URL)
            self.driver.find_element(By.XPATH, button_locator).click()
            WebDriverWait(self.driver, 10).until(
                EC.title_contains(title_input)
            )
            if 'solution' not in url:
                tab_num += 1
                self.driver.switch_to.window(self.driver.window_handles[tab_num])

            assert url == self.driver.current_url

    def tear_down(self):
        self.driver.close()
