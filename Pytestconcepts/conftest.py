import pytest
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def launch():
    print("Beforetestcase")
    yield
    print("afterTestcase")

@pytest.fixture()
def launchBrowserandExit(request):
    web = webdriver.ChromeOptions()
    web.add_argument("--start-maximized")
    web.add_argument("--incognito")
    web.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
    request.cls.driver = driver
    yield
    driver.quit()
@pytest.fixture()
def Username():
    return["kumar.sathish189@gmail.com","Admin@123"]

@pytest.fixture(params=[{"username": "kumar.sathish189@gmail.com", "password": "Admin@123"},
                       {"username": "kumar.sathish189@gmail.com", "password": "Admin@123"}])
def Usernamewithmultidata(request):
    return request.param