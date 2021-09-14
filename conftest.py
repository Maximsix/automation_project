
import pytest
from selenium.webdriver import Chrome

from automation_project.pages.dashboard import Dashboard


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("../drivers/chromedriver")
    driver.maximize_window()
    driver.get('https://bigl.ua/')
    yield driver

    driver.quit()


@pytest.fixture
def dashboard(driver) -> Dashboard:
    yield Dashboard(driver)
