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
class mouseactions():

    def mluseactionimplementation(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.ebay.com/")
        self.driver.maximize_window()
        mouseactionsineabay = ActionChains(self.driver)
        mouseactionsineabay.move_to_element(self.driver.find_element(by=By.XPATH,value="(//*[@class='hl-cat-nav__container']//a[text()='Electronics'])[1]")).perform()
        mouseactionsineabay.move_to_element(self.driver.find_element(by=By.XPATH,value="(//*[@class='hl-cat-nav__container']//a[text()='Computers and tablets'])[1]")).click().perform()

    def mouseactioninfb(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()
        fbmouse = ActionChains(self.driver)
        fbmouse.move_to_element(self.driver.find_element(by=By.ID,value="email")).send_keys("sathish").double_click().context_click().perform()

    def mousedraganddrodp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/drag.xhtml")
        self.driver.maximize_window()
        dragmouse = ActionChains(self.driver)
        dragmouse.move_to_element(self.driver.find_element(by=By.XPATH,value="//*[@id='form:drag_content']")).drag_and_drop(self.driver.find_element(by=By.XPATH,value="//*[@id='form:drag_content']"),self.driver.find_element(by=By.XPATH,value="//*[@id='form:drop_content']")).perform()

    def keyboardpyautogui(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()
        fbmouse = ActionChains(self.driver)
        fbmouse.move_to_element(self.driver.find_element(by=By.ID, value="email")).send_keys(
            "sathish").double_click().context_click().perform()
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("enter")
        fbmouse.key_down("tab")
        fbmouse.key_up("tab")
        pyautogui.press("tab")
        pyautogui.hotkey('ctrl','v')


obj=mouseactions()
obj.mousedraganddrodp()