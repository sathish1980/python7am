import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("launchBrowserandExit")
class commonFunctions():

    def waitforelementobeclickacle(self,path):
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,path)))

    def waitforelementobevisible(self,path):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH,path)))

    def waitforelementobepresentByID(self,path):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID,path)))

    def textToEneter(self,element,actualText):
        element.clear()
        element.send_keys(actualText)

    def elementToClick(self,element):
        element.click()