import time

from conf import LOCATORS
from page_objects.Base_Page import Base_Page


class Demo_page(Base_Page):

    AddContent_button = LOCATORS.ADDCONTACT_Button
    AddContent_Edit = LOCATORS.ADDCONTACT_Edit



    def click_add_button(self):
        self.click_element(self.AddContent_button)
        self.Edit_elment(self.AddContent_Edit,'123')
