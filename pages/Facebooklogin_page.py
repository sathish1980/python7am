from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from Common.CommonFunctions import commonFunctions


class facebooklogin_page(commonFunctions):

    usrname = (By.ID, "email")
    psword = (By.ID, "pass")
    login_btn = (By.XPATH, "//button[text()='Log in']")
    forgot_pwd = (By.LINK_TEXT, "/Forgotten password?")
    Create_acct = (By.XPATH, "//a[text()='Create New Account']")

    def __init__(self,driver):
        self.driver=driver

    def EnterUsername(self,username):
        self.waitforelementobepresentByID("email")
        #WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, "email")))
        #self.driver.find_element(by=By.ID, value="email").send_keys(username)
        #usname=self.driver.find_element(by=By.ID, value="email")
        self.textToEneter(self.driver.find_element(*facebooklogin_page.usrname),username)

    def EnterPassword(self,password):
        #self.driver.find_element(by=By.NAME, value="pass").send_keys(password)
        #pwd = self.driver.find_element(by=By.ID, value="pass")
        self.textToEneter(self.driver.find_element(*facebooklogin_page.psword), password)

    def Clickloginbutton(self):

        #self.driver.find_element(by=By.XPATH, value="//button[text()='Log in']").click()
        self.elementToClick(self.driver.find_element(*facebooklogin_page.login_btn))

    def ClickForgotPassword(self):
        self.driver.find_element(by=By.LINK_TEXT, value="Forgotten password?").click()

    def ClickCreateAccountButton(self):
        self.driver.find_element(by=By.XPATH, value="//*[@data-testid='open-registration-form-button']").click()