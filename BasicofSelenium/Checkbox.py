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
class checkbox:

    def checkboximplementation(self,programname):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/checkbox.xhtml")
        self.driver.maximize_window()
        self.driver.find_element(by=By.XPATH,value="//*[text()='Basic']//preceding::div[contains(@class,'ui-chkbox-box')]").click()
        self.driver.find_element(by=By.XPATH,value="//*[@class='ui-toggleswitch-slider']").click()
        time.sleep(1)
        print(self.driver.find_element(by=By.XPATH,value="//*[@class='ui-growl-title']").text)
        language=self.driver.find_elements(by=By.XPATH,value="//*[contains(@class,'ui-selectmanycheckbox')]//tr//td//label")
        count=0
        for eachelement in language:
            count+=1
            if eachelement.text == programname:
                self.driver.find_element(by=By.XPATH, value="//*[contains(@class,'ui-selectmanycheckbox')]//tr//td["+str(count)+"]//div[contains(@class,'ui-chkbox-box')]").click()
                break



obj=checkbox()
obj.checkboximplementation("Javascript")