import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
class alerts():

    def alertsimplementation(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/alert.xhtml")
        self.driver.maximize_window()
        #alert
        self.driver.find_element(by=By.XPATH,value="(//*[text()='Show']//ancestor::button)[1]").click()
        alertobject = self.driver.switch_to.alert
        alertobject.accept()
        # alert
        self.driver.find_element(by=By.XPATH, value="(//*[text()='Show']//ancestor::button)[2]").click()
        alertobject = self.driver.switch_to.alert
        alertobject.dismiss()
        # alert
        self.driver.find_element(by=By.XPATH, value="(//*[text()='Show']//ancestor::button)[5]").click()
        alertobject = self.driver.switch_to.alert
        alertobject.send_keys("This is besabt technologies")
        alertobject.accept()

        # sweet Alert
        self.driver.find_element(by=By.XPATH, value="(//*[text()='Show']//ancestor::button)[3]").click()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//*[text()='Dismiss']//ancestor::button)")))
        self.driver.find_element(by=By.XPATH,value="(//*[text()='Dismiss']//ancestor::button)").click()

        # sweet Alert
        self.driver.find_element(by=By.XPATH, value="(//*[text()='Show']//ancestor::button)[4]").click()
        time.sleep(2)
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "(//*[contains(@class,'ui-icon-closethick')]//parent::a)[2]")))
        self.driver.find_element(by=By.XPATH, value="(//*[contains(@class,'ui-icon-closethick')]//parent::a)[2]").click()

        # sweet Alert
        self.driver.find_element(by=By.XPATH, value="(//*[text()='Delete']//ancestor::button)").click()
        time.sleep(2)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class,'confirmdialog-no')]")))
        self.driver.find_element(by=By.XPATH,value="//*[contains(@class,'confirmdialog-no')]").click()


obj = alerts()
obj.alertsimplementation()