import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
class slider:

    def sliderimplementation(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/drag.xhtml")
        self.driver.maximize_window()
        self.driver.execute_script("document.querySelector('.ui-state-default').style.left = '0%'")
        # self.driver.execute_script("document.querySelector('.ui-state-default').style.left = '100%'")
        mc = ActionChains(self.driver)
        fromvalue = self.driver.find_element(by=By.XPATH, value="//*[contains(@id,'form:j_idt125')]//div[1]")

        mc.move_to_element(self.driver.find_element(by=By.XPATH,
                                                    value="//*[contains(@id,'form:j_idt125')]//span[1]")).drag_and_drop_by_offset(
            fromvalue, 100, 0).perform()
obj = slider()
obj.sliderimplementation()