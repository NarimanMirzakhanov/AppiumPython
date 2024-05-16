from appium.webdriver.common.appiumby import AppiumBy


class ScrollUtil:

    @staticmethod
    def scroll_to_text_by_android_UI_automator(text, driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiScrollable(new UiSelector().scrollable(true).instance("
                                                   "0)).scrollIntoView(new UiSelector().textContains(\""+text+"\").instance(0))").click()


    @staticmethod
    def scroll_to_text_by_appium_by(text, driver):
        # Scroll to element using scroll_to method
        scrollable_element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0))')
        text_element = scrollable_element.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')
        text_element.click()


    @staticmethod
    def scroll_to_text_exact_by_appium_by(text, driver):
        # Scroll to element using scroll_to_exact method
        scrollable_element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0))')
        text_element = scrollable_element.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}").textExact("{text}")')
        text_element.click()


    @staticmethod
    def swipe_up(how_many_swipes, driver):
        for i in range(1, how_many_swipes + 1):
            driver.swipe(550, 2000, 550, 500, 1000)

    @staticmethod
    def swipe_down(how_many_swipes, driver):
        for i in range(1, how_many_swipes + 1):
            driver.swipe(550, 720, 550, 2000, 1000)

    @staticmethod
    def swipe_right(how_many_swipes, driver):
        for i in range(1, how_many_swipes + 1):
            driver.swipe(100, 1000, 900, 1000, 1000)

    @staticmethod
    def swipe_left(how_many_swipes, driver):
        for i in range(1, how_many_swipes + 1):
            driver.swipe(900, 1000, 100, 1000, 1000)
