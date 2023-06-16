from selenium.webdriver.common.by import By


class login:
    textbox_username_name="email"
    textbox_password_id="pass"
    button_login_id="loginbutton"


    def __init__(self,driver):
        self.driver=driver
    def SetUsername(self,username):
        self.driver.find_element(By.NAME,self.textbox_username_name).send_keys(username)
    def Password(self, password):
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)
    def Login(self, login):
        self.driver.find_element(By.ID,self.button_login_id).click()





