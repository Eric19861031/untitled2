import time

from appium import webdriver

class DriverFactory():

    def mobile_driver(self,os_name,os_version,device_name,app_package,app_activity,app_path):

        desired_capabilities = {}

        desired_capabilities['platformName'] = os_name
        desired_capabilities['platformVersion'] = os_version
        desired_capabilities['deviceName'] = device_name
        desired_capabilities['appPackage'] = app_package
        desired_capabilities['appActivity'] = app_activity
        desired_capabilities['app'] = app_path
        desired_capabilities['automationName'] = 'UiAutomator2'
        desired_capabilities['noReset'] = True

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
        time.sleep(5)
        return driver

