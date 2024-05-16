import time

import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options

from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver(request):
    # global appium_service
    # appium_service = AppiumService()
    # appium_service.start()

    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Android',
        'appPackage': 'com.goibibo',
        'appActivity': '.common.HomeActivity',
        # 'noReset': True
    }
    capability_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://localhost:4723', options=capability_options)
    request.cls.driver = driver
    time.sleep(3)
    driver.press_keycode(4)
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ID, 'com.goibibo:id/buttonSkip').click()
    driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
    yield driver
    driver.quit()
    # appium_service.stop()


@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
