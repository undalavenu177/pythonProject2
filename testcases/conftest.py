import  pytest
from pytest_metadata.hooks import pytest_metadata
from selenium import  webdriver
import pytest
@pytest.fixture()
def Setup(browser):
    if browser=='chrome':
       driver= webdriver.Chrome()

    elif browser=='firefox':
        driver = webdriver.Firefox()
    else:
        driver=webdriver.Edge()
    return driver



def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#pytest html report ,it is hook adding environment to html report
def pytest_configure(config):
    config.option.htmlpath = "reports/report.html"
    config.option.metadata = {
        "Project": "pythonProject2",
        "Tester": "venu",

    }

#hook for modify\delete Environment info to html report
@pytest.mark.optionalhook
def pytestmetadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)





