from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from behave import given,when,then
# Get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# Set Chrome options for incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")
# Create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

@given('Open main page and login')
def main_page (context):

#Navigate to the URL
    context.driver.get("https://soft.reelly.io/sign-in")
    sleep(4)

    #Search in user
context.app.sign_in_page.send_username()
#search_bar_1.clear("")
#search_bar_1.send_keys("Thompb155@gmail.com")

# Search password
context.app.sign_in_page.send_password()
#search_bar_2.clear()
#search_bar_2.send_keys("@qqD9Kfkpymn5Fb")

# Click login
context.app.sign_in_page.click_continue()
sleep(4)

@When('click on settings, subscription and payment options')
def settings_subs_payment (context):

#Click settings (uncomment if needed)
    context.app.sign_in_page.click_settings()
    sleep(4)

@Then('Verify subscription, back button, and upgrade plan')
def verification (context):

    #Click subscription

     check_1 = context.app.verify_page.click_subscription_button()
sleep(4)

if check_1 == "Subscription & payments":
    print("1st check passed")
else:
   print("not verified")

check_2 = context.app.verify_page.verify_back_button()

if check_2 == "Back":
    print("2nd check passed")
else:
   print("not verified")

check_3 = context.app.verify_page.verify_upgrade()

if check_3 == "Upgrade plan":
    print("3rd check passed")
else:
    print("not verified")

driver.quit()