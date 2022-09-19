import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
class radioButton():

    def readiobuttonimplmentation(self,gender, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()
        self.driver.maximize_window()
        self.driver.find_element(by=By.CSS_SELECTOR, value="a[data-testid='open-registration-form-button']").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "firstname")))
        self.driver.find_element(by=By.NAME, value="firstname").send_keys("sathish")
        self.driver.find_element(by=By.NAME, value="lastname").send_keys("kumar")
        self.driver.find_element(by=By.NAME, value="reg_email__").send_keys("kumar.sathish189@gmail.com")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "reg_email_confirmation__")))
        self.driver.find_element(by=By.NAME, value="reg_email_confirmation__").send_keys("kumar.sathish189@gmail.com")
        if gender == "male":
            self.driver.find_element(by=By.XPATH, value="//input[@value='2']").click()
        elif gender == "female":
            self.driver.find_element(by=By.XPATH, value="//input[@value='1']").click()
        else:
            self.driver.find_element(by=By.XPATH, value="//input[@value='-1']").click()

obj=radioButton()
obj.readiobuttonimplmentation("trans")