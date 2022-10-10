import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("launchBrowserandExit")
class Test_facebooklogin:

    def FBLoginwithvalidData(self,Username):
        self.driver.get("https://www.facebook.com/")
        #self.driver.find_element(by=By.ID, value="email").send_keys("kumar.sathish189@gmail.com")
        self.driver.find_element(by=By.ID,value="email").send_keys(Username[0])
        #self.driver.find_element(by=By.NAME, value="pass").send_keys("Admin@123")
        self.driver.find_element(by=By.NAME, value="pass").send_keys(Username[1])
        self.driver.find_element(by=By.XPATH, value="//button[text()='Log in']").click()
        #time.sleep(2)
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "(//*[@aria-label='Your profile'])[1]")))
        myprofilename=self.driver.find_element(by=By.XPATH,value="((//div[@role='navigation'])[3]//span//span)[1]").text
        assert myprofilename=="Sathish Ramakrishnan"
        self.driver.find_element(by=By.XPATH, value="(//*[@aria-label='Your profile'])[1]").click()
        #time.sleep(2)
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[text()='Log Out']//parent::div//parent::div)[1]")))
        self.driver.find_element(by=By.XPATH, value="(//span[text()='Log Out']//parent::div//parent::div)[1]").click()
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, "email")))

    def FBLoginwithinvalidData(self):
        expectedmessage="The password that you've entered is incorrect. Forgotten password?"
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element(by=By.ID,value="email").send_keys("kumar.sathish189@gmail.com")
        self.driver.find_element(by=By.NAME, value="pass").send_keys("test")
        self.driver.find_element(by=By.XPATH, value="//button[text()='Log in']").click()
        time.sleep(6)
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(//*[contains(@class,'clearfix')])[3]//div[2]")))
        actualmessage=self.driver.find_element(by=By.XPATH,value="(//*[contains(@class,'clearfix')])[3]//div[2]").text
        assert expectedmessage==actualmessage

    def FBLoginwithincorrectusername(self):
        expectedmessage="The password that you've entered is incorrect. Forgotten password?"
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element(by=By.ID,value="email").send_keys("acsvf2434355")
        self.driver.find_element(by=By.NAME, value="pass").send_keys(" ")
        self.driver.find_element(by=By.XPATH, value="//button[text()='Log in']").click()
        time.sleep(6)
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='email_container']//div[2]")))
        actualmessage=self.driver.find_element(by=By.XPATH,value="//*[@id='email_container']//div[2]").text
        print(actualmessage)
        assert expectedmessage==actualmessage

    def FBLoginwithvalidDatawithmultiple(self,Usernamewithmultidata):
        self.driver.get("https://www.facebook.com/")
        #self.driver.find_element(by=By.ID, value="email").send_keys("kumar.sathish189@gmail.com")
        self.driver.find_element(by=By.ID,value="email").send_keys(Usernamewithmultidata["username"])
        #self.driver.find_element(by=By.NAME, value="pass").send_keys("Test"])
        self.driver.find_element(by=By.NAME, value="pass").send_keys(Usernamewithmultidata["password"])
        self.driver.find_element(by=By.XPATH, value="//button[text()='Log in']").click()
        #time.sleep(2)
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "(//*[@aria-label='Your profile'])[1]")))
        self.driver.find_element(by=By.XPATH, value="(//*[@aria-label='Your profile'])[1]").click()
        #time.sleep(2)
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[text()='Log Out']//parent::div//parent::div)[1]")))
        self.driver.find_element(by=By.XPATH, value="(//span[text()='Log Out']//parent::div//parent::div)[1]").click()
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, "email")))

    def test_FBLoginwithvalidDatawithmultiplefromother(self, Usernamewithmultidatafromotherfile):
        self.driver.get("https://www.facebook.com/")
        # self.driver.find_element(by=By.ID, value="email").send_keys("kumar.sathish189@gmail.com")
        self.driver.find_element(by=By.ID, value="email").send_keys(Usernamewithmultidatafromotherfile["username"])
        # self.driver.find_element(by=By.NAME, value="pass").send_keys("Test"])
        self.driver.find_element(by=By.NAME, value="pass").send_keys(Usernamewithmultidatafromotherfile["password"])
        self.driver.find_element(by=By.XPATH, value="//button[text()='Log in']").click()
        # time.sleep(2)
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "(//*[@aria-label='Your profile'])[1]")))
        self.driver.find_element(by=By.XPATH, value="(//*[@aria-label='Your profile'])[1]").click()
        # time.sleep(2)
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[text()='Log Out']//parent::div//parent::div)[1]")))
        self.driver.find_element(by=By.XPATH, value="(//span[text()='Log Out']//parent::div//parent::div)[1]").click()
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, "email")))