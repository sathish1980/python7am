from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Common.CommonFunctions import commonFunctions


class facebooklogout_page(commonFunctions):
    logout_dr = (By.XPATH, "(//*[@aria-label='Your profile'])[1]")
    logout_btn = (By.XPATH, "(//span[text()='Log Out']//parent::div//parent::div)[1]")

    def __init__(self,driver):
        self.driver=driver

    def ClickOnProfile(self):
        #WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//*[@aria-label='Your profile'])[1]")))
        self.waitforelementobeclickacle("(//*[@aria-label='Your profile'])[1]")
        #self.driver.find_element(by=By.XPATH, value="(//*[@aria-label='Your profile'])[1]").click()
        #profile=self.driver.find_element(by=By.XPATH, value="(//*[@aria-label='Your profile'])[1]")
        self.elementToClick(self.driver.find_element(*facebooklogout_page.logout_dr))

    def ClickOnLogoutButton(self):
        self.waitforelementobeclickacle("(//span[text()='Log Out']//parent::div//parent::div)[1]")
        #WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//span[text()='Log Out']//parent::div//parent::div)[1]")))
       # self.driver.find_element(by=By.XPATH,value="(//span[text()='Log Out']//parent::div//parent::div)[1]").click()
        #logout=self.driver.find_element(by=By.XPATH,value="(//span[text()='Log Out']//parent::div//parent::div)[1]")
        self.elementToClick(self.driver.find_element(*facebooklogout_page.logout_btn))
