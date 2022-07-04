from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers)
from features.logic.ui.pages.login.qa_assessment_utils import AssessmentAssertions
import pytest

test_assert=AssessmentAssertions()

"""------------------------------- Scenario(s)---------------------------------------------------------"""

@scenario(r'qa_assessment.feature', 'Verify login with valid username and password - Standard User')
def test_login_with_valid_credentials_standard_user():
    """Verify login with valid username and password - Standard User"""

@scenario(r'qa_assessment.feature', 'Verify login with valid username and password - Locked Out User')
def test_login_with_valid_credentials_locked_user():
    """Verify login with valid username and password - Locked Out User"""

@scenario(r'qa_assessment.feature', 'Verify login with valid username and password - Problem User')
def test_login_with_valid_credentials_problem_user():
    """Verify login with valid username and password - Problem User"""

@scenario(r'qa_assessment.feature', 'Verify login with valid username and password - Performance Glitch User')
def test_login_with_valid_credentials_performance_glitch_user():
    """Verify login with valid username and password - Performance Glitch User"""

@scenario(r'qa_assessment.feature', 'Verify login with invalid username')
def test_login_with_invalid_username():
    """Verify login with invalid username"""

@scenario(r'qa_assessment.feature', 'Verify login with invalid password')
def test_login_with_invalid_password():
    """Verify login with invalid password"""

@scenario(r'qa_assessment.feature', 'Verify login with invalid username and password')
def test_login_with_invalid_credentials():
    """Verify login with invalid username and password"""

@scenario(r'qa_assessment.feature', 'Verify login without username')
def test_login_with_no_username():
    """Verify login without username"""

@scenario(r'qa_assessment.feature', 'Verify login without password')
def test_login_with_no_password():
    """Verify login without password"""

@scenario(r'qa_assessment.feature', 'Verify login without username and password')
def test_login_with_no_username_and_password():
    """Verify login without username and password"""

@scenario(r'qa_assessment.feature', 'Verify login with only spaces in username field')
def test_login_with_only_spaces_in_username():
    """Verify login with only spaces in username field"""

@scenario(r'qa_assessment.feature', 'Verify login with only spaces in password field')
def test_login_with_only_spaces_in_password():
    """Verify login with only spaces in password field"""

@scenario(r'qa_assessment.feature', 'Verify login with only spaces in username and password fields')
def test_login_with_only_spaces_in_username_and_password():
    """Verify login with only spaces in username and password fields"""

@scenario(r'qa_assessment.feature', 'Verify login with leading spaces in username field')
def test_login_with_leading_spaces_in_username():
    """Verify login with leading spaces in username field"""

@scenario(r'qa_assessment.feature', 'Verify login with trailing spaces in username field')
def test_login_with_trailing_spaces_in_username():
    """Verify login with trailing spaces in username field"""

@scenario(r'qa_assessment.feature', 'Verify login with leading and trailing spaces in username field')
def test_login_with_leading_trailing_spaces_in_username():
    """Verify login with leading and trailing spaces in username field"""

@scenario(r'qa_assessment.feature', 'Verify login with leading spaces in password field')
def test_login_with_leading_spaces_in_password():
    """Verify login with leading spaces in password field"""

@scenario(r'qa_assessment.feature', 'Verify login with trailing spaces in password field')
def test_login_with_trailing_spaces_in_password():
    """Verify login with trailing spaces in password field"""

@scenario(r'qa_assessment.feature', 'Verify login with leading and trailing spaces in password field')
def test_login_with_leading_trailing_spaces_in_password():
    """Verify login with leading and trailing spaces in password field"""

@scenario(r'qa_assessment.feature', 'Verify login with username in all caps')
def test_login_with_username_all_caps():
    """Verify login with username in all caps"""

@scenario(r'qa_assessment.feature', 'Verify login with password in all caps')
def test_login_with_password_all_caps():
    """Verify login with password in all caps"""

@scenario(r'qa_assessment.feature', 'Verify logout functionality')
def test_logout_functionality():
    """Verify logout functionality"""

@scenario(r'qa_assessment.feature', 'Verify refreshing of credentials fields when page gets refreshed')
def test_page_refresh():
    """Verify refreshing of credentials fields when page gets refreshed"""

"""----------------------------- Given Statement(s)--------------------------------------------------"""

@given(parsers.cfparse('user is on Swag Labs Login Page on "{browser}" browser'))
def navigate_to_login_page(browser):
    """user is on Swag Labs Login Page on "{browser}" browser"""
    test_assert.open_browser(browser)

"""----------------------------- When Statement(s)--------------------------------------------------"""

@when('user logins with credentials from config file')
def login_with_config_credentials():
    """user logins with credentials from config file'"""
    test_assert.login_to_app()

@when('user clicks on Login button')
def click_login_button():
    """user clicks on Login button'"""
    test_assert.click_login_button()

@when('user clicks on Logout link')
def click_logout_link():
    """user clicks on Logout link'"""
    test_assert.click_logout_link()

@when('user refreshes the page')
def refresh_page():
    """user refreshes the page'"""
    test_assert.refresh_page()

@when(parsers.cfparse('user logins with "{username}" username and "{password}" password'))
def login_to_application(username,password):
    """user logins with "{username}" username and "{password}" password"""
    test_assert.login_to_app(username=username, password=password)

@when(parsers.cfparse('user logins without username'))
def login_to_application():
    """user logins without username"""
    test_assert.login_to_app(username="")

@when(parsers.cfparse('user logins without password'))
def login_to_application():
    """user logins without password"""
    test_assert.login_to_app(password="")

@when(parsers.cfparse('user logins without username and password'))
def login_to_application():
    """user logins without username and password"""
    test_assert.login_to_app(username="", password="")

@when(parsers.cfparse('user logins with "{username}" username'))
def login_to_application(username):
    """user logins with "{username}" username"""
    test_assert.login_to_app(username=username)

@when(parsers.cfparse('user logins with "{password}" password'))
def login_to_application(password):
    """user logins with "{password}" password"""
    test_assert.login_to_app(password=password)

@when(parsers.cfparse('user logins with only spaces in username and password fields'))
def login_to_application():
    """user logins with only spaces in username and password fields"""
    test_assert.login_to_app(username="  ", password="  ")


"""---------------------------- Then Statement(s)--------------------------------------------------"""

@then(parsers.cfparse('user should see "{content}" content on the page'))
def verify_content(content):
    """user should see "{content}" content on the page"""
    assert test_assert.verify_result(result=content)

@then(parsers.cfparse('user should see "{content}" validation message on the page'))
def verify_content(content):
    """user should see "{content}" validation message on the page"""
    assert test_assert.verify_result(validation=content)

@then('user should see empty username and password fields')
def verify_page_refresh():
    """user should see empty username and password fields"""
    assert test_assert.verify_page_refresh()


"""--------------------------Fixture methods to run at the end of each scenario execution-----------------------"""

@pytest.fixture(scope="module", autouse=True)
def test_clean_up_process():
    yield
    #Teardown
    test_assert.close_browser()

