from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def browser_init(context):
    """
    param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###
service = Service(executable_path='/Users/svetlanalevinsohn/careerist/18-python-selenium-automation/geckodriver')
context.driver = webdriver.Firefox(service=service)

    ### SAFARI ###
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(
         options=options,
         service=service
     )

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

