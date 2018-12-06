import unittest
from .DriverFactory import DriverFactory


class Borg:
    #The borg design pattern is to share state
    #Src: http://code.activestate.com/recipes/66531/
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

    def is_first_time(self):
        "Has the child class been invoked before?"
        result_flag = False
        if len(self.__dict__)==0:
            result_flag = True

        return result_flag

class Base_Page(Borg,unittest.TestCase):

    def __init__(self):
        Borg.__init__(self)
        if self.is_first_time():
            self.reset()

        self.driver_obj = DriverFactory()
        if self.driver is not None:
            self.start()

    def reset(self):
        self.driver = None

    def start(self):
        pass

    def register_driver(self,os_name,os_version,device_name,app_package,app_activity,app_path):
        self.driver = self.driver_obj.mobile_driver(os_name,os_version,device_name,app_package,app_activity,app_path)

    def click_element(self,locator):
        element = self.driver.find_element_by_xpath(locator)
        element.click()

    def Edit_elment(self,locator,text):
        element = self.driver.find_element_by_xpath(locator)
        element.send_keys(text)
