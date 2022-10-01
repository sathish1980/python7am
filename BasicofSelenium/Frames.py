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


class Frame:

    def frameimplementation(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/frame.xhtml")
        self.driver.maximize_window()
        totalFrames=self.driver.find_elements(by=By.TAG_NAME,value="iframe")
        #self.driver.find_element(by=By.XPATH,value="(//button[@id='Click' and text()='Click Me'])[1]").click()
        #frme can be identified by three ways
        # By id
        # By name
        # by index
        for eachframe in range (0,len(totalFrames)):
            self.driver.switch_to.frame(eachframe) # switch in to the frame
            myelement=self.driver.find_elements(by=By.XPATH,value="(//button[@id='Click' and text()='Click Me'])[1]")
            if len(myelement)>0:
                self.driver.find_element(by=By.XPATH, value="(//button[@id='Click' and text()='Click Me'])[1]").click()
                self.driver.switch_to.default_content() # switch back in to the frame
                break
            else:
                self.driver.switch_to.default_content()

    def multipleiframe(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/frame.xhtml")
        self.driver.maximize_window()
        #self.driver.find_element(by=By.XPATH,value="(//button[@id='Click' and text()='Click Me'])[1]").click()
        totalFrames = self.driver.find_elements(by=By.TAG_NAME, value="iframe")
        for eachframe in range(0, len(totalFrames)):
            self.driver.switch_to.frame(eachframe)
            totalinsdieFrames = self.driver.find_elements(by=By.TAG_NAME, value="iframe")
            print(len(totalinsdieFrames))
            if len(totalinsdieFrames)>0:
                WebDriverWait(self.driver, 60).until(
                    EC.frame_to_be_available_and_switch_to_it((self.driver.find_element(by=By.ID,value="frame2"))))
                #OR
                #self.driver.switch_to.frame("frame2")
                myelement = self.driver.find_elements(by=By.XPATH,
                                                      value="(//button[@id='Click' and text()='Click Me'])[1]")
                if len(myelement) > 0:
                    self.driver.find_element(by=By.XPATH,
                                             value="(//button[@id='Click' and text()='Click Me'])[1]").click()
                    self.driver.switch_to.default_content()
                    break
                else:
                    self.driver.switch_to.default_content()
            else:
                self.driver.switch_to.default_content()

obj=Frame()
obj.multipleiframe()