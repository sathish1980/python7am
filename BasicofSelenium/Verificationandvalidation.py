import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
class vv():

    def vvimplementation(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/dashboard.xhtml")
        self.driver.maximize_window()
        self.driver.find_element(by=By.XPATH,value="//*[text()='Browser']//ancestor::a").click()
        self.driver.find_element(by=By.XPATH,value="//*[text()='Alert']//ancestor::a").click()
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "(//*[text()='Show']//ancestor::button)[1]")))
        print(self.driver.title)
        print(self.driver.current_url)
        print(self.driver.find_element(by=By.XPATH,value="(//*[text()='Show'])[1]").get_attribute("class"))
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        #validation
        print(self.driver.find_element(by=By.XPATH,value="(//*[text()='Show'])[1]").is_enabled())
        print(self.driver.find_element(by=By.XPATH, value="(//*[text()='Show'])[1]").is_displayed())
        print(self.driver.find_element(by=By.XPATH, value="(//*[text()='Show'])[1]").is_selected())
obj=vv()
obj.vvimplementation()