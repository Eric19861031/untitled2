import os

from page_objects.Page_Factory import PageFactory
from conf.app_info import *

APPPATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

def framework_test(os_name,os_version,device_name,app_package,app_activity,app_path):
    test_object = PageFactory.get_page_object("leaf_login_page")
    test_object.register_driver(os_name,os_version,device_name,app_package,app_activity,app_path)
    test_object.login_opt('96009900','aa123456')

if __name__ == '__main__':
    framework_test("android",
                   "8.1.0",
                   "0123456789ABCDEF",
                   leafnet["app_package"],
                   leafnet["app_activity"],
                   leafnet["app_path"])