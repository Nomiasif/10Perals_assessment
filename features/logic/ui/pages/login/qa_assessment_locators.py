"""
    Description:
        |  This class contains the required locators
"""
class loginLocators:
    username_field = "//input[@id='user-name']"
    password_field = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    dashboard_title ="//span[contains(text(),'Products')]"
    lhn_menu_button = "//button[@id='react-burger-menu-btn' and contains(text(),'Open Menu')]"
    logout_link = "//a[@id='logout_sidebar_link' and contains(text(),'Logout')]"