import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
class dropdown():

    def dropdownimplementation(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()
        self.driver.maximize_window()
        self.driver.find_element(by=By.CSS_SELECTOR, value="a[data-testid='open-registration-form-button']").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "firstname")))
        self.driver.find_element(by=By.NAME, value="firstname").send_keys("sathish")
        #### clic the dropdown

        DaydropdownElement=Select(self.driver.find_element(by=By.ID, value="day"))
        DaydropdownElement.select_by_index(3)

        MonthdropdownElement = Select(self.driver.find_element(by=By.ID, value="month"))
        MonthdropdownElement.select_by_value("6")

        YeardropdownElement = Select(self.driver.find_element(by=By.ID, value="year"))
        YeardropdownElement.select_by_visible_text("2005")

    def multiselectdropdown(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://leafground.com/select.xhtml")
        self.driver.maximize_window()


obj=dropdown()
obj.multiselectdropdown()