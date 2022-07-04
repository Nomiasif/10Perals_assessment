import time
import os
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.logic.ui.pages.login.qa_assessment_locators import loginLocators

class AssessmentAssertions:

    locators = loginLocators()

    def __init__(self):
        """
        Description:
            |  This method contains all the variables that have been used across the implementation in different methods
        """
        self.save_into_dict={}
        self.config_credentials=[]

    def get_config_details(self):
        """
        Description:
            |  This method can be used to get all the configuration related details for instance baseURL, username, password,
                environment on which the test scenario(s) need to be executed etc.
        """
        try:
            self.config_file_path=os.getcwd()+"\\config.yml"
            self.open_yml_file=open(self.config_file_path,'r')
            self.save_into_dict=yaml.load(self.open_yml_file,Loader=yaml.FullLoader)
            self.exec_env = self.save_into_dict['execution_env']
        except Exception as e:
            print('Error -->' + str(e))

    def get_base_url(self):
        """
        Description:
            |  This method can be used to get the baseURL from the Config file based on the environment selected in it.
                :return Type: String (BaseUrl)
                Sample method call:
                    get_base_url()
        """
        try:
            self.config_url = self.save_into_dict["env"][self.exec_env]["ui"]["base_url"]
            return self.config_url
        except Exception as e:
            print('Error -->' + str(e))

    def get_login_credentials(self):
        """
        Description:
            |  This method can be used to get the Login Credentials from the Config file based on the environment selected in it.
                :return Type: list (login_credentials)
                Sample method call:
                    get_login_credentials()
        """
        try:
            self.config_credentials.append(self.save_into_dict["env"][self.exec_env]["ui"]["username"])
            self.config_credentials.append(self.save_into_dict["env"][self.exec_env]["ui"]["password"])
            return self.config_credentials
        except Exception as e:
            print('Error -->' + str(e))

    def open_browser(self,browser):
        """
        Description:
            |  This method can be used to initialize the web driver and take the user to the login page of the application.
                browser: (String) -> A parameter to define the browser of user's choice where test cases need to be executed
                :return Type: None
                Sample method call:
                    open_browser("Chrome")
        """
        try:
            if browser.upper() == "EDGE":
                self.driver = webdriver.Edge(os.getcwd() + '/drivers/msedgedriver.exe')
            if browser.upper() == "CHROME":
                self.driver = webdriver.Chrome(os.getcwd()+'/drivers/chromedriver.exe')
            self.driver.maximize_window()
            self.get_config_details()
            self.base_url = self.get_base_url()
            self.driver.get(self.base_url)
        except Exception as e:
            print('Error -->' + str(e))

    def login_to_app(self,**kwargs):
        """
        Description:
            |  This method can be used to enter username and password in the login fields available on the Login page.
                username: (String) (Optional) -> A parameter to provide username of user's choice
                password: (String) (Optional) -> A parameter to provide password of user's choice
                :return Type: None
                Sample method call:
                    login_to_app(username= "test_user", password = "test_password")
        """
        try:
            self.config_credentials = self.get_login_credentials()
            self.username = kwargs.get("username")
            self.password = kwargs.get("password")
            if self.username is not None:
                self.driver.find_element(By.XPATH,self.locators.username_field).send_keys(self.username)
            else:
                self.driver.find_element(By.XPATH, self.locators.username_field).send_keys(self.config_credentials[0])
            if self.password is not None:
                self.driver.find_element(By.XPATH,self.locators.password_field).send_keys(self.password)
            else:
                self.driver.find_element(By.XPATH, self.locators.password_field).send_keys(self.config_credentials[1])
        except Exception as e:
            print('Error -->' + str(e))

    def click_login_button(self):
        """
        Description:
            |  This method can be used to click on Login button
                :return Type: None
                Sample method call:
                    click_login_button()
        """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.locators.login_button))).click()
        except Exception as e:
            print('Error -->' + str(e))

    def refresh_page(self):
        """
        Description:
            |  This method is used to Refresh the opened web page
                :return Type: None
                Sample method call:
                    refresh_page()
        """
        try:
            self.driver.refresh()
        except Exception as e:
            print('Error -->' + str(e))

    def click_logout_link(self):
        """
        Description:
            |  This method can be used to click on Logout link available on the LHN menu
                :return Type: None
                Sample method call:
                    click_logout_link()
        """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.locators.lhn_menu_button))).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.locators.logout_link))).click()
        except Exception as e:
            print('Error -->' + str(e))

    def verify_result(self, **kwargs):
        """
        Description:
            |  This method can be used to verify that the user's expected content is present on the page or not.
                result: (String) (Optional) -> A parameter provided by the user to check the expected content on the page
                validation: (String) (Optional) -> A parameter provided by the user to check the validation message on the page
                :return Type: Bool (bln_flag)
                Sample method call:
                    verify_result("Product")
        """
        try:
            result = kwargs.get("result")
            validation = kwargs.get("validation")
            bln_flag = False
            if result is not None:
                if "Accepted usernames are:" in result:
                    self.actual_result = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, "//h4[contains(text(),'" + result + "')]"))).text
                else:
                    self.actual_result = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'" + result + "')]"))).text
                if result.upper() in self.actual_result.upper():
                    bln_flag = True
                    print("Found the required content i.e. " + result)
            if validation is not None:
                self.heading_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'" + validation + "')]")))
                self.actual_result = self.heading_element.text
                if validation.upper() in self.actual_result.upper():
                    bln_flag = True
                    print("Found the required validation message i.e. " + validation)
            # This fixed time has been deliberately added for the assignment reviewer to just have a look at the required validation message or resultant content. Otherwise there is no need for adding it, since it will work fine without it as well
            time.sleep(1)
            return bln_flag
        except NoSuchElementException:
            print("Required content not found")

    def verify_page_refresh(self):
        """
        Description:
            |  This method can be used to verify that whether the page has been refreshed or not.
                :return Type: Bool (bln_flag)
                Sample method call:
                    verify_page_refresh()
        """
        try:
            bln_flag = False
            username_value_attribute = self.driver.find_element(By.XPATH,self.locators.username_field).get_attribute("value")
            password_value_attribute = self.driver.find_element(By.XPATH, self.locators.password_field).get_attribute("value")
            if username_value_attribute == '' and password_value_attribute == '':
                bln_flag = True
                print("Page has been refreshed")
            # This fixed time has been deliberately added for the assignment reviewer to just have a look at the required validation message or resultant content. Otherwise there is no need for adding it, since it will work fine without it as well
            time.sleep(1)
            return bln_flag
        except Exception as e:
            print('Error -->' + str(e))


    def close_browser(self):
        """
        Description:
            |  This method can be used to close the browser after test completion
                :return Type: None
                Sample method call:
                    close_browser()
        """
        try:
            self.driver.quit()
        except Exception as e:
            print('Error -->' + str(e))