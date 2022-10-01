import time

import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
class uploadanddownload():

    def upload(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://cleartax.in/paytax/UploadForm16")
        self.driver.maximize_window()
        self.driver.find_element(by=By.XPATH, value="(//*[contains(@class,'input-file-upload')])[1]").click()
        # this below line is used to copy the value in to the clip board
        pyperclip.copy("C:\\Users\\sathishkumar\\PycharmProjects\\AutomationPythonWeekdayAug\\Downloads\\products.pdf")
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(2)
        filenameafterupload = self.driver.find_element(by=By.XPATH,
                                                       value="(//*[contains(@class,'input-file-upload')])[2]").text
        print(filenameafterupload)
    def dowloadnormal(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/grid.xhtml")
        self.driver.find_element(by=By.ID, value="form:j_idt93").click()

    def download(self):
        chromeoptions = webdriver.ChromeOptions()
        downloadsettingpath = {
            "download.default_directory": "C:\\Users\\sathishkumar\\PycharmProjects\\Pythongitupload\\Downloadfiles\\"}
        chromeoptions.add_experimental_option("prefs", downloadsettingpath)
        chromeoptions.add_argument("--start-maximized")
        chromeoptions.add_argument("--incognito")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chromeoptions)
        self.driver.get("https://leafground.com/grid.xhtml")
        self.driver.find_element(by=By.ID, value="form:j_idt93").click()


obj=uploadanddownload()
obj.download()
