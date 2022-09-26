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
class windowsHandling():

    def Windowshandleimplementaion(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/window.xhtml")
        self.driver.maximize_window()
        parentwindowname=self.driver.current_window_handle
        self.driver.find_element(by=By.XPATH,value="//*[text()='Open']//parent::button").click()
        allwindow=self.driver.window_handles
        for eachchildwindow in allwindow :
            if (eachchildwindow!=parentwindowname):
                self.driver.switch_to.window(eachchildwindow)
                checkelement=self.driver.find_elements(by=By.XPATH, value="//*[text()='Browser']//ancestor::a")
                if len(checkelement)>0:
                    self.driver.find_element(by=By.XPATH, value="//*[text()='Browser']//ancestor::a").click()
                    self.driver.find_element(by=By.XPATH, value="//*[text()='Alert']//ancestor::a").click()
                    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//*[text()='Show']//ancestor::button)[1]")))
                    print(self.driver.title)
                    print(self.driver.current_url)
                    print(self.driver.find_element(by=By.XPATH, value="(//*[text()='Show'])[1]").get_attribute("class"))
                    print(self.driver.current_window_handle)
                    print(self.driver.window_handles)
                    self.driver.close()
                    self.driver.switch_to.window(parentwindowname)
                    #self.driver.quit()
                else:
                    self.driver.switch_to.window(parentwindowname)

    def multiplewindow(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/window.xhtml")
        self.driver.maximize_window()
        currentwindowname = self.driver.current_window_handle
        self.driver.find_element(by=By.XPATH,value="//*[text()='Open Multiple']//parent::button").click()
        allwindow = self.driver.window_handles
        for eachchildwindow in allwindow:
            if (eachchildwindow != currentwindowname):
                self.driver.switch_to.window(eachchildwindow)
                checkelement = self.driver.find_elements(by=By.XPATH, value="//*[text()='Browser']//ancestor::a")
                if len(checkelement) > 0:
                    self.driver.maximize_window()
                    self.driver.find_element(by=By.XPATH, value="//*[text()='Browser']//ancestor::a").click()
                    self.driver.find_element(by=By.XPATH, value="//*[text()='Alert']//ancestor::a").click()
                    WebDriverWait(self.driver, 60).until(
                        EC.element_to_be_clickable((By.XPATH, "(//*[text()='Show']//ancestor::button)[1]")))
                    print(self.driver.title)
                    print(self.driver.current_url)
                    print(self.driver.find_element(by=By.XPATH, value="(//*[text()='Show'])[1]").get_attribute("class"))
                    print(self.driver.current_window_handle)
                    print(self.driver.window_handles)
                    #self.driver.close()
                    self.driver.switch_to.window(currentwindowname)
                    break
                else:
                    self.driver.switch_to.window(currentwindowname)


obj=windowsHandling()
#obj.Windowshandleimplementaion()
obj.multiplewindow()