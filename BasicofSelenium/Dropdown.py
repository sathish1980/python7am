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
        YeardropdownElement.select_by_visible_text("2012")

    def multiselectdropdown(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
        self.driver.maximize_window()
        time.sleep(2)
        fooditem=Select(self.driver.find_element(by=By.XPATH,value="//select[@id='second']"))
        if fooditem.is_multiple:
            fooditem.select_by_value("donut")
            fooditem.select_by_index(3)
            fooditem.select_by_visible_text("Pizza")
            time.sleep(2)
            fooditem.deselect_by_index(3)
            time.sleep(2)
            fooditem.deselect_all()


obj=dropdown()
obj.multiselectdropdown()