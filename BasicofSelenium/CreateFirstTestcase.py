import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class firstclass():

    def firsttestcase(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.maximize_window()
        #self.driver.minimize_window()
        #self.driver.set_window_size(200, 600)
        self.driver.get("https://www.google.com")
        self.driver.get("https://www.facebook.com/")
        self.driver.back()
        time.sleep(2)
        self.driver.forward()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)

        self.driver.close()
        self.driver.quit()


        #driver = webdriver.Chrome("D:\Software\chromedriver_win32\chromedriver.exe", options=options)
bc= firstclass()
bc.firsttestcase()