import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class facbooklogin():

    def login(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()
        email=self.driver.find_element(by=By.ID, value="email")
        email.send_keys("kumar.sathish189@gmail.com124")
        time.sleep(2)
        email.clear()
        email.send_keys("nextvalue")
        password = self.driver.find_element(by=By.NAME, value="pass")
        password.send_keys("242454545")
        time.sleep(2)
        password.clear()
        password.send_keys("nextvalue")
        #password = self.driver.find_element(by=By.CLASS_NAME, value="_6lux")
        print(self.driver.page_source)
        self.driver.find_element(by=By.LINK_TEXT,value="Forgotten password?").click()
        time.sleep(2)
        """self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="ount?").click()"""

        #self.driver.find_element(by=By.CSS_SELECTOR, value="input#identify_email").send_keys("sample")
        self.driver.find_element(by=By.CSS_SELECTOR, value="input[placeholder = 'Email address or mobile number']").send_keys("sample")

        self.driver.back();
        #xpatj
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value="//input[@data-testid='royal_email']").send_keys("xpathvalue")
        #self.driver.find_element(by=By.XPATH,value="//button[contains(@id,'u_0_')]").click()
        #self.driver.find_element(by=By.XPATH,value="//button[contains(@class,'6lth')]").click()
        #self.driver.find_element(by=By.XPATH,value="//button[starts-with(@id,'u_0')]").click()
        #self.driver.find_element(by=By.XPATH,value="//button[starts-with(@id,'u_0') or contains(@class,'6lth')]").click()
        self.driver.find_element(by=By.XPATH,value="//button[text()='Log in']").click()
obj=facbooklogin()
obj.login()