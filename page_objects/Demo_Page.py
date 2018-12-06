from conf import LOCATORS
from page_objects.Base_Page import Base_Page


class Demo_page(Base_Page):

    AddContent_button = LOCATORS.ADDCONTACT_Button



    def click_add_button(self):
        self.click_element(self.AddContent_button)
