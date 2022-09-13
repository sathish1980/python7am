import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class firstclass():

    def firsttestcase(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://www.google.com/")
        time.sleep(1)

        self.driver.close()

        #driver = webdriver.Chrome("D:\Software\chromedriver_win32\chromedriver.exe", options=options)
bc= firstclass()
bc.firsttestcase()