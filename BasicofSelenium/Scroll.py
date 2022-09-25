import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
class scroll():

    def scrollimplementation(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/dashboard.xhtml")
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 700)", "")
        time.sleep(1)
        obj.screenshot("verticallydown")
        # scroll up Vertically
        self.driver.execute_script("window.scrollTo(0, -400)", "")
        time.sleep(1)
        obj.screenshot("verticallyup")
        # scroll right horizontaly
        self.driver.execute_script("window.scrollTo(300, 0)", "")
        time.sleep(1)
        obj.screenshot("horizontalright")
        # scroll left horizontaly
        self.driver.execute_script("window.scrollTo(-300, 0)", "")
        time.sleep(1)
        obj.screenshot("horizontalleft")
        # scroll bottom
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        obj.screenshot("endofpage")
        # scroll up
        self.driver.execute_script("window.scrollTo(0, -0);")
        time.sleep(1)
        obj.screenshot("topofpage")
        # scroll to be element
        elementscroll=self.driver.find_element(by=By.XPATH,value="(//*[text()='Events'])[2]")
        element = self.driver.find_element(by=By.XPATH, value="//*[text()='Previous']")
        self.driver.execute_script("arguments[0].scrollIntoView();", elementscroll)
        element.click()
        obj.screenshot("toelement")

    def screenshot(self, filename):
        self.driver.save_screenshot(
                "C:\\Users\\sathishkumar\\PycharmProjects\\Pythongitupload\\Screenshot\\" + filename + ".png")

obj=scroll()
obj.scrollimplementation()