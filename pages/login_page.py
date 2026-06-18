from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    """Page Object Model for Swag Labs login page"""
    
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")
    
    def __init__(self, driver: WebDriver):
        """Initialize LoginPage with WebDriver instance"""
        self.driver = driver
    
    def enter_username(self, username: str) -> None:
        """Enter username in the username field"""
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
    
    def enter_password(self, password: str) -> None:
        """Enter password in the password field"""
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
    
    def click_login(self) -> None:
        """Click the login button"""
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    
    def login(self, username: str, password: str) -> None:
        """Complete login flow with username and password"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self) -> str:
        """Get error message text if login fails"""
        return self.driver.find_element(*self.ERROR_MESSAGE).text