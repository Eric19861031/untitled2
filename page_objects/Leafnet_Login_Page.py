from conf import LOCATORS
from page_objects.Base_Page import Base_Page

class Leafnet_Login_Page(Base_Page):

    Username_Text = LOCATORS.USERNAME_Text
    Password_Text = LOCATORS.PASSWORD_Text
    Login_Button = LOCATORS.LOGIN_Button

    def login_opt(self,username,password):
        self.Edit_elment(self.Username_Text,username)
        self.Edit_elment(self.Password_Text, password)
        self.click_element(self.Login_Button)
