import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class FBaccount():
    
    def createAccount(self, web=None):
        #self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        #self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=web)
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=web)
        self.driver.get("https://www.facebook.com/")
        #self.driver.implicitly_wait(60)
        self.driver.maximize_window()
        self.driver.find_element(by=By.CSS_SELECTOR,value="a[data-testid='open-registration-form-button']").click()
        #time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "firstname")))

        self.driver.find_element(by=By.NAME,value="firstname").send_keys("sathish kumar")

obj=FBaccount()
obj.createAccount()