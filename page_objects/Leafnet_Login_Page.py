from selenium.webdriver.common.by import By

from conf import LOCATORS
from page_objects.Base_Page import Base_Page

class Leafnet_Login_Page(Base_Page):

    Username_Text = LOCATORS.USERNAME_Text_Id
    Password_Text = LOCATORS.PASSWORD_Text_Id
    Login_Button = LOCATORS.LOGIN_Button_Id

    def login_opt(self,username,password):
        self.Edit_elment(By.ID,self.Username_Text,username)
        self.Edit_elment(By.ID,self.Password_Text, password)
        self.click_element(By.ID,self.Login_Button)
