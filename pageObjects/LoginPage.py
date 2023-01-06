class LoginPage:
    # Login Page Elements
    textbox_username_id = 'user-name'
    textbox_password_id = 'password'
    button_login_id = 'login-button'
    button_menu_id = 'react-burger-menu-btn'
    link_logout_linktext = 'Logout'

    def __init__(self,driver):
        self.driver = driver

    def set_Username(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def set_Password(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def click_Login(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    def click_Menu(self):
        self.driver.find_element_by_id(self.button_menu_id).click()

    def click_Logout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()


