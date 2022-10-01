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
class webtable():

    def tableimplementation(self,actualCountryName):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/table.xhtml")
        self.driver.maximize_window()
        totalPages=self.driver.find_elements(by=By.XPATH,value="//*[@class='ui-paginator-pages']//a")
        print(len(totalPages))
        for eachelement in range(1,len(totalPages)+1):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='ui-paginator-pages']//a["+str(eachelement)+"]")))
            self.driver.find_element(by=By.XPATH, value="//*[@class='ui-paginator-pages']//a["+str(eachelement)+"]").click()

            #eachelement.click()
            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #WebDriverWait(self.driver, 60).until(EC.staleness_of((self.driver.find_element(By.XPATH, value="//div[@class='ui-datatable-scrollable-body']//table//tbody//tr"))))
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,"//div[@class='ui-datatable-scrollable-body']//table//tbody//tr[1]//td[2]//span[3]")))

            time.sleep(1)
            totalRows=self.driver.find_elements(by=By.XPATH,value="//div[@class='ui-datatable-scrollable-body']//table//tbody//tr")
            for eachvalue in range(1,len(totalRows)+1):
               WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='ui-datatable-scrollable-body']//table//tbody//tr["+str(eachvalue)+"]//td[2]//span[3]")))

               countryName= self.driver.find_element(by=By.XPATH,value="//div[@class='ui-datatable-scrollable-body']//table//tbody//tr["+str(eachvalue)+"]//td[2]//span[3]").text

               if (countryName==actualCountryName):
                   representative=self.driver.find_element(by=By.XPATH,
                                            value="//div[@class='ui-datatable-scrollable-body']//table//tbody//tr[" + str(eachvalue) + "]//td[3]//span[2]").text
                   #print(representative)
                   Status = self.driver.find_element(by=By.XPATH,
                                                             value="//div[@class='ui-datatable-scrollable-body']//table//tbody//tr[" + str(eachvalue) + "]//td[5]//span[2]").text
                   #print(Status)
                   print(countryName ,representative,Status)

    def tableinfiorstpage(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/table.xhtml")
        self.driver.maximize_window()
        totalrows=self.driver.find_elements(by=By.XPATH,value="//*[@class='card']//div[@class='ui-datatable-scrollable-body']//table//tbody//tr")
        count=0
        for eachrow in totalrows:
            count+=1
            country=self.driver.find_element(by=By.XPATH,
                                      value="//*[@class='card']//div[@class='ui-datatable-scrollable-body']//table//tbody//tr["+str(count)+"]//td[2]//span[3]").text

            joindate = self.driver.find_element(by=By.XPATH,
                                               value="//*[@class='card']//div[@class='ui-datatable-scrollable-body']//table//tbody//tr[" + str(
                                                   count) + "]//td[4]").text
            print(country,joindate)

    def allpages(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/table.xhtml")
        self.driver.maximize_window()
        allpages=self.driver.find_elements(By.XPATH,value="//*[@class='ui-paginator-pages']//a")
        for eachpage in range(1,len(allpages)+1):

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("###############%%%%%%%%%%%%%%%%%%")
            #time.sleep(2)
            self.driver.find_element(By.XPATH,value="//*[@class='ui-paginator-pages']//a["+str(eachpage)+"]").click()
            time.sleep(2)
            totalrows = self.driver.find_elements(by=By.XPATH,
                                                  value="//*[@class='card']//div[@class='ui-datatable-scrollable-body']//table//tbody//tr")
            count = 0
            for eachrow in totalrows:
                count += 1
                country = self.driver.find_element(by=By.XPATH,
                                                   value="//*[@class='card']//div[@class='ui-datatable-scrollable-body']//table//tbody//tr[" + str(
                                                       count) + "]//td[2]//span[3]").text

                joindate = self.driver.find_element(by=By.XPATH,
                                                    value="//*[@class='card']//div[@class='ui-datatable-scrollable-body']//table//tbody//tr[" + str(
                                                        count) + "]//td[4]").text
                print(country, joindate)


obj=webtable()
obj.allpages()
#obj.tableimplementation("Germany")