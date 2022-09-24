import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
class listconcept():

    global driver
    def listconceptimplementation(self, expectedcountry,expectedcity,web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://leafground.com/select.xhtml")
        self.driver.maximize_window()
        # dropdown
        uiautomation=Select(self.driver.find_element(by=By.CLASS_NAME,value="ui-selectonemenu"))
        uiautomation.select_by_visible_text("Playwright")
        time.sleep(2)
        #list concept
        """self.driver.find_element(by=By.XPATH,value="//*[contains(@id,'country')]//div[contains(@class,'ui-selectonemenu-trigger')]").click()
         AllCountry=self.driver.find_elements(by=By.XPATH,value="//*[contains(@id,'country_items')]//li")
         for eachvalue in AllCountry:
             actualcountryname=eachvalue.text
             print(actualcountryname)
             if actualcountryname == expectedcountry:
                 eachvalue.click()
                 break"""
        countrydrodpdownarrow="//*[contains(@id,'country')]//div[contains(@class,'ui-selectonemenu-trigger')]"
        countrylist="//*[contains(@id,'country_items')]//li"
        self.listselect(expectedcountry, countrydrodpdownarrow, countrylist)
        citydrodpdownarrow = "//*[contains(@id,'city')]//div[contains(@class,'ui-selectonemenu-trigger')]"
        cityylist = "//*[contains(@id,'city_items')]//li"
        self.listselect(expectedcity, citydrodpdownarrow, cityylist)

    def listcountryconcept(self,countryName):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/select.xhtml")
        self.driver.maximize_window()
        countrydrodpdownarrow = "//*[contains(@id,'country')]//div[contains(@class,'ui-selectonemenu-trigger')]"
        self.driver.find_element(by=By.XPATH,value=countrydrodpdownarrow).click()
        allelement=self.driver.find_elements(by=By.XPATH,value="//*[contains(@id,'j_idt87:country_items')]//li")
        for eachelement in allelement:
            print(eachelement.text)
            if eachelement.text == countryName:
                eachelement.click()
                break

    def listcityconcept(self,cityName):
        time.sleep(2)
        citydrodpdownarrow = "//*[contains(@id,'city')]//div[contains(@class,'ui-selectonemenu-trigger')]"
        self.driver.find_element(by=By.XPATH,value=citydrodpdownarrow).click()
        allelement=self.driver.find_elements(by=By.XPATH,value="//*[contains(@id,'j_idt87:city_items')]//li")
        for eachelement in allelement:
            print(eachelement.text)
            if eachelement.text == cityName:
                eachelement.click()
                break

    def listselect(self,selectlistname,dropdownclikcelement,dropddownlist):
        time.sleep(2)
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, dropdownclikcelement)))
        self.driver.find_element(by=By.XPATH,value=dropdownclikcelement).click()
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, dropdownclikcelement)))
        Allvalues = self.driver.find_elements(by=By.XPATH, value=dropddownlist)
        for eachvalue in Allvalues:
            actualname = eachvalue.text
            print(actualname)
            if actualname == selectlistname:
                eachvalue.click()
                break

obj=listconcept()
obj.listcountryconcept("USA")
obj.listcityconcept("New York")