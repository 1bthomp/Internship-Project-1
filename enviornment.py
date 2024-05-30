from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):

    #Get the path to the ChromeDriver executable
    driver_path = ChromeDriverManager().install()

    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    #create a new Chrome browser instance
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.maximize_window()

    from pages.sign_in_page import SignInPage
    from pages.verify_page import VerifyPage
    
    context.app = type('', (), {})()
    context.app.sign_in_page = SignInPage(context.driver)
    context.app.verify_page = VerifyPage(context.driver)
def after_all(context):
    context.driver.quit()

def before_scenario(context, scenario):

    pass

def after_scenario(context, scenario):

    pass

