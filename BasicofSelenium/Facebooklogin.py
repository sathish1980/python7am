import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class facbooklogin():

    def login(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://www.facebook.com/")
        #username=self.driver.find_element(by=By.ID, value="email")
        #username.send_keys("kumar.sathish189@gmail.com")
        """username = self.driver.find_element(by=By.NAME, value="email") # webElement
        username.send_keys("kumar.sathish189@gmail.com") #actions
        username.clear()
        username.send_keys("another value")"""
        self.driver.find_element(by=By.CLASS_NAME, value="inputtext _55r1 _6luy").send_keys("")
        self.driver.find_element(by=By.CLASS_NAME, value="inputtext _55r1 _6luy").clear()
        self.driver.find_element(by=By.CLASS_NAME, value="inputtext _55r1 _6luy").send_keys("")
        #or
        username = self.driver.find_element(by=By.CLASS_NAME, value="inputtext _55r1 _6luy")  # webElement
        username.send_keys("kumar.sathish189@gmail.com")  # actions
        username.clear()
        username.send_keys("another value")


        time.sleep(2)

obj=facbooklogin()
obj.login()