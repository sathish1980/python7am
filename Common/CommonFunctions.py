from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class commonFunctions():

    def waitforelementobeclickacle(self,driver,path):
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,path)))

    def waitforelementobevisible(self,driver,path):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH,path)))

    def textToEneter(self,element,actualText):
        element.clear()
        element.send_Keys(actualText)

    def elementToClick(self,element):
        element.Click()