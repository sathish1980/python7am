import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class progressbar:

    def progressbarimplementation(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/drag.xhtml")
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script("document.querySelector('.ui-state-default').style.left = '0%'")
        self.driver.find_element(by=By.ID, value="form:j_idt119").click()
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "ui-progressbar-label"), "100%"))
        print(self.driver.find_element(by=By.XPATH, value="//*[@class='ui-growl-message']//span").text)

obj=progressbar()
obj.progressbarimplementation()